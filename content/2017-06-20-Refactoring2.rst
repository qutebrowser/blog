#########################################################
Refactoring more things, a working YAML config, and more!
#########################################################

:category: config

It's day 12 of 20, and I did a lot more work on making everything (including
tests) use the new config. I also implemented initial support for reading
from/writing to YAML files.

This is how things look now:

.. code-block:: raw

   154 files changed, 6128 insertions(+), 7000 deletions(-)

This is with all end2end tests also adjusted for the new config. I haven't
looked at the unit tests yet, but things are getting better!

.. code-block:: raw

   1001 passed, 42 skipped, 10 xfailed in 374.00 seconds

I was also finally able to `remove`_ almost all the legacy config code, so it's
only the new code around now.

Setting values and saving/restoring them already works, with either ``:set`` or
``qute://settings``. As I already was working on ``qute://settings``, I also
`made it work`_ with QtWebEngine, which was something which was requested a lot.

.. _remove: https://github.com/qutebrowser/qutebrowser/commit/26753bfb4ff8c1d0bcff494ece734804f16afc2f
.. _made it work: https://github.com/qutebrowser/qutebrowser/commit/15e803c02af52d99f11db9b6233a1fdfd4312d0d

************
config types
************

There's a ``configtypes.py`` module in qutebrowser which defines all the
different types (such as a string, or a list of regexes) in the configuration.

A setting type also can convert a value (of its type) to either a string (for
`:set`), or to whatever the Python code using the config expects (such as a
Python list of compiled regex patterns).

When implementing the new config, I first thought that with the new config, the
value which will be stored internally would be the converted Python value.

Originally, a type was looking like this:

.. code-block:: python

   class BaseType:

       def from_py(self, value):
           # Convert the value from a config.py or YAML file to a
           # value used by the rest of the code (and stored as
           # internally).

       def from_str(self, value):
           # Convert the value from plaintext to a value used like
           # explained above.

However, I found out that that's actually a problem - for some kind of values
(like a ``QColor`` object, or a proxy object), they can't be converted back to a
string losslessly.

The API also was quite confusing - a lost a bit of time because I once assumed
``from_py`` would be what gets the value from qutebrowser's code.

I ended up instead storing the value as it's saved in ``config.py`` or the YAML
file, so as a string/list/dict/bool/int/float.

Then, a type looks like this:
            
.. code-block:: python

   class BaseType:

       def from_str(self, value):
           # Convert the value from plaintext to a YAML-like value.
           # (which is also what's stored internally)

       def from_py(self, value):
           # Convert the value from how it's stored internally
           # to what is used by the rest of the code.

This worked out pretty well, and made it easy to implement ``:set`` and reading
from YAML.

********
Mutables
********

Another big issue I was facing is how to deal with mutables. If a ``config.py``
would do this:

.. code-block:: python

   headers = conf.content.custom_headers
   headers['X-Foo'] = 'bar'

the config wouldn't get updated, and that's probably quite
unexpected.

First I tried solving that by returning custom list/dict objects from the
config, which notifies the config when they've been mutated:

.. code-block:: python

   class ConfigNotifierMixin:
   
       def __init__(self, data, manager, option, origin):
           self._inited = False
           self._manager = manager
           self._option = option
           self._origin = origin
           super().__init__(data)
           self._inited = True
   
       def __getitem__(self, name):
           item = super().__getitem__(name)
           return wrap_value(item, manager=self._manager,
                             name=self._option,
                             origin=self._origin)
   
       def __setitem__(self, name, value):
           value = wrap_value(value, manager=self._manager,
                              name=self._option,
                              origin=self._origin)
           super().__setitem__(name, value)
           if not self._inited:
               return
           self._manager.set(self._option, self._origin)
   
       def __delitem__(self, name):
           super().__delitem__(name)
           if not self._inited:
               return
           self._manager.set(self._option, self._origin)
   
   
   class ConfigDict(ConfigNotifierMixin, collections.UserDict):
   
       pass
   
   
   class ConfigList(ConfigNotifierMixin, collections.UserList):
   
       pass
   
   
   def wrap_value(val, *, manager, name, origin):
       if isinstance(val, (list, ConfigList)):
           return ConfigList(val, manager, name, origin)
       elif isinstance(val, (dict, ConfigDict)):
           return ConfigDict(val, manager, name, origin)
       else:
           return val

But I wasn't been able to make that work properly. Either some sub-values
weren't wrapped properly, or I got some funny infinite recursion in Jinja (the
templating engine qutebrowser uses).

In the end, I went for a `simpler solution`_ - for every value qutebrowser
returns, it saves a reference to it as well as a (deep) copy of it. Then, after
e.g. a ``config.py`` has been executed, it checks the saved values for changes,
and calls ``config.set`` as appropriate.

.. _simpler solution: https://github.com/qutebrowser/qutebrowser/commit/6e4a5319cee60278106b51c57e30f639a1051449

*********************
YAML saving/restoring
*********************

With all the converting already done in ``configtypes``, implementing this was
`a breeze`_. Now whatever has been changed via ``:set`` or ``qute://settings``
is saved to a YAML file (and loaded from there), and it was really easy to
implement that. The new config code being much cleaner and more modular already
payed off, even when it was a long way there!

As an example, when doing ``:set tabs.position left`` and quitting, this ends up
in ``~/.config/qutebrowser/autoconfig.yml``:

.. code-block:: yaml

   # DO NOT edit this file by hand, qutebrowser will overwrite it.
   # Instead, create a config.py - see :help for details.
   
   global:
     tabs.position: left

.. _a breeze: https://github.com/qutebrowser/qutebrowser/commit/6375530bfad5daee5789d3308851e809e491ae5c

***********
Keybindings
***********

Currently, the bindings are just something like:

.. code-block:: python

   bindings.commands = {
       'normal': {
           'gg': 'scroll-perc 0',
           ...
       },
       ...
   }

in the config - i.e., just a value like any other, set to a dict of dicts.

However, that turned out to not be very practical - if a single binding is
changed, the whole ``bindings.commands`` value is treated as modified, and thus
saved in the config.

This definitely needs some re-thinking and probably some special-casing.

**************
SQL completion
**************

The `pull request`_ for the new sqlite completion (and related completion
refactoring) also has seen some progress (mostly thanks to ``@rcorre``).

Today, I also fixed a data corruption issue which showed up in the SQL branch
since somewhen recently - turned out it was `an issue`_ with how SQL columns
were inserted into the database, which caused things to get mixed up.

I also decided to give `reviewable.io`_ another try, as reviewing stuff of this
size is really cumbersome with GitHub... I did an `initial review`_ there, and
now I'm wondering whether that'll work out better.

.. _pull request: https://github.com/qutebrowser/qutebrowser/pull/2295
.. _an issue: https://github.com/qutebrowser/qutebrowser/commit/29ce1b381121645589cb18906682fe79b11a69b8
.. _reviewable.io: https://reviewable.io/
.. _initial review: https://reviewable.io/reviews/qutebrowser/qutebrowser/2295

***********************
Dropping legacy support
***********************

With v1.0 at the horizon, it was also time to think about (finally) throwing out
some legacy support.

I opened an issue `to discuss`_ about what'd be possible to drop, and what needs
to stay. **If you use qutebrowser on something other than
Archlinux/Windows/macOS, this will probably affect you** - and I'd love your
input!

.. _to discuss: https://github.com/qutebrowser/qutebrowser/issues/2742

*************
Next few days
*************

As mentioned in the Kickstarter already, I'm having a planned eye surgery. I'm
leaving for the hospital tomorrow (Wednesday) and should be back home on Friday
if everything goes well.

I can't say when I'll feel well enough to start coding again, but I hope that's
already early next week somewhen.

Also, somewhen after next week I'll take a longer "break" because I need to
start learning for my exams coming up in August (and there's **a lot** to do).

This means the rest of the work (and also, taking care of the shirts) might be
postponed until September, after my exams. But it all really depends on how much
days I'll be able to do next week.

Also, for the sake of transparency: I'm starting to worry whether I can really
do everything I planned during the crowdfunded time, as only 8 days are left
now. The initial refactoring took a lot more time than I thought it would. I
hope adding the Python config API will be just as easy as adding the YAML was,
but then there are still per-domain settings which probably require a bit of
work. My hope is that I'll get (a prototype of) those into the ``new-config``
branch by the end, but I'm not sure whether I'll manage to get everything merged
to ``master`` by then.

Still, of course I'm fully committed to making this happen (after my exams,
though) even in my spare time. The biggest part (hours and hours of refactoring,
essentially) is done already. It just means it might take a bit longer than
expected.

Or maybe everything will work nicely and all this is unfounded.
I don't know yet.
