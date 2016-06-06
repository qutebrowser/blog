##################
About and Timeline
##################

:tags: pyplanet, qtplanet, pytest
:category: webengine

************
Introduction
************

A bit over two months ago, I started a `crowdfunding campaign`_ for
`qutebrowser`_, with the goal of working full-time on adding `QtWebEngine`_
support to it, which will bring more stability, security and features.

I asked for 3000€ to fund a month of full-time work before starting my studies
in September. The campaign took off more than I'd have ever imagined and was
almost funded in the first 24h.

At the end of the campaign, I got two months of full-time work funded. I'm now
close to starting those awesome two months and set up this blog as a work log
for what I'm doing, inspired by the one of `git annex assistant`_.

I also submitted this blog to `planet python`_,  `planet pytest`_ and
`planet Qt`_ - if you're reading this via one of those, fear not: I have
dedicated tags for them, and only will tag posts which actually seem relevant,
so you won't see daily posts there.

.. _crowdfunding campaign: http://igg.me/at/qutebrowser
.. _qutebrowser: http://www.qutebrowser.org/
.. _QtWebEngine: http://doc.qt.io/qt-5/qtwebengine-index.html
.. _git annex assistant: http://git-annex.branchable.com/devblog/
.. _planet python: http://planetpython.org/
.. _planet pytest: http://planet.pytest.org/
.. _planet Qt: http://planet.qt.io/

********
Timeline
********

My full-time work is planned to start *tomorrow*. I have some other obligations
until September, so there will be some days in between where I won't be working
on qutebrowser, but other things related to either Python or my studies.

This is the tenative schedule:

- June 6th - 10th: **qutebrowser (days 1-5)**
- June 13th - 15th: **qutebrowser (days 6-8)**
- June 16th - 29th I'll be in `Freiburg`_ for the development `sprint`_ on
  `pytest`_ (which qutebrowser is using too), and giving a 3-day `training`_
  for it.
- June 30th - July 1st: **qutebrowser (days 9-10)**
- July 4th - 8th: **qutebrowser (days 11-15)**
- July 11th - 15th: **qutebrowser (days 16-20)**
- July 17th - 24th I'll be in `Bilbao`_ at `EuroPython`_ giving
  `another training`_ about pytest and hopefully learning a lot in all the
  awesome talks.
- July 25th - 29th: **qutebrowser (days 21-25)**
- August 1st - 5th: **qutebrowser (days 26-30)**
- August 8th - 11th: **qutebrowser (days 31-34)**
- August 12th I'll be travelling to `Cologne`_ for `Evoke`_, a `demoparty`_ I'm
  visiting every year (let me point out this has nothing to do with political
  demos, go check the wikipedia article :P).
- August 15th - 19th: **qutebrowser (days 35-39)**
- August 22th - September 2nd I'll be busy with a math preparation course of
  the university I'll be going to.
- September 5th - 9th: **qutebrowser (day 40 and some buffer)**

.. _Freiburg: https://en.wikipedia.org/wiki/Freiburg_im_Breisgau
.. _sprint: http://pytest.org/latest/announce/sprint2016.html
.. _pytest: http://www.pytest.org/
.. _training: http://www.python-academy.com/courses/specialtopics/python_course_testing.html
.. _europython: http://europython.eu/
.. _another training: https://ep2016.europython.eu/conference/talks/pytest-simple-rapid-and-fun-testing-with-python-1
.. _Bilbao: https://en.wikipedia.org/wiki/Bilbao
.. _Cologne: https://en.wikipedia.org/wiki/Cologne
.. _Evoke: http://www.evoke.eu/
.. _demoparty: https://en.wikipedia.org/wiki/Demoparty

*****
Plans
*****

The work required to get QtWebEngine to run can roughly be divided into four
steps:

- **Preparation:** Writing end-to-end tests for all important features, merging
  some `pull requests`_ which are still open, doing a last release without any
  QtWebEngine support at all, and organizing/shipping t-shirts/stickers for the
  crowdfunding. A lot of this already happened over the past few months, but I
  still expect this to take the first few days.
- **Refactoring:** Since I plan to keep QtWebKit support for now, I'll refactor
  the current code so there's a clear abstraction layer over all
  backend-specific code. This will also make it easier to add support for a new
  backend (say, `Servo`_) in the future. Since this will probably break a lot
  in the initial phase, this work will happen in a separate branch. As soon as
  the current QtWebKit backend works fine again, that'll be merged and
  QtWebEngine support will be in the main branch behind a `feature switch`_.
- **Basic browsing**: The next step is to get basic browsing with
  ``--backend webengine`` working. This means you'll already be able to surf,
  but things like adblocking, settings, automatic insert mode, downloads or
  hints will show an error or simply not work yet.
- **Everything else**: All current features which are implementable with
  QtWebEngine will work, others will be clearly disabled (a few obscure
  settings might be missing with ``--backend webengine`` for example). See the
  respective `issue`_ for a breakdown of features which will probably require
  some extra work.

.. _pull requests: https://github.com/The-Compiler/qutebrowser/pulls
.. _Servo: https://servo.org/
.. _feature switch: https://en.wikipedia.org/wiki/Feature_toggle
.. _issue: https://github.com/The-Compiler/qutebrowser/issues/666

**************************
Frequently asked questions
**************************

**When will I be able to use QtWebEngine?**:

This depends on what features you need, and how fast I'll get them to work. 
Estimating how long the steps outlined above will take is quite difficult, but I
hope you'll have something to try after the first week or so.

Also note you'll need to have a quite recent Qt (5.6, maybe even 5.7 which
isn't released yet) at least at the beginning, because QtWebEngine is missing
some important features in older versions.

**Is QtWebEngine ready?**:

It certainly wasn't when it was first released with Qt 5.4 in December 2014.

That's also why I spent a lot of time writing tests for existing features
instead of trying to start working on QtWebEngine support.

Nowadays with Qt 5.5/5.6/5.7 things certainly look better, and I believe I'll
be able to implement all important features, however I'll need to rewrite some
code in Javascript as there's no C++ (and thus no Python API) for all the
functionality QtWebKit had.

Long story short: It's by no means a drop-in replacement (like initially
claimed by Qt) - but most users won't notice any missing functionality which I
can't implement at all with a recent enough QtWebEngine, and things are getting
better and better.

**How is this blog made?**:

Using `spacemacs`_, writing `ReStructuredText`_, storing it in a `git`_ repo,
processing it with `Pelican`_, the `Monospace theme`_ and the `thumbnailer`_
plugin.

Definitely a better workflow than Wordpress ;)

.. _spacemacs:  http://spacemacs.org/
.. _ReStructuredText: https://en.wikipedia.org/wiki/ReStructuredText
.. _git: https://git-scm.com/
.. _Pelican: http://blog.getpelican.com/
.. _Monospace theme: https://github.com/getpelican/pelican-themes/tree/master/monospace/
.. _thumbnailer: https://github.com/getpelican/pelican-plugins/tree/master/thumbnailer
