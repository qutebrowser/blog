####################
Day 7: Fixing things
####################

:category: webengine
:tags: pyplanet

******************
Handling callbacks
******************

I did a small experiment today, trying to make it easier to use QtWebEngine
functions which expect a callback, like ``QWebEnginePage::runJavaScript``.

Normally, you'd call such a function like this:

.. code-block:: python

   def calc(view):
       def cb(data):
           print("data: {}".format(data))
       view.page().runJavaScript('1 + 1', cb)

What I wanted is to (ab)use Python's ``yield`` statement instead (as a
`coroutine`_), so I can yield a callback to call, and the rest of the function
would run after it:

.. _coroutine: https://www.python.org/dev/peps/pep-0342/

.. code-block:: python

   @wrap_cb
   def calc(view):
       data = yield view.page().runJavaScript, '1 + 1'
       print("data: {}".format(data))

This worked fine, and the ``wrap_cb`` decorator looks like this:

.. code-block:: python

   def wrap_cb(func):

       @functools.wraps(func)
       def inner(*args):
           gen = func(*args)
           arg = next(gen)

           def _send(*args):
               try:
                   gen.send(*args)
               except StopIteration:
                   pass

           if callable(arg):
               cb_func = arg
               args = []
           else:
               cb_func, *args = arg
           cb_func(*args, _send)

       return inner

In the end I ended up not using it though, because it felt like too much magic.

Definitely was an interesting experiment, and I'm a step closer wrapping my head
around how coroutines work.

******************
QtWebEngine branch
******************

Yesterday, I `branched off`_ a ``qtwebengine`` branch, and started refactoring
everything so there would be a clearly defined interface which hides the
implementation details of a single tab in qutebrowser (``QWebView`` or
``QWebEngineView``).

This means even the current QtWebKit backend broke, which is why the work is
still in a branch. I got both QtWebKit and QtWebEngine to run enough to show you
a nice `screenshot`_, but as soon as you do anything except opening an URL (like
scrolling, or going back/forward) qutebrowser crashed.

Today I worked on getting everything running with QtWebKit first again, and expanding the
`API of a tab`_. Here's what's working so far:

- Scrolling
- Going back/forward
- ``:debug-dump-page`` (needed for tests)
- ``:jseval`` (needed for tests)
- Caret browsing

Everything apart from that is either broken or untested - but it's a start!

Seeing the first tests pass definitely was a satisfying feeling :)

.. _branched off: {filename}/06_Branching_off.rst
.. _screenshot: /images/day_6.png
.. _API of a tab: https://github.com/The-Compiler/qutebrowser/blob/qtwebengine/qutebrowser/browser/tab.py
