##############################################
qutebrowser v1.3.3 released (security update!)
##############################################

:category: releases
:tags: pyplanet, qtplanet

I've just released qutebrowser v1.3.3, which fixes an XSS vulnerability
on the qute://history page (:history).

qutebrowser is a keyboard driven browser with a vim-like, minimalistic
interface. It's written using PyQt and cross-platform.

The vulnerability allowed websites to inject HTML into the page via a
crafted title tag. This could allow them to steal your browsing history.

If you're currently unable to upgrade, avoid using :history.

A CVE request for this issue is pending, see the relevant issue for updates:
https://github.com/qutebrowser/qutebrowser/issues/4011

The issue was introduced in March 2017 and part of the v0.11.0 release:
https://github.com/qutebrowser/qutebrowser/commit/845f21b275bf438eccd7854f7f5401233ec6719a
https://github.com/qutebrowser/qutebrowser/commit/1179ee7a937fb31414d77d9970bac21095358449

The patch applies cleanly to v1.2.x and v1.1.x (but I do not plan to do
any updated releases of those):
https://github.com/qutebrowser/qutebrowser/commit/5a7869f2feaa346853d2a85413d6527c87ef0d9f.patch

It does *not* apply to v1.0.x and v0.11.x. If you need a backport,
please let me know, but especially on v0.11.x you'll probably have a lot
of other security issues due to an outdated QtWebKit anyways.

I plan to release v1.4.0 later this week (once PyQt 5.11 is out), but
since the bug was opened publicly, I decided to do an immediate bugfix
release. As a reminder, for security-relevant bugs, please contact me
directly at mail at qutebrowser.org.

Other bugfixes in this release:

- Crash in a workaround for a Qt 5.11 bug in rare circumstances.
- Workaround for a Qt bug which preserves searches between page loads.
- In v1.3.2 a dependency on the `PyQt5.QtQuickWidgets` module was accidentally
  introduced. Since that module isn't packaged everywhere, it's been removed
  again.

Sorry for the trouble!
