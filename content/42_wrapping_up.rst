#####################################
Wrapping up and looking at the future
#####################################

:category: webengine

************
Looking back
************

As you might have noticed, it's gotten a bit more quiet here again. The reason
for that is that, unfortunately, the 40 crowd-funded days are over (plus a few
extra days), and today I'm starting to study computer science at the
`University of applied sciences in Rapperswil`_ (with a beautiful campus next
to the lake).

As probably `usual in software development`_, things took a bit longer than
planned - I originally thought I'd have the second month for things other than
QtWebEngine, and it didn't turn out that way. I think my guesstimates for
everything related to QtWebEngine were roughly accurate, but there was a lot of
other work (organizing crowdfunding stuff, taking care of contributions and
issues, and the occasional important bugfix/release) which took more time than
I imagined.

Still I'm happy with the progress made in these two months. A few features are
still `missing`_, but I know about multiple people (myself included) using the
QtWebEngine backend as a daily driver and not really missing much.

What's more important is that the big things are out of the way - the last
feature I expect to take a longer time to implement are downloads, everything
else is something I can also implement whenever I have an hour or two to spare
some evening.

A lot changed in those two months! From 5th June when I wrote the
`first post here`_ until now, 19538 lines were added and 9435 deleted in 375
files. Only looking at the ``qutebrowser/`` subtree (i.e. actual source,
without tests/scripts), the numbers are a bit smaller though: 9975 added and
5701 removed lines in 124 files.

***********
What's next
***********

As mentioned above, today I'll start studying, so currently it's quite hard for
me to predict how much time I'll be able to spend on qutebrowser in the near
future. I expect it to roughly go back to the levels it was before the
crowdfunding started, which is still `a lot of activity`_.

As for things I plan to work on: First of all, I want to get downloads and the
other missing QtWebEngine features working. However, before that, some other
areas (namely error messages and prompts) need some bigger changes, as I don't
know which window/tab a download originated from with QtWebEngine.

For messages, this was already `done`_ a week ago, along with a new UI for
messages and a lot of simplified code. For prompts, there's `an issue`_
collecting some ideas and information.

After the remaining QtWebEngine stuff is out of the way, I plan to look at some
postponed `pull requests`_.

The next big topic to tackle is the `config revolution`_ which changes the way
how qutebrowser is configured (splitting the config into a `YAML`_ file for the
GUI config and a simple Python config for manual configuration).

After that, it's probably time for a qutebrowser v1.0 release!

*******************
Stickers and shirts
*******************

If your perk only contained stickers and you've not recieved them yet, please
let me know. 

If you didn't get anything in the crowdfunding but still would like some
stickers, please let me know as well - if there's enough interest, I'll set up
a way to get stickers with a donation.

As for t-shirts: Don't panic, you didn't miss anything. This was a bigger
logistic challenge than I thought it would be, but they're ordered in the
meantime. I hope they'll arrive at a friend's place in (southern) Germany this
or next week, and then we'll need to find a weekend where we both have the time
to send them out to you. Sending them from Germany instead of Switzerland saves
me trouble with customs inside the EU and some 500€ in postage, so it's
definitely worth the hassle!

*******
Thanks!
*******

Finally, I'd like to thank everyone involved in the crowdfunding again. You all
made this possible, and QtWebEngine support would be nowhere where it is
without you all. It was a blast, and I hope I'll be able to do something
similar again some time in the future.

Thank you!

.. _University of applied sciences in Rapperswil: https://www.hsr.ch/Home.home.0.html?L=4
.. _usual in software development: https://en.wikipedia.org/wiki/Hofstadter%27s_law
.. _missing: https://github.com/The-Compiler/qutebrowser/issues/666
.. _first post here: {filename}/00_Timeline.rst
.. _a lot of activity: https://github.com/The-Compiler/qutebrowser/graphs/contributors
.. _done: https://github.com/The-Compiler/qutebrowser/compare/5bef7dc74c26bcdc9bc2453c48e6f75daeaac5ac...e338d4b49ce8ec198ed2f000d1af4ec8cc08a42c
.. _an issue: https://github.com/The-Compiler/qutebrowser/issues/1898#issuecomment-247460199
.. _pull requests: https://github.com/The-Compiler/qutebrowser/pulls
.. _config revolution: https://github.com/The-Compiler/qutebrowser/issues/499
.. _YAML: https://en.wikipedia.org/wiki/YAML
