################################
Days 39/40/41: Lots of features!
################################

:category: webengine

A new blogpost is overdue, as I worked on qutebrowser again for the past three
days! A lot of new features arrived, and this will hopefully make QtWebEngine
usable as a daily driver for some people!

**********
Adblocking
**********

Perhaps the most exciting news first: `adblocking`_ is now available with
QtWebEngine! The used Qt `API`_ is quite powerful, and hopefully will make it
possible to implement something like `uMatrix`_ for qutebrowser somewhen in the
coming months!

Right now, adblocking works the same as it did with QtWebKit, using the existing
host block lists.

While implementing it, I noticed an interesting issue: qutebrowser did freeze
and crash when there was an exception inside the request interceptor used to
block the request. This is probably due to it running in Chromium's IO
thread, which makes it impossible for us to display the usual crash report
window. Instead, I added the ``utils.prevent_exceptions`` `decorator`_ in order
to simply log exceptions happening there.

******************************
Opening windows via javascript
******************************

Some people already noticed how Qt ignored javascript trying to open a new
window (via ``window.open()``).

Support for that `is now implemented`_, however unfortunately I did run into a
`Qt bug`_ causing the qutebrowser javascript code not being loaded for windows
opened that way (or, according to that report, possibly crashing).

This will be fixed in Qt 5.6.2 and 5.7.1, however neither is released yet.
Their plan is to release Qt 5.6.2 in the `coming weeks`_ and then release
5.7.1 after that.

Those requests are currently silently `ignored`_ with older Qt versions. I tried
adding an error message when that happens, however it was also displayed when
opening a new link using middle-/ctrl-click, and I didn't find a way to tell the
two apart.

If you don't want to wait until the release and happen to be on Archlinux, you
can also use my `qt-debug packages`_ and set ``QUTE_QTBUG54419_PATCHED=1`` in
your environment. Note if you do that and don't have those fixed packages
installed, stuff will break and I'll probably ignore all related crash logs ;)

On other distributions, you'll need to rebuild QtWebEngine with `this patch`_.

***************
Session support
***************

Another feature many people missed was support for sessions, which is now
implemented! Unfortunately (like Qt 5.6's QtWebKit), QtWebEngine has no API to
manipulate the history of a tab programmatically, so qutebrowser instead creates
a `binary stream`_ in Qt's internal serialization format and then loads that.

This was definitely made much easier by an existing implementation in
`Otter Browser`_ (thanks!) and of course by QtWebEngine/Chromium being open
source.

Initially, when loading the history, qutebrowser just segfaulted. After some
debugging in Chromium's C++ code I figured out that was because I set the
current history index to 0 instead of -1 when there are no history entries.

With this fixed, everything seems to work fine so far! The only thing missing
(due to missing Qt API) is storing zoom level and scroll positions for earlier
pages in the history (i.e., everything except the currently viewed one).
However, I doubt many people will notice.

************************
Running without QtWebKit
************************

Since I wanted to get the OS X tests to run again (which lack QtWebKit due to it
being removed from the Homebrew package manager), I looked into getting
qutebrowser (and tests) to run without QtWebKit installed. After various small
changes to how things are imported, this is now the case.

************
Tests and CI
************

Until now, qutebrowser with QtWebEngine wasn't tested on CI. This now changed,
by adding a job for QtWebEngine with Archlinux.

With the session support added, I was also able to activate around 150 tests
which were disabled before. This uncovered some smaller bugs like invalid URLs
`being added`_ to the history sometimes (causing a warning to be printed), or
`cloning`_ the zoom level when cloning a tab not working properly. Some tests
(mainly for scrolling) also needed some `additional waiting`_ since scrolling
now happens async (via javascript) with QtWebEngine.

There also were various small improvements to the output when tests fail, for
cases I discovered thanks to those failing tests.

Unfortunately, a handful of tests are still flaky (failing sometimes), so I
added a ``@qtwebengine_flaky`` marker and `applied`_ it to all tests which fail
sometimes and I don't see an easy fix for yet.

********************
Other bits and bytes
********************

- qutebrowser now `knows`_ when the scroll position is at the very bottom, so
  ``:scroll-page`` with ``--bottom-navigate`` works.
- I tried making ``colors -> webpage.bg`` `work`_, but without any luck.
- The ``auto-insert-mode`` setting `now works`_.
- The ``:insert-text`` and ``:paste-primary`` commands were `implemented`_.
- ``webelem.classes`` got `implemented for QtWebEngine`_ which means the insert
  mode will now work correctly with things like the ACE editor (with a
  corresponding `test`_ added).
- Custom HTTP headers, including the ``do-not-track`` and ``accept-language``
  settings are now `available`_ with QtWebEngine
- Qt 5.6.0 or newer is now `enforced`_ when using ``--backend webengine``. This
  will probably stay the minimum version required for QtWebEngine support, I
  don't intend to add support for Qt 5.4 and 5.5.
- Various blocks of now-unneeded or dead code got removed:
    - `webkitelem.focus_elem <https://github.com/The-Compiler/qutebrowser/commit/78d64f47916f51c51893e15e3147620424a84f62>`_
    - `WebKitElement.run_js_async <https://github.com/The-Compiler/qutebrowser/commit/8f9cfcf2323c0c8dfa36fe716308a8fba0f96c48>`_
    - `WebKitElement.debug_text <https://github.com/The-Compiler/qutebrowser/commit/60c86a08c44efc39b4891e77c4b89cf4a3d99bad>`_
    - `WebKitElement.is_visible <https://github.com/The-Compiler/qutebrowser/commit/3e1583bb1cf353ff8793a59ed37cdc75e6966ef5>`_ (made private as it's only needed with QtWebKit)
    - `BrowserPage.shouldInterruptJavaScript <https://github.com/The-Compiler/qutebrowser/commit/8c3906b784df09257a0e87fa1470b9cc8e796561>`_ (broken due to `an old Qt bug <https://bugreports.qt.io/issues/?jql=text%20~%20%22shouldInterruptJavascript%22>`_ and not available with QtWebEngine)
    - `BrowserPage.chooseFile <https://github.com/The-Compiler/qutebrowser/commit/bac7a6eaf29418327b88b831113a75c55000c875>`_ (does the same as the default implementation, and file choosing also works out-of-the box with QtWebEngine!)
- And probably some other stuff I forgot - as you can see, a lot happened in
  those three days!

.. _API: https://doc.qt.io/qt-5/qwebengineurlrequestinfo.html
.. _uMatrix: https://addons.mozilla.org/en-us/firefox/addon/umatrix/
.. _adblocking: https://github.com/The-Compiler/qutebrowser/commit/02bd42cbed8a1faf606efdf107b010c2aba2d064
.. _is now implemented: https://github.com/The-Compiler/qutebrowser/commit/a4cd0291a687070e05736fbb8c312e59377cc2d3
.. _decorator: https://github.com/The-Compiler/qutebrowser/blob/v0.8.2/qutebrowser/utils/utils.py#L573-L626
.. _Qt bug: https://bugreports.qt.io/browse/QTBUG-54419
.. _coming weeks: http://lists.qt-project.org/pipermail/releasing/2016-August/004329.html
.. _ignored: https://github.com/The-Compiler/qutebrowser/commit/cf070d48f2de931bb4c00f37a1b8077ba69956a4
.. _qt-debug packages: https://github.com/The-Compiler/qutebrowser/blob/master/doc/stacktrace.asciidoc#archlinux
.. _this patch: https://codereview.qt-project.org/gitweb?p=qt/qtwebengine.git;a=patch;h=f5ee1feeed2abbcbe6db2bf9757d692b38fcbcb1
.. _binary stream: https://github.com/The-Compiler/qutebrowser/blob/master/qutebrowser/browser/webengine/tabhistory.py
.. _Otter Browser: https://otter-browser.org/
.. _being added: https://github.com/The-Compiler/qutebrowser/commit/f2c4cedf619f89045172ce2be57ea1c8416ecead
.. _cloning: https://github.com/The-Compiler/qutebrowser/commit/abdc604ead32b516fa69329101263bb2582ee003
.. _additional waiting: https://github.com/The-Compiler/qutebrowser/commit/85b3d08c6632462b292fea4a1ab5721550376d85
.. _applied: https://github.com/The-Compiler/qutebrowser/commit/08302c5a5fdc63e608c628b838a926d8c66e30dc
.. _knows: https://github.com/The-Compiler/qutebrowser/commit/919196714b0e4b5ac9dbb0d8d4e4f5f0a7543299
.. _work: https://github.com/The-Compiler/qutebrowser/commit/02df91e369f441160296ef9c6f38733c3d36b2d3
.. _now works: https://github.com/The-Compiler/qutebrowser/commit/ee5a97206902cd44776966538b8296b92f38c4fe
.. _implemented: https://github.com/The-Compiler/qutebrowser/commit/948fa033c7339d6648af2141e88283105ffbaa31
.. _implemented for QtWebEngine: https://github.com/The-Compiler/qutebrowser/commit/fca37abf55b1e8b1639c8a885eda99e48d48d28d
.. _test: https://github.com/The-Compiler/qutebrowser/commit/522049132b24354266478b1d496950bb46233d09
.. _available: https://github.com/The-Compiler/qutebrowser/commit/44d1056e5497064b21f7c40f04fa640d8f834ad3
.. _enforced: https://github.com/The-Compiler/qutebrowser/commit/4d91ccfea5c970797023ec2a496178151e90ccaa
