########################################
Day 21-23: After Europython and releases
########################################

:category: webengine

This week I came back from `EuroPython`_ (which was awesome!), so on Monday I
was busy with responding to issues, reading crash reports and reviewing PRs
which accumulated during my "holiday".

Yesterday I `released`_ qutebrowser v0.8.0, as I had to get a new release out
ASAP because of breaking changes in Qt 5.7, and enough changes for a new real
release (rather than a simple patch release) accumulated.

I then noticed the OS X ``.app`` release was broken, due to a packaging issues.
I `fixed`_ the build script, added a `smoke test`_ to notice such issues in the
future, and uploaded a new package.

Today, a total of four crash reports for the same `issue`_ came in (even
though nobody reported it before the release), where qutebrowser crashed when
simply doing ``:<enter>`` due to a change how aliases are handled.

So I decided to `fix`_ that and do an immediate v0.8.1 `release`_, since it's
likely that more people would run into this.

After the release, I started `refactoring`_ the web element API which used by
hints and some other features. Now (almost) everything is behind an unified
API. This is still kind of an experiment, as I'm not 100% sure yet if I can
implement a bridge from javascript to Python for QtWebEngine (so the existing
code can continue to use the same Python API it can with QtWebKit). We'll
hopefully see later this week.

.. _EuroPython: https://ep2016.europython.eu/en/
.. _released: {filename}/release_v0.7.0.rst
.. _issue: https://github.com/The-Compiler/qutebrowser/issues/1690
.. _fixed: https://github.com/The-Compiler/qutebrowser/commit/2795ae947817f494c58b49959346b48779bb077c
.. _smoke test: https://github.com/The-Compiler/qutebrowser/commit/fb20352e3fcfb88dbea8ae3a6121497fb73758d8
.. _fix: https://github.com/The-Compiler/qutebrowser/commit/9ff006746fb75de6fdff1aaa2329ccb7b29eb51c
.. _release: https://lists.schokokeks.org/pipermail/qutebrowser/2016-July/000235.html
.. _refactoring: https://github.com/The-Compiler/qutebrowser/compare/webelem
