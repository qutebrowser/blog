##########################
Day 9: A bit of everything
##########################

:category: webengine

I'm back from the pytest sprint, which unfortunately got interrupted by me
having to get my wisdom tooth out (which started to hurt shortly before the
sprint...).

I'm back on track, but yesterday and today was full with various little things
as aftermath of the sprint, and because I left qutebrowser alone for almost two
weeks.

Since I want to go to sleep soon, this blog post won't be as detailed as usual,
but a simple overview of work done at the sprint, yesterday, and (a lot of it!)
today.

As it involves various things only tangentially related to qutebrowser, I
didn't count yesterday as a qutebrowser crowdfunding day, but I counted today.
I think that's fair.

Unfortunately that means I didn't get to working on the ``qtwebengine`` branch
at all today, but it was definitely necessary to get all those little things
done and off my mind.

Stuff I worked on, roughly separated in categories:

************************
qutebrowser crowdfunding
************************

- Finalizing the sticker design (I'll follow up with a picture in a few days
  when they're here!)
- Ordering stickers
- Trying to figure out what's the best way to send out dozens of letters
  (parcels?) worldwide without going insane

***********
qutebrowser
***********

- Looking at ~20 crash reports and answering to 5 of them
- Reviewing/Merging a PR improving the dvorak bindings suggested in the
  completion for ``hints -> letters``
- Various (more or less painless) version updates in the testing/linting
  toolchain.
- Hiding a Qt warning appearing with Qt 5.7.0 (fixed in .1) when showing
  invalid images.
- Reviewing/Merging a PR which prefers the given count over an argument for
  ``:scroll-perc``, which means ``gg`` now can be used with a count.
- Trying to build Qt 5.6.1-1 for OS X (as Homebrew refuses to install binary
  packages for older versions once a newer one is released, which failed the
  build...), which for some reason didn't work even though it contains
  QtWebKit. I ended up disabling automated tests on OS X until QtWebEngine is
  ready or someone steps up to take care of it.
- Reviewing/Merging a PR allowing to set an alias mapped to multiple commands.
- Updating to the new ``pytest-bdd`` release and starting to use its new tag
  customization hook to make tags in qutebrowser's ``.feature`` files simpler.
  This was troublesome for frozen tests (freezing: compiling a script to an
  executable) on Windows as the hook needed ``pytest-bdd`` to be installed, but
  as soon as that was installed the tests would fail when frozen. I ended up
  only defining the hooks when not frozen.
- Adding documentation and a default keybinding for ``:hint inputs``
- Fix for ``:jump-mark`` (``'x``) crashing with an invalid URL
- Reviewing a PR adding a ``:repeat-command`` command (``.``)
- Reviewing a PR adding a ``$QUTE_CONFIG`` variable for userscripts
- Reviewing a PR potentially fixing an issue with configs being corrupted when
  a disk runs full
- Reviewing a PR improving ``:edit-url``
- Reviewing a PR adding tests for completion models
- Reviewing a PR scaling the column widths in the completion more intelligently
- Testing the 3.0 beta of flake8 to avoid bad surprises when it's released, and
  tracking down/reporting bugs against flake8 and various plugins qutebrowser
  uses.
- Trying to track down qutebrowser hanging for me when I open PDFs since
  recently (due to an evince/GTK bug?)
- Triaging various issues and answering questions, as always

******
pytest
******

I'm one of the maintainers of pytest, and since I'm taking care of
shirts/stickers for qutebrowser already, I'll also do that part for the pytest
sprint (which also had a crowdfunding).

- Getting addresses for t-shirts for people at the sprint
- Doing a survey for people getting t-shirts as part of the crowdfunding
- Designing stickers (with ``@kvas-it``)
- Designing t-shirts (with ``@kvas-it``)
- Ordering stickers
- Various long discussions about pytest 3.0

**********
pytest-bdd
**********

- Adding a hook to customize how ``@tags`` in ``.feature`` files are converted
  to pytest markers, which made using tags for qutebrowser much simpler (with
  ``@olegpidsadnyi``)
- Allowing spaces in tags
- Fixing a test with older pytest versions
- Releasing v2.17.0

*********
pytest-qt
*********

- Picking up a ``modeltest`` branch I started almost a year ago to test Qt
  models (e.g. for qutebrowser's completion models), updating it, adding tests,
  and getting it merged.
- Changing various defaults for an upcoming major release (with ``@nicoddemus``)
- Reviewing/Merging a PR adding a method to wait async for a predicate.
- Reviewing a PR making it easier to configure which Qt backend should be used.
