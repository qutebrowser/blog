######################
Day 12: Tests running!
######################

:category: webengine

Today I got all end-to-end tests for the ``qtwebengine`` branch (still with the
QtWebKit backend!) to work:

.. code-block:: raw

   671 passed, 9 skipped, 8 xfailed

This means almost all qutebrowser code is now refactored to use a well-defined
API over QtWebKit!

There are still some places (hints/downloads/editor) where I'm cheating and
still accessing the underlying ``QWebView`` object directly. I plan to look at
those once I have some more experience with QtWebEngine, as I currently don't
know how the API for those should look like.

Probably the most difficult thing today was `rewriting`_ userscript code to
work with the new way how dumping a page's content will work with QtWebEngine
(async, by calling a callback when the data is ready instead of returning it).

.. _rewriting: https://github.com/The-Compiler/qutebrowser/commit/86acf3b973c85380317c543d35fd9219d5df32ef

There's still some work to do, but we're getting closer to me working in the
``master`` branch again and having finished the first big refactoring phase.

The changes in the ``qtwebengine`` branch are quite big already:

.. code-block:: raw

   35 files changed, 2085 insertions(+), 867 deletions(-)

The plan for the rest of the week looks like this:

- Clean up linter warnings
- Get the unit tests for session saving/loading to work again as they're still
  broken thanks to some heavy mocking
- Add stub implementations for still missing QtWebEngine features so they log a
  warning and do nothing instead of crash.
- Implement the most needed features (like scrolling)
- Merge ``qtwebengine`` into ``master``

At that point, people using the git version will be able to use
``--backend webengine`` to play around with QtWebEngine support which will then
gradually get better and better.
