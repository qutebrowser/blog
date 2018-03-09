############################
qutebrowser v1.2.0 released!
############################

:category: releases
:tags: pyplanet, qtplanet

I'm happy to announce that I just released qutebrowser v1.2.0!

qutebrowser is a keyboard driven browser with a vim-like, minimalistic
interface. It's written using PyQt and cross-platform.

This release comes with a long changelog, but the most interesting changes are
probably initial support for per-domain settings (I've had JavaScript disabled
globally for a while myself now) and a big refactoring of how keybindings are
handled (allowing for emacs-like key chains with modifiers).

Here's the complete changelog:

Added
-----

- Initial implementation of per-domain settings:

  - ``:set`` and ``:config-cycle`` now have a ``-u``/``--pattern`` argument taking a URL match pattern for supported settings.
  - ``config.set`` in ``config.py`` now takes a third argument which is the pattern.
  - New ``with config.pattern('...') as p:`` context manager for ``config.py`` to use the shorthand syntax with a pattern.
  - New ``tsh`` keybinding to toggle scripts for the current host. With a capital ``S``, the toggle is saved. With a capital ``H``, subdomains are included. With ``u`` instead of ``h``, the exact current URL is used.
  - New ``tph`` keybinding to toggle plugins, with the same additional binding described above.

- New QtWebEngine features:

  - Caret/visual mode
  - Authentication via ~/.netrc
  - Retrying downloads with Qt 5.10 or newer
  - Hinting and other features inside same-origin frames

- New flags for existing commands:

  - ``:session-load`` has a new ``--delete`` flag which deletes the session after loading it.
  - New ``--no-last`` flag for ``:tab-focus`` to not focus the last tab when focusing the currently focused one.
  - New ``--edit`` flag for ``:view-source`` to open the source in an external editor.
  - New ``--select`` flag for ``:follow-hint`` which acts like the given string was entered but doesn't necessary follow the hint.

- New special pages:

  - ``qute://bindings`` (opened via ``:bind``) which shows all keybindings.
  - ``qute://tabs`` (opened via ``:buffer``) which lists all tabs.

- New settings:

  - ``statusbar.widgets`` to configure which widgets should be shown in which order in the statusbar.
  - ``tabs.mode_on_change`` which replaces ``tabs.persist_mode_on_change``. It can now be set to ``restore`` which remembers input modes (input/passthrough) per tab.
  - ``input.insert_mode.auto_enter`` which makes it possible to disable entering insert mode automatically when an editable element was clicked. Together with ``input.forward_unbound_keys``, this should allow for emacs-like "modeless" keybindings.

- New ``:prompt-yank`` command (bound to ``Alt-y`` by default) to yank URLs referenced in prompts.
- The ``hostblock_blame`` script which was removed in v1.0 was updated for the new config and re-added.
- New ``cycle-inputs.js`` script in ``scripts/`` which can be used with ``:jseval -f`` to cycle through inputs.

Changed
-------

- Complete refactoring of key input handling, with various effects:

  - emacs-like keychains such as ``<Ctrl-X><Ctrl-C>`` can now be bound.
  - Key chains can now be bound in any mode (this allows binding unused keys in hint mode).
  - Yes/no prompts don't use keybindings from the ``prompt`` section anymore, they have their own ``yesno`` section instead.
  - Trying to bind invalid keys now shows an error.
  - The ``bindings.default`` setting can now only be set in a ``config.py``, and existing values in ``autoconfig.yml`` are ignored.

- Improvements for GreaseMonkey support:

  - ``@include`` and ``@exclude`` now support regex matches. With QtWebEngine and Qt 5.8 and newer, Qt handles the matching, but similar functionality will be added in Qt 5.11.
  - Support for ``@requires``
  - Support for the GreaseMonkey 4.0 API

- The sqlite history now uses write-ahead logging which should be a performance and stability improvement.
- When an editor is spawned with ``:open-editor`` and ``:config-edit``, the changes are now applied as soon as the file is saved in the editor.
- The ``hist_importer.py`` script now only imports URL schemes qutebrowser can handle.
- Deleting a prefix (``:``, ``/`` or ``?``) via backspace now leaves command mode.
- Angular 1 elements and ``<summary>``/``<details>`` now get hints assigned.
- ``:tab-only`` with pinned tabs now still closes unpinned tabs.
- The ``url.incdec_segments`` option now also can take ``port`` as possible segment.
- QtWebEngine: ``:view-source`` now uses Chromium's ``view-source:`` scheme.
- Tabs now show their full title as tooltip.
- When there are multiple unknown keys in a autoconfig.yml, they now all get reported in one error.
- More performance improvements when opening/closing many tabs.
- The ``:version`` page now has a button to pastebin the information.
- Replacements like ``{url}`` can now be escaped as ``{{url}}``.

Fixed
-----

- QtWebEngine bugfixes:

  - Improved fullscreen handling with Qt 5.10.
  - Hinting and scrolling now works properly on special ``view-source:`` pages.
  - Scroll positions are now restored correctly from sessions.
  - ``:follow-selected`` should now work in more cases with Qt > 5.10.
  - Incremental search now flickers less and doesn't move to the second result when pressing Enter.
  - Keys like ``Ctrl-V`` or ``Shift-Insert`` are now correctly handled/filtered with Qt 5.10.
  - Fixed hangs/segfaults on exit with Qt 5.10.1.
  - Fixed favicons sometimes getting cleared with Qt 5.10.
  - Qt download objects are now cleaned up properly when a download is removed.
  - JavaScript messages are now not double-HTML escaped anymore on Qt < 5.11

- QtWebKit bugfixes:

  - Fixed GreaseMonkey-related crashes.
  - ``:view-source`` now displays a valid URL.

- URLs containing ampersands and other special chars are now shown correctly when filtering them in the completion.
- ``:bookmark-add "" foo`` can now be used to save the current URL with a custom title.
- ``:spawn -o`` now waits until the process has finished before trying to show the output. Previously, it incorrectly showed the previous output immediately.
- Suspended pages now should always load the correct page when being un-suspended.
- Exception types are now shown properly with ``:config-source`` and ``:config-edit``.
- When using ``:bookmark-add --toggle``, bookmarks are now saved properly.
- Crash when opening an invalid URL from an application on macOS.
- Crash with an empty ``completion.timestamp_format``.
- Crash when ``completion.min_chars`` is set in some cases.
- HTML/JS resource files are now read into RAM on start to avoid crashes when changing qutebrowser versions while it's open.
- Setting ``bindings.key_mappings`` to an empty value is now allowed.
- Bindings to an empty commands are now ignored rather than crashing.

Removed
-------

- ``QUTE_SELECTED_HTML`` is now not set for userscripts anymore except when called via hints.
- The ``qutebrowser_viewsource`` userscript has been removed as ``:view-source --edit`` can now be used.
- The ``tabs.persist_mode_on_change`` setting has been removed and replaced by ``tabs.mode_on_change``.
