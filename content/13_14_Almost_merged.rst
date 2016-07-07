#########################
Day 13/14: Almost merged!
#########################

:category: webengine

The past two days I was busy with getting stickers shipped out to everyone most
of the time - I'll post a dedicated blogpost about that tomorrow with some
pictures!

I still got some work in the ``qtwebengine`` branch done:

- Lots and lots of cleanups and small fixes
- Marked failing session tests as "expected to fail" for now as sessions will
  get a refactoring before they're supported in QtWebEngine anyways.
- Got scrolling with ``--backend webengine`` to work
- Fixed mouse wheel zooming
- Rebased and cleaned up commits
- Opened a `PR`_ for it to solicit some feedback from other contributors. I
  plan to merge it tomorrow.

And some other maintainance work:

- Merged a PR exposing a ``$QUTE_CONFIG_DIR`` (and ``DATA`` / ``DOWNLOADS``) to
  userscripts
- Merged a PR with new unit tests for completions
- Merged a PR making the statusbar position configurable (top/bottom)
- Merged a PR adding a simple issue template for GitHub
- `Fixed`_ an issue where eslint (javascript linting) started to fail due to a
  too old node version being installed on Travis (which caused all builds to
  fail)
- `Improved`_ the version output to make it cleaner and provide some more
  informations (like if QtWebEngine is installed)
- The usual CI version updates

.. _PR: https://github.com/The-Compiler/qutebrowser/pull/1629
.. _Fixed: https://github.com/The-Compiler/qutebrowser/commit/89cdef851d8f56b509dc04331330dd14f8ec62a1
.. _Improved: https://github.com/The-Compiler/qutebrowser/compare/a58c3ff0c639ae3b4d1b92713981a76586cc693c...29ee605c790a134b2aaf7bffa4bd1868b8be7213
