########################################
Paving the road towards qutebrowser v2.0
########################################

:category: other
:tags: pyplanet, qtplanet

Today, it's been exactly 6 months since I launched the
`GitHub Sponsors campaign`_ - time flies!

I wanted to use this opportunity to update everyone on what has been going on,
on my plans for qutebrowser's future, and on various other bits and bytes - I
have a lot of things I want to write down in my head, so this might get rather
long. Grab some beverage of your choice, and feel free to skip over sections
which don't seem relevant for you!

In case you're reading this via the Python or Qt Planet and need some context:
`qutebrowser`_ is a web browser with vim-like keybindings, based on Python and Qt.

.. _qutebrowser: https://www.qutebrowser.org

******************
Founding a company
******************

(Note that the donation amounts mentioned here are rounded figures. Thus, they
should still be roughly accurate if you substitute USD by CHF or EUR.)

After starting the crowdfunding, I had no idea what to expect. If I had to
guess, I'd probably have expected a couple hundred USD per month. I'm happy to
report that I'm getting an average of around 1000 USD in donations since
November.

I'm very happy to receive so many donations - this is `quite extraordinary`_ for
a somewhat niche open source project, and I'm grateful to have an awesome
community around qutebrowser! However, getting regular donations also meant a
lot of additional "bureaucracy" work. I had to fill out US tax-exemption forms
(W8-BEN) for GitHub, and I had to found my own small company to take care of
things like taxation or social security contributions for the income.

Founding a small freelancing company is something I wanted to do anyways: I did
some small freelancing gigs during my studies, and that's something I wanted to
continue building upon.

.. image:: /images/bruhinsw.png
   :alt: Bruhin Software Logo
   :target: https://bruhin.software/

Thus, `Bruhin Software`_ was born. In case you're wondering: The bear paw is
based on the family `coat of arms`_ for my last name "Bruhin", which needed to
be part of the company name due to Swiss laws for sole proprietorship companies.

Getting everything set up took some time: To combat employments by
a single company disguised as self-employment, you typically have to start
working as a company and prove that you have at least three different customers,
as well as things like a logo or business cards.

Thankfully, I already had some ideas lined up during my studies, so I could do
various gigs in late 2019 and early 2020:

- I was in Berlin in November - besides `speaking at`_ the Qt World Summit and
  finally meeting the people behind Qt at the Qt Contributors Summit, I also
  gave a training about advanced Python and pytest at a company.
- Around January/February/March, I updated a `website`_ run by an
  `Open Source student association`_ (both links in German). That website is a
  platform for students to upload cheatsheets and other documents. I modernized
  it from an outdated tech stack (Django 1.8 which was supported until April
  2018, Python 2, server with `2000 days`_ uptime and broken RAID) to something
  current and maintainable again.
- In February, I was in Dresden (Germany) for another Python/pytest training.
- I gave a training on pytest basics in London in March.
- In April, I gave a remote training on writing GUIs using `Qt for Python`_
  (PySide2).

.. image:: /images/qtws.png
   :alt: Me speaking at Qt World Summit
   :target: https://www.youtube.com/watch?v=zdsBS5BXGqQ

I don't intend this to get something too big - and I'm not financially dependent
on either donations or freelancing work, as I'm still employed 40% by an
university. Still: If you're interested in trainings or consulting around Python
(especially the language itself, testing with pytest, or writing GUIs with PyQt5
or PySide2): Please reach out to `florian@bruhin.software`_!

Back to bureaucracy: After failing to figure out how to best handle the
rather unique situation around donations and such, I reached out to a `tax
professional`_ (website in German) in February. That was a great idea: I'm happy
to report that yesterday, I finally got the official confirmation that I'm
(part-time) self-employed.

In the meantime, I also took care of some other things, like making sure my
accounting (something I had ignored so far) was up-to-date. Again, I intend to
get some professional help where needed, but I think it's good to have some
overview over things personally as well.

Long story short: Setting things up was a rather long but exciting journey. With
that out of the way, I can now get back to doing more for qutebrowser again.

Doing some other work for a while definitely was a good variation, though it can
be difficult to juggle three responsibilities (employment at the university,
freelancing, qutebrowser) at times.

.. _Open Source student association: https://www.openhsr.ch/
.. _quite extraordinary: https://reference.kemitchell.com/top-donations-developers.html
.. _GitHub Sponsors campaign: https://github.com/sponsors/The-Compiler
.. _Bruhin Software: https://bruhin.software/
.. _speaking at: https://www.youtube.com/watch?v=zdsBS5BXGqQ
.. _website: https://studentenportal.ch/
.. _Qt for Python: https://wiki.qt.io/Qt_for_Python
.. _2000 days: https://twitter.com/the_compiler/status/1239831837272309760
.. _florian@bruhin.software: <mailto:florian@bruhin.software>
.. _tax professional: https://www.stt.ch/
.. _coat of arms: https://www.chgh.ch/1800-b/bracher-brysacher/bruhin.html

****************
Funding campaign
****************

Back to the GitHub Sponsors funding: Originally, I wanted to order shirts,
stickers and swag in May. This won't be happening for now, as I don't trust
postal services in various countries to be reliable at the moment (and even if
they are: they are overloaded enough right now).

Thus, the shipping date for those physical rewards is currently postponed
indefinitely. I'll send out updates via GitHub Sponsors as soon as there's some
news on that front.

.. image:: /images/shirts.jpg
   :alt: A qutebrowser shirt

Thanks to all your generous donations, I reached GitHub's $5000 matching cap
around March. GitHub Sponsors still remains an excellent platform for collecting
funding, as they have no fees, not even for currency conversions. I still have
some ideas for alternative funding options via Stripe, but that's not a priority
for me right now.

From time to time, people ask me how much money I'm still missing in donations.
I struggle to find an answer for that question: Working on qutebrowser isn't
primarily about money, otherwise I wouldn't still be doing it after 6.5 years.
Even if you ignore the "historical" work and pick the lowest rate I'm willing to
work for as a freelancer (50 USD/h which I've billed for some open-source work
before, for non-commercial projects I really like): The 1000 USD would lead to
around 20h of work per month. I think it's safe to say that I'm doing more than
that on average, especially if you consider community reach-out, which is still
something I find very important. As an example: Just today, I replied to one
private mail related to qutebrowser, answered to a new issue, three mailinglist
mails, a couple of Reddit posts, and some questions in IRC. I like hearing from
all the people using qutebrowser (and helping them), though!

With the bureaucracy out of the way and no planned freelancing gigs right now,
at this point I can commit to doing a bit more work on qutebrowser. To start
with, I plan to work on qutebrowser exclusively for a day per week (in addition
to the small day-to-day things). It's possible I'll be able to ramp
that up soon - for the next 4-5 weeks, there's still a lot to finish for
university lectures.

Around June/July/August, I might also able to devote some bigger blocks of time
to qutebrowser as there are no weekly university preparation deadlines - for
example, I could work for a week or two on qutebrowser only, and then on
university stuff for another week or two. I will need to experiment a bit to see
what works best.

Like probably a lot of people, I'm currently stuck working from my home-office,
which is my 11m² bedroom. Productivity-wise, that probably isn't optimal, but
we'll see how things go. So far, I seem to manage quite well, though I'm looking
forward to going to the office for university work again some time in the
(hopefully not too distant) future.

********************
Pull request backlog
********************

My immediate focus for qutebrowser - and something I know various people are
waiting for - is still the backlog of contributions, some dating back to
December 2017. This is still something I struggle with, as reviewing code takes
a lot of time and focus (perhaps more than writing code myself) and for a long
time, I felt overwhelmed by the backlog.

Still, two years later, I feel like I'm finally getting a grasp on the issue,
and I feel confident that I can clear things up this time around. The thing which
ended up helping me a lot is creating a GitHub `project board`_ where I'm
organizing pull requests into various categories, depending on (what I think is)
their current state.

.. image:: /images/prbacklog.png
   :alt: Part of the pull request backlog board
   :target: https://github.com/qutebrowser/qutebrowser/projects/4

This helped me tremendously and resulted in 15 PRs being merged since I opened
the project board 16 days ago. I finally feel like I'm not missing the forest
for the trees anymore. I hope I'll be able to continue the trend of merging
around 1 PR per day on average (at least until I get to the more complex ones),
but there are is also another urgent change coming up - more on that in the next
section.

Thanks again to everyone for your patience. Around once a week or so, people ask
me what the current state of a given pull request is - usually with a different
pull request every time, since different people have different priorities. I
hope the project board will result in more transparency in that regard. Note,
however, that I likely won't be able to say more than that. If there aren't any
open comments on a pull request, I don't know what's missing to get it merged: I
haven't looked at that particular PR in detail yet.

For older PRs, often there are conflicts with the current master branch, or the
author might have moved on and is not interested in continuing to invest time
into get the PR merged. As a result, I usually request changes and give feedback
on recent PRs, but I will pick up and finish older PRs from where they are
currently.

.. _project board: https://github.com/qutebrowser/qutebrowser/projects/4

**************************
Session changes in Qt 5.15
**************************

Loading of sessions has always been a bit of a hack in qutebrowser (though a
hack other QtWebEngine browsers share as well; the original idea is coming from
`Otter Browser`_): Since QtWebEngine `doesn't provide`_ a way to load a tab's
back/forward history, qutebrowser `reconstructs`_ a binary data stream used by
Qt internally to save/restore history objects.

Unfortunately, that reverse-engineered binary stream `changed`_ in the
underlying Chromium version for Qt 5.15, causing it to load ``about:blank``
rather than the URLs from the session. When the session is saved again, this
causes the pages originally listed in it to be overwritten. With the change, a
complex "page state" blob is now required to load a tab's history, and this
isn't something we can reconstruct from the data available in session files.

As a stop-gap measure, I `released`_ qutebrowser v1.11.0 this week, which works
around the issue by at least opening the current URL for each tab, and also
creates a backup of the session directory on the first start with Qt 5.15.

Solving the issue properly means adding support for a new history format, which
stores the binary "page state" data needed by Chromium when saving a session,
and restores the data when loading the session.

At the same time, some other session format changes are planned as well:
Sessions will be saved as a JSON file (rather than YAML), stored inside a zip
file together with the required binary data. After some discussion, this was
deemed the best solution to store the needed data efficiently, while still
keeping session data readable by humans and scripts alike.

.. _Otter Browser: https://otter-browser.org/
.. _doesn't provide: https://bugreports.qt.io/browse/QTBUG-60112
.. _reconstructs: https://github.com/qutebrowser/qutebrowser/blob/v1.11.0/qutebrowser/browser/webengine/tabhistory.py
.. _changed: https://github.com/qutebrowser/qutebrowser/issues/5359
.. _released: https://lists.schokokeks.org/pipermail/qutebrowser-announce/2020-April/000080.html

*********************
Other bits and pieces
*********************

Finally, there are other smaller changes I'd like to take a look at, for a
variety of reasons: A few are urgent or important for qutebrowser to continue
working, some are important to me personally, others are just a good fit
together with a PR I might be reviewing.

To make it more transparent what my current focus is, I opened another `roadmap
project board`_ on GitHub, where I'm collecting issues I'm currently focused on
or issues I'd like to tackle.

.. _roadmap project board: https://github.com/qutebrowser/qutebrowser/projects/5

********************************************
The road towards Qt 6 and qutebrowser v2.0.0
********************************************


After Qt 5.15 is released in around three weeks, the next release will be
`Qt 6`_ - a new major release of Qt with backwards-incompatible changes, something
that happens once all 7-8 years.

.. image:: /images/qt6.png
   :alt: Qt 6 Vision graphic
   :target: https://www.youtube.com/watch?v=YmwAeS_ojPA

An `initial timeline`_ was proposed this week, planning a Qt 6 release for
December 2020. Unfortunately, while Qt 4 and 5 were `supported in parallel`_ for
three years, this time around, non-commercial support for Qt 5 `will end`_ the
moment Qt 6 is released.

Therefore, qutebrowser's plan is to be ready for Qt 6 as
soon as possible after it's released (or, ideally, before that). At the same
time, qutebrowser will keep compatibility for Qt 5 for some time (multiple
months, possibly multiple years, depending on the maintenance cost and usage.
Right now it's too early to tell).

It's planned to use that opportunity to clean up various things for a
qutebrowser v2.0.0 release: There will be various dependency changes with
`Python 3.5 support dropped`_, `support for Qt < 5.11 dropped`_ and some
dependencies being added, swapped out or removed.

At the same time, there will be various other internal refactorings: I'd like to
get back to looking at `extension support`_ and related refactorings, and also
`start using`_ various automatic code-formatters such as `black`_ and `isort`_.
Those projects weren't around (or not used commonly) when qutebrowser was born,
but I think they would be a good addition to make everyone's lives easier when
working on qutebrowser - just like various Python 3.6+ only features, especially
`fstrings`_.

All that will cause a lot of code churn, so it will only happen after the
majority of the currently open pull requests are merged. I hope that timeline
will work out, and qutebrowser will be a more modern codebase by the end of the
year! See the v2.0.0 `milestone`_ on GitHub for all planned changes.

.. _Qt 6: https://www.youtube.com/watch?v=YmwAeS_ojPA&feature=youtu.be
.. _initial timeline: https://lists.qt-project.org/pipermail/development/2020-April/039382.html
.. _supported in parallel: https://www.qt.io/blog/2014/11/27/qt-4-8-x-support-to-be-extended-for-another-year
.. _will end: https://www.qt.io/blog/qt-offering-changes-2020
.. _Python 3.5 support dropped: https://github.com/qutebrowser/qutebrowser/issues/4800
.. _support for Qt < 5.11 dropped: https://github.com/qutebrowser/qutebrowser/issues/3839
.. _extension support: https://github.com/qutebrowser/qutebrowser/issues/30
.. _start using: https://github.com/qutebrowser/qutebrowser/issues/1455
.. _black: https://black.readthedocs.io/en/stable/
.. _isort: https://github.com/timothycrosley/isort
.. _fstrings: https://realpython.com/python-f-strings/
.. _milestone: https://github.com/qutebrowser/qutebrowser/milestone/42

*****************************************
Qt Company and the KDE free Qt foundation
*****************************************

.. image:: /images/kdeqt.png
   :alt: Konqi with Qt inside
   :target: https://community.kde.org/Konqi

Finally, there was a `concerning announcement`_ by the `KDE Free Qt Foundation`_
before Easter. In the announcement, they claim that:

    [...] [The Qt Company] suddenly informed both the KDE e.V. board and the 
    KDE Free QT Foundation that the economic outlook caused by the Corona virus 
    puts more pressure on them to increase short-term revenue. As a result, they 
    are thinking about restricting ALL Qt releases to paid license holders for the 
    first 12 months. They are aware that this would mean the end of contributions 
    via Open Governance in practice.

A day later, The Qt Company `published`_ a (very brief) announcement disputing
those claims:

   There have been discussions on various internet forums about the future of Qt
   open source in the last two days. The contents do not reflect the views or
   plans of The Qt Company.

   The Qt Company is proud to be committed to its customers, open source, and
   the Qt governance model.

I've asked both sides for clarification (`KDE`_, `Qt`_). This was three weeks
ago, and I haven't heard much more so far.

If this came true, there aren't many options for qutebrowser and me: Either add
support for a different backend (such as `Chromium Embedded Framework`_) which
means months of work on top of an already giant backlog; or throw the towel.
Having a browser backend with a year delay in security updates is unacceptable
to me, and due to Qt's commercial license terms, purchasing a commercial license
isn't a reaslistic option either.

Needless to say, this would be a very hard decision to take. For now, it looks
like The Qt Company just used this to bluff (probably to get some other
provision in their contract changed). That in itself is very concerning and
disheartening, but gives me hope that things can still continue as usual.

I will update everyone on this matter once (if) there's more to say - until
then, there isn't much more I can do.

.. _concerning announcement: https://mail.kde.org/pipermail/kde-community/2020q2/006098.html
.. _KDE Free Qt Foundation: https://kde.org/community/whatiskde/kdefreeqtfoundation.php
.. _published: https://www.qt.io/blog/qt-and-open-source
.. _KDE: https://mail.kde.org/pipermail/kde-community/2020q2/006121.html
.. _Qt: https://lists.qt-project.org/pipermail/interest/2020-April/034891.html
.. _Chromium Embedded Framework: https://en.wikipedia.org/wiki/Chromium_Embedded_Framework

***********
Wrapping up
***********

It's been four months since the last blog post in the `qutebrowser blog`_.
Judging from the length of this post, I probably should post things more often -
sorry about that, and thanks for reading until the end! I hope you are all
healthy and things are going okay, despite the current circumstances. If that's
not the case and you need someone to talk, please don't hesitate to
`reach out to me`_! Let's see what the future brings and deal with things as
they come up - both with qutebrowser and in general.

.. _qutebrowser blog: https://blog.qutebrowser.org/
.. _reach out to me: me@the-compiler.org
