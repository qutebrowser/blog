###########################
qutebrowser v0.7.0 released
###########################

:category: releases
:tags: pyplanet, qtplanet

I'm happy to annouce the release of qutebrowser v0.7.0!

qutebrowser is a keyboard driven browser with a vim-like, minimalistic
interface. It's written using PyQt and cross-platform.

As usual the source release is available, binary releases
(Windows as usual, and now also a standalone OS X .app/.dmg and a
Debian .deb) will follow ASAP (but might be Monday until everything is
taken care of).

This is a really exciting release! It comes with fixes for a few
long-standing bugs (like being able to use :hint spawn with flags or
sharing of cookies between tabs with private browsing) and includes
many new features (like marks to remember the scroll position).

It also comes with a greatly improved hint and history implementation:
Hints now work more reliably in some corner cases, and gained a few
new features and other bugfixes. The history completion now contains
titles and handles redirects.

And there's a lot more than that - see the full changelog:

Added
*****

- New ``:edit-url`` command to edit the URL in an external editor.
- New ``network -> custom-headers`` setting to send custom headers with every request.
- New ``{url:pretty}`` commandline replacement which gets replaced by the decoded URL.
- New marks to remember a scroll position:
    - New ``:jump-mark`` command to jump to a mark, bound to ``'``
    - New ``:set-mark`` command to set a mark, bound to ` (backtick)
    - The ``'`` mark gets set when moving away (hinting link with anchor, searching, etc.) so you can move back with ``''``
- New ``--force-color`` argument to force colored logging even if stdout is not a
  terminal
- New ``:messages`` command to show error messages
- New pop-up showing possible keybinding when the first key of a keychain is
  pressed. This can be turned off using ``:set ui keyhint-blacklist *``.
- New ``hints -> auto-follow-timeout`` setting to ignore keypresses after
  following a hint when filtering in number mode.
- New ``:history-clear`` command to clear the entire history
- New ``hints -> find-implementation`` to select which implementation (JS/Python)
  should be used to find hints on a page. The ``javascript`` implementation is
  better, but slower.

Changed
*******

- qutebrowser got a new (slightly updated) logo
- ``:tab-focus`` can now take a negative index to focus the nth tab counted from
  the right.
- ``:yank`` can now yank the pretty/decoded URL by adding ``--pretty``
- ``:navigate`` now clears the URL fragment
- ``:completion-item-del`` (``Ctrl-D``) can now be used in ``:buffer`` completion to
  close a tab
- Counts can now be used with special keybindings (e.g. with modifiers)
- Various SSL ciphers are now disabled by default. With recent Qt/OpenSSL
  versions those already all are disabled, but with older versions they might
  not be.
- Show favicons as window icon with ``tabs-are-windows`` set.
- ``:bind <key>`` without a command now shows the existing binding
- The optional ``colorlog`` dependency got removed, as qutebrowser now displays
  colored logs without it.
- URLs are now shown decoded when hovering.
- Keybindings are now shown in the command completion
- Improved behavior when pasting multiple lines
- Rapid hints can now also be used for the ``normal`` hint target, which can be
  useful with javascript click handlers or checkboxes which don't actually open
  a new page.
- ``:zoom-in`` or ``:zoom-out`` (``+``/``-``) with a too large count now zooms to the
  smallest/largest zoom instead of doing nothing.
- The commandline now accepts partially typed commands if they're unique.
- Number hints are now kept filtered after following a hint in rapid mode.
- Number hints are now renumbered after filtering
- Number hints can now be filtered with multiple space-separated search terms
- ``hints -> scatter`` is now ignored for number hints
- Better history implementation which also stores titles.
  As a consequence, URLs which redirect to another URL are now added to the
  history too, marked with a ``-r`` suffix to the timestamp field.

Fixed
*****

- Fixed using ``:hint links spawn`` with flags - you can now use things like the
  ``-v`` argument for ``:spawn`` or pass flags to the spawned commands.
- Various fixes for hinting corner-cases where following a link didn't work or
  the hint was drawn at the wrong position.
- Fixed crash when downloading from an URL with SSL errors
- Close file handles correctly when a download failed
- Fixed crash when using ``;Y`` (``:hint links yank-primary``) on a system without
  primary selection
- Don't display quit confirmation with finished downloads
- Fixed updating the tab index in the statusbar when opening a background tab
- Fixed a crash when entering ``:--`` in the commandline
- Fixed ``:debug-console`` with PyQt 5.6
- Fixed qutebrowser not starting when ``sys.stderr`` is ``None``
- Fixed crash when cancelling a download which belongs to a MHTML download
- Fixed rebinding of keybindings being case-sensitive
- Fix for tab indicators getting lost when moving tabs
- Fixed handling of backspace in number hinting mode
- Fixed ``FileNotFoundError`` when starting in some cases on old Qt versions
- Fixed sharing of cookies between tabs when ``private-browsing`` is enabled
- Toggling values with ``:set`` now uses lower-case values
- Hints now work with (non-standard) links with spaces around the URL
- Strip off trailing spaces for history entries with no title

Since v0.6.0, the following people have contributed to qutebrowser:

- Ryan Roden-Corrent
- Daniel Schadt
- Jakub Klinkovsk
- Panagiotis Ktistakis
- Corentin Jul
- Felix Van der Jeugt
- Tarcisio Fedrizzi
- Liam BEGUIN
- Jimmy
- kanikaa1234
- Tomasz Kramkowski
- Philipp Hansch
- Nick Ginther
- Fritz Reichwald
- haitaka
- Ismail
- adam
- Stefan Tatschner
- Samuel Loury
- Jan Verbeek
- oniondreams
- Xitian9
- Noah Huesser
- Johannes Martinsson
- Jay Kamat
- Error 800
- Alexey Glushko

Thank you!
