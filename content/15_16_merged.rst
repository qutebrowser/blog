##################
Day 15/16: Merged!
##################

:category: webengine

On Friday and today (Monday) a dealt with a lot of little annoying issues, but
I finally got the ``qtwebengine`` branch with the initial refactoring merged!

After incoperating some great code review `feedback`_ I got on Thursday and
doing some other cleanups, I thought I was really close to merging the branch. 

Then I noticed some places inside qutebrowser still access the QWebView via
qutebrowser's object registry, and moved things around so the tab object (i.e.
the new abstraction API) is registered instead. So far, so good.

However, this suddenly made all tests using a fake ``tab`` object segfault on
PyQt versions older than 5.6 (i.e. all test environments except Archlinux).

It seems like it's somehow connected to the object registry using the
``QObject::destroyed`` signal to know when to remove an object from itself, but
when trying to do so, PyQt segfaults.

After trying to find out what's going on without any success, I just `skipped`_
those tests on older PyQt versions for now so I could move on. This is clearly
not a good solution and I'll need to revisit this in the following days and
find the underlying cause...

But there's better news: Today I finally could merge the branch, and with the
newest ``master`` you can now launch qutebrowser with ``--backend webengine``
to try it out!

Be careful however - other than basic browsing, some scrolling and zooming not
much is working yet:

.. image:: images/errorpage_small.png
   :alt: Chromium error page in qutebrowser
   :target: images/errorpage.png

After that worked, I mainly spent time getting QtWebKit specific code out of
qutebrowser's ``QWebView`` subclass - either `removing it entirely`_ because
it's a feature nobody uses hopefully, or moving it to the new tab API so it
works with QtWebEngine as well. This made things like page load status and
progress work.

I also made the end to end tests run with ``--backend webengine`` and only
about 300 of 500 fail ;)

I used QtWebEngine with qutebrowser for a bit, and started cursing mainly
because finding text, scrolling with ``gg`` and auto-insert-mode didn't work.
So probably those are the next things I'll get to run!

Another blogpost is planned for later or tomorrow morning, showing some photos
of how I sent all stickers out - stay tuned!

.. _feedback: https://github.com/The-Compiler/qutebrowser/pull/1629
.. _skipped: https://github.com/The-Compiler/qutebrowser/issues/1638
.. _removing it entirely: https://github.com/The-Compiler/qutebrowser/commit/e80475ed5724431188e76f1822be0bd81370b9eb
