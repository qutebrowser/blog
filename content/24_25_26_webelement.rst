#########################################
Day 24-26: Refactoring the WebElement API
#########################################

:category: webengine

Last Thursday I finished the WebElement API refactoring to the point where the
QtWebKit code and all related tests work normally again, and I merged the
branch.

On Friday, I did some work because of a major pytest-qt release (2.0) and fixed
some other small issues. After that, I wanted to start experimenting with some
javascript to hopefully get hints working with QtWebEngine.

However I noticed having a web inspector makes writing JS much easier, so I
wanted to work on that first. Then I realized there's still no setting support
for QtWebEngine yet, so that's what I decided to actually `start working on`_.

Today was a `public holiday`_ so I took it a bit easier and mainly merged some
(7!) pull requests, and fixed some easy bugs (`1`_, `2`_, `3`_, `4`_). I also
looked at some new crash reports, and `updated`_ my patched PyQt package.

.. _start working on: https://github.com/The-Compiler/qutebrowser/commit/066c9bf4dcf179d38a6997512386c6a0a38caef2
.. _public holiday: https://en.wikipedia.org/wiki/Swiss_National_Day
.. _1: https://github.com/The-Compiler/qutebrowser/commit/5ec39b7540c4e9e15012c866cf4946f7a042f05c
.. _2: https://github.com/The-Compiler/qutebrowser/commit/81d0d647319bbff1ac6c079f871afacae97c6760
.. _3: https://github.com/The-Compiler/qutebrowser/commit/49699be44e9d9b88a8550dc9e914fb9ecce30c13
.. _4: https://github.com/The-Compiler/qutebrowser/commit/ef439bb916e04989cc13776a8c3b5f246cebebc1
.. _updated: https://github.com/The-Compiler/qt-debug-pkgbuild/commit/9950622c6d0cab536f351b57e800891e8ad27e41
