###########################
Refactoring all the things!
###########################

:category: config

**********
New config
**********

We're on day 8 already (time flies!), and I'm almost finished refactoring the
entire qutebrowser codebase to use the new config. There are still some issues
here and there and some missing changes (for ``:set`` and ``qute:config``
mostly), but qutebrowser is now mostly usable again without needing any of the
old config code.

This took much `more work`_ than I expected, and much of it was quite tedious:

.. code-block:: raw

   98 files changed, 4270 insertions(+), 3865 deletions(-)

I'm glad I'm almost done with that part, the real fun (working on reading and
writing the YAML/Python files) will begin soon!

.. _more work: https://github.com/qutebrowser/qutebrowser/compare/new-config

****************
Jinja templating
****************

qutebrowser uses `jinja2`_ as a template engine to build Qt stylesheets from
config options, and then style widgets accordingly.

While refactoring the config, I noticed that it's jinja's default behavior to
not raise an exception if an attribute is invalid - instead, it just assumes an
empty default value.

Because this made it very hard to find issues during the refactoring, I made my
jinja environment `more strict`_ so an ``AttributeError`` is actually caught
when it happens.

.. _jinja2: http://jinja.pocoo.org/
.. _more strict: https://github.com/qutebrowser/qutebrowser/commit/df631c5a4a6fd5cd2f0f9d5eabdc66b56647df30

******************
QtWebKit segfaults
******************

Another thing I tried to track down is why the new QtWebKit packages for
Archlinux segfault a lot - I've been getting a lot of reports about this lately,
and indeed I could reproduce a crash when writing replies on Reddit.

I first thought this was some bug in the `updated QtWebKit-NG package`_, but
then I could reproduce it with the legacy QtWebKit package which hasn't seen any
changes in the last couple of months as well...

As this segfault was affecting a lot of qutebrowser users (anyone using it on
Archlinux with QtWebKit, pretty much), I decided to dig a bit deeper into it.

The segfault happens here:

.. code-block:: raw

   WTF::StringImpl::copyChars<char16_t>()
   JSC::jsSpliceSubstringsWithSeparators()
   JSC::replaceUsingRegExpSearch()
   JSC::replace()
   JSC::stringProtoFuncReplace()

From the stacktrace, this looked like something which would be happening when
you call ``"abc".replace(/a/, "b")`` in JavaScript. I tried various various
variations of that, but couldn't get it to crash.

I then thought I could get JavaScript to log everything passed to ``.replace()``
on a string, hoping I could get the string which causes the crash.

A fellow student of mine came up with this, which worked beautifully:

.. code-block:: javascript

   (function(replace) {
       String.prototype.replace = function() {
           console.log(this, arguments);
           return replace.apply(this, arguments);
       };
   })(String.prototype.replace)

While I saw all those calls in the console, I didn't see the call which actually
caused the crash...

So I took a closer look at the C++ stacktrace, and was able to get the string
from there. It was some 9000 chars of HTML edited via JavaScript...

After some more tinkering, I was able to get it down to this example which
crashes when run in ``jsc``, a command-line JavaScript interpreter coming with
WebKit:

.. code-block:: javascript

   s = 'xxxxxxxxxxxxxxAxxxxxxxxxxxxxxxxxxxxA–'; s.replace(/A/g, 'b')

I then compiled WebKitGTK (which is the upstream of QtWebKit, as strange as that
sounds) with GCC 7, and indeed it was reproducable there as well.

The C++ code where it crashes turned out to be this:

.. code-block:: cpp

   template <typename T> static void copyChars(
       T* destination, const T* source, unsigned numCharacters)
   {
     if (numCharacters == 1) {
       *destination = *source;
       return;
     }

     if (numCharacters <= s_copyCharsInlineCutOff) {
       unsigned i = 0;
   #if (CPU(X86) || CPU(X86_64))
       const unsigned charsPerInt = sizeof(uint32_t) / sizeof(T);

       if (numCharacters > charsPerInt) {
         unsigned stopCount = numCharacters & ~(charsPerInt - 1);

         const uint32_t* srcCharacters =
             reinterpret_cast<const uint32_t*>(source);
         uint32_t* destCharacters =
             reinterpret_cast<uint32_t*>(destination);
         for (unsigned j = 0; i < stopCount; i += charsPerInt, ++j)
           destCharacters[j] = srcCharacters[j];
       }
   #endif
       for (; i < numCharacters; ++i)
         destination[i] = source[i];
     } else
       memcpy(destination, source, numCharacters * sizeof(T));
   }

This is essentially an optimized version of ``memcpy``, which does the copying
inline when it's less than 20 (``s_copyCharsInlineCutOff``) chars. Nowadays, a
simple ``memcpy`` would probably be optimized to something equivalent, but there
we are...

I first was confused about how that optimized part (in the ``#if``) worked
together with the "simple" part below, and how the inner loop uses ``j`` and
``i``, but eventually I got it, and was sure that part was actually fine.

(The optimized part copies 4-byte blocks at once, and then the part below copies
the rest)

I didn't have an idea what was wrong, but people in the ``#gcc`` IRC channel
had: Turns out it's undefined behavior when you access an ``uint16_t*`` via an
``uint32_t*`` - that was when I learned about `type punning`_ and
`strict aliasing`_...

And indeed, `removing`_ that optimized loop made things run fine.

The "fun" thing is that WebKit is compiled using the ``-fno-strict-aliasing``
flag to GCC, which should actually allow this kind of thing. Still, with GCC 6
it works fine, with GCC 7 it crashes - so this might turn out to be some kind of
GCC bug.

I haven't opened an upstream WebKit bug for this yet, but I'll do so today or
tomorrow unless the QtWebKit maintainer does so.

I also requested my workaround to be `applied`_ to Archlinux' packages, but that
hasn't happened so far.

.. _updated QtWebKit-NG package: https://lists.schokokeks.org/pipermail/qutebrowser-announce/2017-June/000017.html
.. _type punning: https://www.cocoawithlove.com/2008/04/using-pointers-to-recast-in-c-is-bad.html
.. _strict aliasing: http://dbp-consulting.com/tutorials/StrictAliasing.html
.. _removing: https://github.com/annulen/webkit/issues/562#issuecomment-307911343
.. _applied: https://bugs.archlinux.org/task/54428
