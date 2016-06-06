##############################################
Day 1: Merging pull requests, and a stupid bug
##############################################

:category: webengine

Today was my first day of working on QtWebEngine, and as mentioned in the
previous post I started with merging some pull requests before they diverge too
much because of all the planned refactoring.

In the morning I was in the train without an internet connection, so I worked
on adding a few missing tests:

- `Spawning external editor <https://github.com/The-Compiler/qutebrowser/commit/3cfb430cdfddb8c0298e091558a7d59cfa5d1521>`_
- Some `test pages <https://github.com/The-Compiler/qutebrowser/tree/master/tests/manual/hints>`_
  for manual inspection for hint rendering, as that's difficult to automate.
  For some of those I attemted to create minimal examples but failed, if you
  know your way around HTML/CSS your help would be appreciated! See `#1550 <https://github.com/The-Compiler/qutebrowser/issues/1550>`_.


I then `merged <https://github.com/The-Compiler/qutebrowser/commit/b1914d641437c80e2cc17ae8fd44edba58b5851c>`_
a pretty old pull request helping with hints positioning in some corner cases,
where those tests really helped.

After doing so I cleaned up the current `webelem <https://github.com/The-Compiler/qutebrowser/blob/master/qutebrowser/browser/webelem.py>`_
code a bit (which will also help when porting hints to QtWebEngine) and really
confused myself with zoom adjustments for hints.

When drawing hints, the coordinates need to be adjusted "negatively" for the
zoom level of the web view, so that the hint gets clicked with the correct
position.

When getting the element coordinates via javascript however (like the PR did if
possible), they are already adjusted accordingly. Since the code
**drawing** the hints needs the unadjusted position, the zoom level needs to be
adjusted in the other direction.

To top off the confusion, in the unit tests I'm not actually getting the
element position via javascript, so I had to adjust the coordinates a third
time so the fake ``getElementRects()`` method would act like in real-life.

After doing so, some tests failed with a strange error - the position of the
rectangles was adjusted, but the width and height was not:

.. code-block:: python

   assert QRect(5, 5, 4, 4) == QRect(10, 10, 4, 4)

After a lot of head-scratching, I found the culprit:

.. code-block:: python

   {
       "left": geometry.left() - scroll_x / zoom,
       "top": geometry.top() - scroll_y / zoom,
       "right": geometry.right() - scroll_x / zoom,
       "bottom": geometry.bottom() - scroll_y / zoom,
       "width": geometry.width() / zoom,
       "height": geometry.height() / zoom,
   }

This was fixed by adding the needed parentheses:

.. code-block:: python

   {
       "left": (geometry.left() - scroll_x) / zoom,
       "top": (geometry.top() - scroll_y) / zoom,
       "right": (geometry.right() - scroll_x) / zoom,
       "bottom": (geometry.bottom() - scroll_y) / zoom,
       "width": geometry.width() / zoom,
       "height": geometry.height() / zoom,
   }

In hindsight it's - as always - totally obvious, but it was a nightmare to
debug.

Since those tests (checking if zoom was accounted for properly) used a scroll
position of 0/0, this evaluated to ``geometry.left() - (0 / zoom)`` which is
``geometry.left()``. The width and height were correct because they didn't
subtract any scroll position...

But the frustration was worth it, hints are now drawn correctly in various
corner cases!

After that, I merged and closed some more pull requests:

- I `improved <https://github.com/The-Compiler/qutebrowser/commit/abfd789f9e310daff9f042fe432975ea082cd862>`_
  how zooming behaves with a too big count and thus superseded/closed `#1140 <https://github.com/The-Compiler/qutebrowser/pull/1140>`_.
- I picked out a `fix <https://github.com/The-Compiler/qutebrowser/commit/3e22f64a20a52004d1927829b9cc31f5d6b3dcde>`_
  for tab indicators disappearing when using ``:tab-move``, and then closed
  `#697 <https://github.com/The-Compiler/qutebrowser/pull/697>`_ (which was
  pretty much a year old...) because the other things are either already fixed
  in the meantime, or things I disagree with.
- I `added <https://github.com/The-Compiler/qutebrowser/commit/57a1847e3a1d18cfdf60c627e04cb66c88d29167>`_
  some missing bits and tests for `#1460 <https://github.com/The-Compiler/qutebrowser/pull/1460>`_
  which allows to use partial commands (like ``:bac``) if they're unique in the command bar.
- And some other bits and bytes like updating pinned test dependencies or
  removing a few lines unused code.

Now, only 10 pull requests are `still open <https://github.com/The-Compiler/qutebrowser/pulls>`_,
of which two are work-in-progress, and four are explicitly marked as postponed
until after QtWebEngine support.

I plan to merge the other 6 pull requests and release a v0.7 over the next
day(s), and then all is ready to start! \\o/
