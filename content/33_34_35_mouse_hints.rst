####################################################
Days 33-35: Mouse functionality, and rewriting hints
####################################################

:category: webengine

Past Friday and on Monday I wasn't working on qutebrowser (apart from some
usual maintaince tasks) as I was traveling to/from `Evoke`_ (which was great!).
But there's a lot to write about from Wednesday, Thursday and today!

.. _evoke: http://www.evoke.eu/

*******
History
*******

The first thing I got to work on Wednesday was the history - after `moving`_ the
history implementation out of ``WebView``, all it took was a `single line`_ (and
a `bugfix`_ in that single line) to implement history for QtWebEngine.

After that I also `split`_ the ``history`` module into a QtWebKit specific and a
generic file, to avoid importing QtWebKit if it's not needed.

.. _moving: https://github.com/The-Compiler/qutebrowser/commit/77531d09df3ff891f57843a0752379017c05760c
.. _single line: https://github.com/The-Compiler/qutebrowser/commit/393178262eeb69ecb6e420891e2aca4dc20f5b4d
.. _bugfix: https://github.com/The-Compiler/qutebrowser/commit/cc693f17caa5cfcf0a2910d89132b5095f8677e0
.. _split: https://github.com/The-Compiler/qutebrowser/commit/33193d7dd4578238b18c07526c051f326821d3f5

*****
Mouse
*****

I moved all mouse handling to an `event filter`_ so it was decoupled from any
QtWebKit code and - in theory - would just work with QtWebEngine.

However, that `took`_ some more effort as QtWebEngine actually forwards all
mouse events to a ``QOpenGLWidget`` (on which Chromium draws), and that also
seems to be swapped out sometimes...

This initially just handled back/forward keys on mice which have them, but I
then gradually moved over more mouse functionality:

- `Mouse wheel zooming <https://github.com/The-Compiler/qutebrowser/commit/1a94cb551c829f9d8db37a07d9ea476e715aa94c>`_
- `Open-target handling <https://github.com/The-Compiler/qutebrowser/commit/3bffb71b551edcd4c39e9226e9a3691b3f2dba75>`_ (ctrl-click / middle-click / also affects hints)
- `Rocker gestures <https://github.com/The-Compiler/qutebrowser/commit/fb07655e5614cca1eedff7a53b46d310bee96e33>`_
- `Insert mode on click <https://github.com/The-Compiler/qutebrowser/commit/1138d068e6dbd5a15a6e74a7323c53b451ba3e40>`_ (also affects hints)

.. _event filter: https://github.com/The-Compiler/qutebrowser/commit/f908d29a5ff1af283d6f66e181203bdfbb26cce2
.. _took: https://github.com/The-Compiler/qutebrowser/commit/64afc562b60d62446c67814b77b3ff5240ad1287

*****
Hints
*****

Probably the most missed feature, and I made some important progress, though it's not quite there yet ;)

Last week, I `moved`_ some hinting code out of ``WebView``, and today I did a
complete `rewrite`_ of how hints are drawn.

In the ``new-hints`` branch, hints are now simply a `QLabel`_ shown on an
overlay over the web contents instead of being a HTML element inserted into the
page.

Apart from solving some issues like `#925`_ where the hints are influenced by
the page stylesheet, this makes the implementation much more straightforward and
makes it work with the same code on both backends.

Initially, this looked quite wrong:

.. image:: /images/hints_ugly_small.png
   :alt: wrongly drawn hints
   :target: /images/hints_ugly.png

But after getting the sizing and more styling correct, they look better:

.. image:: /images/hints_fixed_small.png
   :alt: correctly drawn hints
   :target: /images/hints_fixed.png

What's quite a challenge is that the old config used WebKit gradients (as the
hint labels were actual page elements), so with the native drawing, the
configuration is quite a bit different. The opacity is also part of the color,
so I removed the ``hints -> opacity`` setting.

I tried to auto-migrate the trivial cases (like the default setting, or similar
gradients), but for more complex existing settings qutebrowser will simply
display an error and let the user fix it.

.. _moved: https://github.com/The-Compiler/qutebrowser/commit/421b14681f21aa85b2b70b6ba1d7176e0f0404dd
.. _rewrite: https://github.com/The-Compiler/qutebrowser/compare/master...new-hints
.. _QLabel: http://doc.qt.io/qt-5/qlabel.html
.. _#925: https://github.com/The-Compiler/qutebrowser/issues/925

******************************
Contributions and maintainance
******************************

Contributions to qutebrowser are still on their all-time high!

In the past seven days, 20 pull requests got merged (and 6 new ones are still
open), and there have been dozens - if not hundreds - of comments for issues and
PRs. This is awesome, but of course also takes a bit of time ;)

I also helped `tracking down`_ a bug in pytest 3.0 (not released yet) affecting
the qutebrowser testsuite. So far, nobody `seems to know`_ what's going on there
exactly...

Other than that, a lot of other small things happened and a few bugs got fixed -
too many to list them all here!

.. _tracking down: https://github.com/pytest-dev/pytest/issues/1794#issuecomment-239084479
.. _seems to know: https://mail.python.org/pipermail/pytest-dev/2016-August/003775.html
