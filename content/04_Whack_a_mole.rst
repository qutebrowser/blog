###########################
Day 4: Playing whack-a-mole
###########################

:category: webengine
:tags: pytest

Today, I felt like I was forced to play whack-a-mole:

.. figure:: images/mole.png
   :alt: whack-a-mole

   (Image cc by-nc-sa by `Mommysaurus75`_ on Flickr)

********
The good
********

Everything started nicely: Someone posted a `pull request`_ to handle links
with (non-standard) spaces correctly with hints
(``<a href=" http://example.com ">``), I told them how to add a test, they did,
I fixed a small issue, bam, merged.

.. _Mommysaurus75: https://www.flickr.com/photos/mommysaurus75/5518643830/
.. _pull request: https://github.com/The-Compiler/qutebrowser/pull/1564

*******
The bad
*******

Then I fixed some tests which were failing due to changes from yesterday. The
first one was a test which failed reliably on Windows since changing the test
to use a real file instead of a mock.

It tests a function getting the last **n** bytes from a file, with 64 bytes.
On Windows, it expected:

.. code-block:: raw

    58
   new data 59
   new data 60
   new data 61
   new data 62
   new data 63

but got:

.. code-block:: raw

   ew data 59
   new data 60
   new data 61
   new data 62
   new data 63

Unfortunately pytest failed to produce a nice readable diff like it usually
does:

.. code-block:: raw

   > assert lineparser.get_recent(size) == data
   E assert ['ew data 59\...ew data 63\n'] ==
            [' 58\n', 'new...ew data 63\n']
   E   At index 0 diff: 'ew data 59\n' != ' 58\n'
   E   Right contains more items, first extra item: 'new data 63\n'

After printing the raw values staring at them for some seconds, I figured the
few missing bytes were exactly the count of ``\r`` (carriage returns) you'd
need to insert.

While Python takes care of the conversion when reading/writing files, when
getting the last 64 bytes of a file, you'll get less data on Windows.

I fixed the code to use ``os.linesep`` instead of ``\n``, and it still was off
by one on Windows, but not in Linux:

.. code-block:: python

   # data = '\n'.join(self.BASE_DATA + new_data)
   data = os.linesep.join(self.BASE_DATA + new_data)
   data = [e + '\n' for e in data[-(size - 1):].splitlines()]

I then figured out I actually had an off-by-one error there - the
"``-(size - 1)``" should actually be just ``-size``. What I **actually** was
missing is a "``+ os.linesep``" for the final line ending. I guess when
originally implemented it I thought I just was off by one while `slicing`_ and
naively fixed it the wrong way...

With that `out of the way`_, I looked at the other test which was flaky - it
reads the history a qutebrowser subprocess, definitely waits until the
subprocess has written it, and still sometimes ends up with an empty file.

I let the logs sink in for a bit, but I still have no idea what'd cause it. In
the end I just ended up `marking`_ the test as flaky using
`pytest-rerunfailures`_. This means it'll be run a second time if it fails, and
if it passes then, it's assumed to be okay.

This is definitely less than ideal, but it's better than having a test which
fails sometimes for no apparent reason, and better than not testing this
functionality at all.

.. _slicing: http://stackoverflow.com/a/509295/2085149
.. _out of the way: https://github.com/The-Compiler/qutebrowser/commit/d6926f06227616c0f659ff1f39ec84f0e9b67465
.. _marking: https://github.com/The-Compiler/qutebrowser/commit/9e1d20017c6e7a59083d1a2bc1af0e4710b0ffb2
.. _pytest-rerunfailures: https://github.com/pytest-dev/pytest-rerunfailures

********
The ugly
********

After all that, I updated to Qt 5.6.1 to check if a `segfault on exit`_ was
fixed like claimed in the bug report.

Turns out it wasn't, but instead there was a new `bogus warning`_ and a
`weird behavior change`_ I needed to take care of in my testsuite.

.. _segfault on exit: https://bugreports.qt.io/browse/QTBUG-52988
.. _bogus warning: https://github.com/The-Compiler/qutebrowser/commit/c390c797b2de96b18db21eb3cdcf7829a6220598
.. _weird behavior change:  https://github.com/The-Compiler/qutebrowser/commit/2d54c927e34abaead2366aeac5465da400b1a9f4

Now I hoped I was finally done fixing weird bugs - turns out that was just the
beginning. Someone joined the IRC channel and reported how hints often don't
work at all for them since the big hint changes from Monday.

I couldn't reproduce the issue, and what we were seeing made no sense at all.
See the `bug report`_ I opened to see all the gory details. If I tried to write
them up here, I'd probably just hopelessly confuse myself again.

They are an experienced Python programmer as well, and after over 3.5h of
debugging, we gave up.

I ended up `adding a setting`_ which allows to revert back to the old Python
implementation. It's less accurate but also faster than the new (JS) one, so
some people might prefer that anyways.

.. _bug report: https://github.com/The-Compiler/qutebrowser/issues/1568
.. _adding a setting: https://github.com/The-Compiler/qutebrowser/commit/035526848eb40cb95f70926667911f5bc5f8e393

**********************
And some other changes
**********************

Before and after that frustrating debugging session, I also managed to get some
other changes in:

I `improved the error message`_ when an invalid link is clicked as I stumbled
upon it and it confused me.

I also `started refactoring`_ the history implementation and adding a few tests
to it, as I still need to do a small change to handle redirects nicely before
releasing v0.7.0 (what is what I originally planned to do today...).

The refactoring also allowed me to split off the QtWebKit-specific part of it
nicely, so that's already a little step closer to QtWebEngine as a nice side
effect!

.. _improved the error message: https://github.com/The-Compiler/qutebrowser/commit/089131c79dbc069c5c5ce30f70b4392d1bd7d80a
.. _started refactoring: https://github.com/The-Compiler/qutebrowser/compare/34ba44b0a31272c93517be422f91684c39221205~1...14a04f1535f8e8df5813b8d7b3b4420650e5400b

*******
Outlook
*******

The todo list for tomorrow roughly looks like this:

- Handle redirects in saved history
- Merge the trivial doc PR for the Debian packages
- Package and release v0.7.0

I really want to release v0.7.0 tomorrow unless another serious regression is
found (fingers crossed!).

And then full-speed towards QtWebEngine support next week!
