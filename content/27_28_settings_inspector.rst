######################################
Days 27/28: Settings and web inspector
######################################

:category: webengine

As mentioned in the last post, I wanted to look at settings and having a web
inspector before continuing to write javascript for web elements.

Yesterday, just as I was getting started with splitting up settings, I noticed
a bad `bug`_ in how the ``private-browsing`` setting was handled. Due to that,
local storage was enabled even when private browsing was turned on, until the
browser was restarted once after setting the setting.

After `fixing`_ it, I `released`_ v0.8.2 with that fix (and some others) on the
same day. I also `improved`_ the release automation so the ``build_release.py``
script automatically uploads release artifacts to GitHub. This should
significantly cut down the time I spend on doing future releases.

Today I got most settings `to work`_ with QtWebEngine, and marked the rest as
QtWebKit-only in the documentation.

After that was done, I `started`_ implementing support for having a web
inspector with QtWebEngine. Qt's support for that is currently quite spartanic,
so qutebrowser has to set the ``QTWEBENGINE_REMOTE_DEBUGGING`` environment
variable early enough (which means setting ``developer-extras`` requires a
restart) and then display that port on localhost with a second
``QWebEngineView``.

This worked just fine in a minimal example, but didn't in qutebrowser:

.. image:: /images/inspector_broken_small.png
   :alt: broken web inspector
   :target: /images/inspector_broken.png

After digging into it for a while, I found out that simply accessing
``QWebEngineSettings.globalSettings()`` caused something in QtWebEngine which
made it read the environment variable - I `rewrote`_ the code to not
immediately call ``globalSettings`` and the inspector started to work:

.. image:: /images/inspector_small.png
   :alt: web inspector
   :target: /images/inspector.png

There are still some rough edges, but tomorrow I should be able to improve the
inspector and start working on the required javascript code.

.. _bug: https://github.com/The-Compiler/qutebrowser/issues/1742
.. _fixing: https://github.com/The-Compiler/qutebrowser/commit/f73f3a2001c20f55640a67b1c31ed16a19d8a326
.. _released: https://lists.schokokeks.org/pipermail/qutebrowser/2016-August/000238.html
.. _improved: https://github.com/The-Compiler/qutebrowser/commit/195b17c1ad2b25a0924d9f5e6e99e5d248695162
.. _to work: https://github.com/The-Compiler/qutebrowser/commit/cae7eead6f305c9a91f397b8ee2b5bb0c333810d
.. _started: https://github.com/The-Compiler/qutebrowser/commit/614893bdd6f338f1727b04a8f0a604d197a19046
.. _rewrote: https://github.com/The-Compiler/qutebrowser/commit/61e0c8327a6329b3de49018679aa305442df1e82
