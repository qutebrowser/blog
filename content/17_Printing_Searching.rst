##############################
Day 17: Printing and searching
##############################

:category: webengine

After looking at a `pull request`_ adding a ``:print --pdf`` flag to directly
print to PDF (and an accompanying test), I noticed I totally forgot to add
printing support to the new tab API. This wasn't caught previously because
there was no test for printing (as it's hard to use the print dialog
programmatically).

I `added some API`_ for printing and fixed up the PR as well as the current
printing code. Unfortunately real print support is still missing upstream in
QtWebEngine, but ``:print --pdf`` should work with QtWebEngine with a (yet to
be released) enough recent PyQt version.

The PDF printing test failed on Windows - the issue wasn't entirely obvious at
first: Windows uses backslashes as path separators, but the qutebrowser
commandline (which is also used by the end-to-end tests) uses that to escape
quotes - I pushed a `change`_ to (almost) always escape backslashes in commands
for the tests, which fixed that and didn't break anything else.

After that I took a look at the searching code, as that was probably what I
missed the most when trying to use QtWebEngine in qutebrowser to browser
documentation.

I had to `restructure`_ things quite a bit as much was handled inside
qutebrowser's ``QWebView`` subclass, but now searching works with QtWebEngine
as well - and it even shows the nice indicators on the scrollbar, like
Chromium:

.. image:: /images/searching.png
   :alt: scroll bar while searching

I also ended up `removing`_ support for the setting ``general -> wrap-search``,
which now is always ``true``. Only very few people seemed to change that
setting, and QtWebEngine always wraps without a possibility to influence that.

.. _pull request: https://github.com/The-Compiler/qutebrowser/pull/1639
.. _added some API: https://github.com/The-Compiler/qutebrowser/commit/cd4eff364a841b36c6fa1653ef8f0284ab1beef0
.. _change: https://github.com/The-Compiler/qutebrowser/commit/e5cab1197963cde7ff165de0273aacd35ca64fed
.. _restructure: https://github.com/The-Compiler/qutebrowser/commit/f0da508c218ad57289bdb9268faeba7b7741a233
.. _removing: https://github.com/The-Compiler/qutebrowser/commit/64b32ec87d739b3df7119c7857e8dbe38429139b
