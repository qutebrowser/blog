###########################
qutebrowser v0.8.0 released
###########################

:category: releases
:tags: pyplanet, qtplanet

I'm happy to annouce the release of qutebrowser v0.8.0!

qutebrowser is a keyboard driven browser with a vim-like, minimalistic
interface. It's written using PyQt and cross-platform.

The main reason for this release is that v0.7.0 will break with
PyQt 5.7 which is soon going to be released.

I decided to do a new minor release instead of a patch release as
plenty new features have accumulated already. If your distribution
can't update to v0.8.0 for some reason, backporting `this patch`_
patch *should* work, though I haven't verified this.

.. _this patch: https://github.com/The-Compiler/qutebrowser/commit/63e466f01985abd7be275855f0af7450eb97d8e1

This release also got a big refactoring to prepare for QtWebEngine
support. To my current knowledge, all issues have been smoothened out.
If not, crash reports shall now tell me. ;)

You can also already start with "``--backend webengine``" with this
release to try the QtWebEngine support - however many features are
still missing.

Source release and binaries for Windows/OS X are available, the Debian
packages are still work-in-progress.

The full changelog for this release:

Added
*****

- New ``:repeat-command`` command (mapped to ``.``) to repeat the last command.
  Note that two former default bundings conflict with that binding, unbinding
  them via ``:unbind .i`` and ``:unbind .o`` is recommended.
- New ``qute:bookmarks`` page which displays all bookmarks and quickmarks.
- New ``:prompt-open-download`` (bound to ``Ctrl-X``) which can be used to open a
  download directly when getting the filename prompt.
- New ``{host}`` replacement for tab- and window titles which evaluates
  to the current host.
- New default binding ``;t`` for ``:hint input``.
- New variables ``$QUTE_CONFIG_DIR``, ``$QUTE_DATA_DIR`` and
  ``$QUTE_DOWNLOAD_DIR`` available for userscripts.
- New option ``ui`` -> ``status-position`` to configure the position of the
  status bar (top/bottom).
- New ``--pdf <filename>`` argument for ``:print`` which can be used to generate a
  PDF without a dialog.

Changed
*******

- ``:scroll-perc`` now prefers a count over the argument given to it, which means
  ``gg`` can be used with a count.
- Aliases can now use ``;;`` to have an alias which executed multiple commands.
- ``:edit-url`` now does nothing if the URL isn't changed in the spawned editor.
- ``:bookmark-add`` can now be passed a URL and title to add that as a bookmark
  rather than the current page.
- New ``taskadd`` userscript to add a taskwarrior task annotated with the
  current URL.
- ``:bookmark-del`` and ``:quickmark-del`` now delete the current page's URL if none
  is given.

Fixed
*****

- Compatibility with PyQt 5.7
- Fixed some configuration values being lost when a config option gets removed
  from qutebrowser's code.
- Fix crash when downloading with a full disk
- Using ``:jump-mark`` (e.g. ``''``) when the current URL is invalid doesn't crash
  anymore.

Removed
*******

- The ability to display status messages from webpages, as well as the related
  ``ui ->  display-statusbar-messages`` setting.
- The ``general -> wrap-search`` setting as searches now always wrap.
  According to a quick straw poll and prior crash logs, almost nobody is using
  ``wrap-search = false``, and turning off wrapping is not possible with
  QtWebEngine.
- ``:edit-url`` now doesn't accept a count anymore as its behavior was confusing
  and it doesn't make much sense to add a count.

Since v0.7.0, the following people have contributed to qutebrowser:

- Ryan Roden-Corrent
- Jan Verbeek
- Daniel Schadt
- Marshall Lochbaum
- Ismail S
- David Vogt
- Michał Góral
- Panashe M. Fundira
- Jeremy Kaplan
- Edgar Hipp
- Daryl Finlay
- Jean-Louis Fuchs
- Kevin Velghe
- Jakub Klinkovský
- Dietrich Daroch

Thank you!
