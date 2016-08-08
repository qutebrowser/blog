########################
Days 29/30: Web elements
########################

:category: webengine

A lot of code got moved around last Thursday/Friday!

I `finished`_ working on the web inspector, which made dealing with javascript
a lot easier! I also `added`_ a new ``utils.javascript`` Python module for
various javascript-related utilities.

While working on the Python/Javascript bridge for web elements, I noticed the
functions I define actually "leak" to the page. For Qt 5.7 and newer, I fixed
this letting the javascript run in a `different world`_ which means it runs
isolated from the page's javascript, but can still access and manipulate it.
For Qt 5.6 (which I'd still like to support with QtWebEngine, due to Archlinux'
PyQt version), this change `broke`_ compatibility, so I fixed things up and
decided to `rename`_ my javascript functions to make conflicts unlikely.

I `changed`_ the ``tab.find_all_elements()`` method to be async (i.e. call a
callback rather than returning the found elements), which is the groundwork to
be able to implement it for QtWebEngine. I also wrote a small first
`proof-of-concept`_ of manipulating web elements from Python with QtWebEngine:

.. image:: /images/jsbridge_small.png
   :alt: Manipulating web elements
   :target: /images/jsbridge.png

It's about as ugly as it can get, but it demonstrates that getting elements
from Python (via Javascript) and then coloring them (via Javascript) works with
QtWebEngine, which is the first step towards supporting hints, ``:navigate``
and editing fields with an external editor.

While reading the hints code again, I realized how the ``HintManager`` class
has grown way too big, and cleaned things up: I `moved`_ all ``:navigate``
related code to its own ``qutebrowser.browser.navigate`` module, `split up`_
actions (like "click the link" or "download the link") to a separate class, and
moved the ``_resolve_url`` function to a `webelement method`_.

Since pytest 3.0 is going to be `released`_ soon, I also `wrote`_ a
``requirements.txt`` file installing all test dependencies from git/hg.
Unfortunately, I `found`_ some issues - at least this way I could report them
before 3.0 was released!

Apart from all that, there also was a big number of GitHub issues, pull
requests, and other little things - too many to mention them all here!

The plan for this week is to split up ``webelem`` into
generic/QtWebKit/QtWebEngine parts, get ``:navigate`` to work, and then
hopefully start looking at hints.

.. _finished: https://github.com/The-Compiler/qutebrowser/commit/764c23203386b10bd37271ffdd966244bf49071b
.. _added: https://github.com/The-Compiler/qutebrowser/commit/08b70f0f4cfb102f41b1105b1b06681d30362c59
.. _different world: https://github.com/The-Compiler/qutebrowser/commit/7b211e0b65b4be30347239fb0345a5df792b7f12
.. _broke: https://github.com/The-Compiler/qutebrowser/commit/94cf3fa4ff1f040329f177dbee30cd8204908fd9
.. _rename: https://github.com/The-Compiler/qutebrowser/commit/0169f3a24f32e35a7701ef9f83807dc9c1946aa0
.. _changed: https://github.com/The-Compiler/qutebrowser/commit/d8521f43eeb888c10de0e99df9e3b7a7c991e464 
.. _proof-of-concept: https://github.com/The-Compiler/qutebrowser/commit/2232e7474a39353006c33b9c7b80ae638865e599
.. _moved: https://github.com/The-Compiler/qutebrowser/commit/778ccad39f1962924a3755c67f82c54b9eee787b
.. _split up: https://github.com/The-Compiler/qutebrowser/commit/e2ae133757a6e95cbe1d5ed633289d0790ef4851
.. _webelement method: https://github.com/The-Compiler/qutebrowser/commit/7a65559cce3e3d168be0e5d22953b930efb39fa1
.. _released: https://mail.python.org/pipermail/pytest-dev/2016-August/003754.html
.. _found: https://mail.python.org/pipermail/pytest-dev/2016-August/003756.html
.. _wrote: https://github.com/The-Compiler/qutebrowser/blob/master/misc/requirements/requirements-tests-git.txt
