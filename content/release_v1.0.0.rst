############################
qutebrowser v1.0.0 released!
############################

:category: releases
:tags: pyplanet, qtplanet

I'm delighted to announce that I just released qutebrowser v1.0.0!

qutebrowser is a keyboard driven browser with a vim-like, minimalistic
interface. It's written using PyQt and cross-platform.

This release comes with many big breaking changes such as the new config and
QtWebEngine by default, so please take a look at the changelog.

As announced previously, per-domain settings unfortunately didn't make it into
v1.0.0 - it's the next thing I plan on tackling. However, there's more than
enough big things in v1.0.0! :)

Enjoy!

The full changelog for this release:

Major changes
-------------

- Dependency changes:

  - Support for legacy QtWebKit (before 5.212 which is
    `distributed independently from Qt <https://github.com/annulen/webkit/wiki>`__
    is dropped.
  - Support for Python 3.4 is dropped.
  - Support for Qt before 5.7.1 and PyQt before 5.7 is dropped.
  - New dependency on the QtSql module and Qt sqlite support.
  - New dependency on the `attrs <http://www.attrs.org/>`__ project (packaged as
    ``python-attr`` in some distributions).
  - The depedency on PyOpenGL (when using QtWebEngine) got removed. Note
    that PyQt5.QtOpenGL is still a dependency.
  - PyQt5.QtOpenGL is now always required, even with QtWebKit.

- The QtWebEngine backend is now used by default. Note this means that
  QtWebEngine now should be a required dependency, and QtWebKit (if new enough)
  should be changed to an optional dependency.
- Completely rewritten configuration system which ignores the old config file.
  See ``qute://help/configuring.html`` for details.
- Various documentation files got moved to the doc/ subfolder; ``qutebrowser.desktop`` got moved to misc/.
- ``:set`` now doesn't support toggling/cycling values anymore, that functionality got moved to ``:config-cycle``.
- New completion engine based on sqlite, which allows to complete
  the entire browsing history. The default for
  ``completion.web_history_max_items`` got changed to ``-1`` (unlimited). If the
  completion is too slow on your machine, try setting it to a few 1000 items.

Added
-----

- QtWebEngine: Spell checking support, see the ``spellcheck.languages`` setting.
- New ``qt.args`` setting to pass additional arguments to Qt/Chromium.
- New ``backend`` setting to select the backend to use.
  Together with the previous setting, this should make most wrapper scripts
  unnecessary.
- qutebrowser can now be set as the default browser on macOS.
- New config commands:

  - ``:config-cycle`` to cycle an option between multiple values.
  - ``:config-unset`` to remove a configured option.
  - ``:config-clear`` to remove all configured options.
  - ``:config-source`` to (re-)read a ``config.py`` file.
  - ``:config-edit`` to open the ``config.py`` file in an editor.
  - ``:config-write-py`` to write a ``config.py`` template file.

- New ``:version`` command which opens ``qute://version``.
- New back/forward indicator in the statusbar.
- New ``bindings.key_mappings`` setting to map keys to other keys.
- QtWebEngine: Support for proxy authentication.

Changed
-------

- Using ``:download`` now uses the page's title as filename.
- Using ``:back`` or ``:forward`` with a count now skips intermediate pages.
- When there are multiple messages shown, the timeout is increased.
- ``:search`` now only clears the search if one was displayed before, so pressing
  ``<Escape>`` doesn't un-focus inputs anymore.
- Pinned tabs now adjust to their text's width, so the ``tabs.width.pinned``
  setting got removed.
- ``:set-cmd-text`` now has a ``--run-on-count`` argument to run the underlying
  command directly if a count was given.
- ``:scroll-perc`` got renamed to ``:scroll-to-perc``.

Removed
-------

- Migrating QtWebEngine data written by versions before 2016-11-15 (before
  v0.9.0) is now not supported anymore.
- Upgrading qutebrowser with a version older than v0.4.0 still running now won't
  work properly anymore.
- The ``--harfbuzz`` and ``--relaxed-config`` commandline arguments got dropped.

Fixes
-----

- Exiting fullscreen via ``:fullscreen`` or buttons on a page now
  restores the correct previous window state (maximized/fullscreen).
- When ``input.insert_mode.auto_load`` is set, background tabs now don't enter
  insert mode anymore.
- The keybinding help widget now works correctly when using keybindings with a
  count.
- The ``window.hide_wayland_decoration`` setting now works correctly again.
