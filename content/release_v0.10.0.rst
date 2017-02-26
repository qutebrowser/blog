############################
qutebrowser v0.10.0 released
############################

:category: releases
:tags: pyplanet, qtplanet

I'm happy to annouce the release of qutebrowser v0.10.0!

qutebrowser is a keyboard driven browser with a vim-like, minimalistic
interface. It's written using PyQt and cross-platform.

I haven't announced the v0.9.0 release in this blog (or any patch releases), but
for v0.10.0 it definitely makes sense to do so, as it's mostly centered on
QtWebEngine!

The full changelog for this release:

Added
-----

-  Userscripts now have a new ``$QUTE_COMMANDLINE_TEXT`` environment
   variable, containing the current commandline contents
-  New ``ripbang`` userscript to create a searchengine from a duckduckgo
   bang
-  `QtWebKit Reloaded <https://github.com/annulen/webkit/wiki>`__ (also
   called QtWebKit-NG) is now fully supported
-  Various new functionality with the QtWebEngine backend:

   -  Printing support with Qt >= 5.8
   -  Proxy support with Qt >= 5.8
   -  The ``general -> print-element-backgrounds`` option with Qt >= 5.8
   -  The ``content -> cookies-store`` option
   -  The ``storage -> cache-size`` option
   -  The ``colors -> webpage.bg`` option
   -  The HTML5 fullscreen API (e.g. youtube videos) with QtWebEngine
   -  ``:download --mhtml``

-  New ``qute:history`` URL and ``:history`` command to show the
   browsing history
-  Open tabs are now auto-saved on each successful load and restored in
   case of a crash
-  ``:jseval`` now has a ``--file`` flag so you can pass a javascript
   file
-  ``:session-save`` now has a ``--only-active-window`` flag to only
   save the active window
-  OS X builds are back, and built with QtWebEngine

Changed
-------

-  PyQt 5.7/Qt 5.7.1 is now required for the QtWebEngine backend
-  Scrolling with the scrollwheel while holding shift now scrolls
   sideways
-  New way of clicking hints which solves various small issues
-  When yanking a mailto: link via hints, the mailto: prefix is now
   stripped
-  Zoom level messages are now not stacked on top of each other anymore
-  qutebrowser now automatically uses QtWebEngine if QtWebKit is
   unavailable
-  :history-clear now asks for a confirmation, unless it's run with
   --force.
-  ``input -> mouse-zoom-divider`` can now be 0 to disable zooming by
   mouse wheel
-  ``network -> proxy`` can also be set to ``pac+file://...`` now to use
   a local proxy autoconfig file (on QtWebKit)

Fixed
-----

-  Various bugs with Qt 5.8 and QtWebEngine:

   -  Segfault when closing a window
   -  Segfault when closing a tab with a search active
   -  Fixed various mouse actions (like automatically entering insert
      mode) not working
   -  Fixed hints sometimes not working
   -  Segfault when opening a URL after a QtWebEngine renderer process
      crash

-  Other QtWebEngine fixes:

   -  Insert mode now gets entered correctly with a non-100% zoom
   -  Crash reports are now re-enabled when using QtWebEngine
   -  Fixed crashes when closing tabs while hinting
   -  Using :undo or :tab-clone with a view-source:// or chrome:// tab
      is now prevented, as it segfaults

-  ``:enter-mode`` now refuses to enter modes which can't be entered
   manually (which caused crashes)
-  ``:record-macro`` (``q``) now doesn't try to record macros for
   special keys without a text
-  Fixed PAC (proxy autoconfig) not working with QtWebKit
-  ``:download --mhtml`` now uses the new file dialog
-  Word hints are now upper-cased correctly when hints -> uppercase is
   true
-  Font validation is now more permissive in the config, allowing e.g.
   "Terminus (TTF)" as font name
-  Fixed starting on newer PyQt/sip versions with LibreSSL
-  When downloading files with QtWebKit, a User-Agent header is set when
   possible
-  Fixed showing of keybindings in the :help completion
-  ``:navigate prev/next`` now detects ``rel`` attributes on ``<a>``
   elements, and handles multiple ``rel`` attributes correctly
-  Fixed a crash when hinting with target ``userscript`` and spawning a
   non-existing script
-  Lines in Jupyter notebook now trigger insert mode
