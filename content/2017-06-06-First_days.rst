############
First 2 days
############

:category: config

Today was the first day in my "office" (the local `hackerspace`_) working on
qutebrowser, and day 2 of the crowdfunding in total!

.. _hackerspace: https://www.ccczh.ch/

Right now I'm preparing some things for the new config to be possible, and also
finishing some work related to QtWebEngine and Qt 5.9.

Here's what happened since the weekend:

- Stickers for backers who don't have a t-shirt are all sent out. Let me know
  when you get them!
- The check for the unsupported Nouveau graphic driver with QtWebEngine is now
  `more stable <https://github.com/qutebrowser/qutebrowser/commit/a858611bb9ac392b0a08f616b4c1a4feda7c3af4>`_
  and also `can be used <https://github.com/qutebrowser/qutebrowser/commit/4d64bcc8521e73d67c068688fd8e89b8f94433c0>`_
  from an already running instance with ``:debug-console``.
- Some `reply object tracking <https://github.com/qutebrowser/qutebrowser/commit/a45de9cef2f8c292d42aa4f63bf6a1ea08557508>`_
  which was originally introduced to help with segfaults on exit with old Qt
  versions was removed as it's not needed anymore, and caused problems with the
  PyQt 5.9 snapshots.
- Download error messages are now
  `displayed <https://github.com/qutebrowser/qutebrowser/commit/d4f58533c0f93d423ab83d09f769a86fba88103e>`_
  with QtWebEngine on Qt 5.9. I've had this patch lying around for a while, but
  now I could finally test it with an updated PyQt.
- Chromium logging messages occurring during tests are now
  `properly parsed <https://github.com/qutebrowser/qutebrowser/commit/998f93dfd3458f4f9a84e6b6c3f532667ba99c23>`_
  and updated for Qt 5.9.
- The way defaults are handled for settings passed to the web backend was
  `refactored <https://github.com/qutebrowser/qutebrowser/commit/1785b72393f6f4b0d4f8bd02ab8a45931efbe7ff>`_
  so they don't require a getter anymore (which would've gotten difficult with
  the new settings, as there's no one true value anymore).
- While working on that, I noticed clicking an element via javascript didn't use the right setting object when using private browsing, so I
  `fixed <https://github.com/qutebrowser/qutebrowser/commit/f9b046d766eb6ecadd3787fbdad2f04d097fd1cc>`_ that.
- Some settings which (according to past crash reports) almost nobody did modify were
  `removed <https://github.com/qutebrowser/qutebrowser/commit/2a32e26846b34cf668d2d21d14189934f69316a5>`_ or
  `merged <https://github.com/qutebrowser/qutebrowser/commit/c69672365023d3dfb5739d104fcb98af8b44f60a>`_.
- A setting got
  `renamed <https://github.com/qutebrowser/qutebrowser/commit/0ca59f2184b1953869529be431d7985470997a49>`_
  to make clearer what it does. I expect to rename many more settings at a later point though.
- A pull request adding a ``{private}`` field to the ``window-title`` setting was
  `accepted <https://github.com/qutebrowser/qutebrowser/commit/49b8737f7979fc878ba25aed94cc3e57f481ae3a>`_.

Tomorrow, I plan to take a closer look at a
`quite big pull request <https://github.com/qutebrowser/qutebrowser/pull/2295>`_
(maybe even the biggest in qutebrowser's history?) refactoring most of the
completion code and fixing many issues in the process. Unfortunately it has some
performance issues, but I'd really like to get it in before starting the big
config rewriting.
