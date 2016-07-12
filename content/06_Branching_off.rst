####################
Day 6: Branching off
####################

:category: webengine

After `releasing`_ v0.7.0 last Friday, I could finally start refactoring stuff
for QtWebEngine support today.

.. _releasing: {filename}/release_v0.6.0.rst

Nothing really works properly yet, but I was able to open a website:

.. image:: /images/day_6_small.png
   :alt: qutebrowser with QtWebEngine user agent
   :target: /images/day_6.png

I also merged a `pull request`_ to master which adds a ``{host}`` replacement
for the title/tab-title format settings, and reviewed two other new pull
requests:

- `Aliases with multiple commands`_
- `Unit tests for completion models`_

.. _pull request: https://github.com/The-Compiler/qutebrowser/pull/1570
.. _Aliases with multiple commands: https://github.com/The-Compiler/qutebrowser/pull/1577
.. _Unit tests for completion models: https://github.com/The-Compiler/qutebrowser/pull/1572
