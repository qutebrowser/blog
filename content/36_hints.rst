##############
Day 36: Hints!
##############

:category: webengine

Today I did a lot more work on hints! After some `refinements`_ on my hint
drawing branch, I `opened`_ a pull request to get some feedback from other
developers.

After that, I `continued`_ working on hints for QtWebEngine, and got the basics
to work:

.. image:: /images/hints_webengine_small.png
   :alt: basic hints with QtWebEngine!
   :target: /images/hints_webengine.png

However, it doesn't filter hints which aren't visible yet, which means its
performance is bad and the hint strings are longer than they should be.
Hopefully this will change tomorrow!

.. _refinements: https://github.com/The-Compiler/qutebrowser/compare/7c17af3889b15845fbccf9af07c224ca4c4dbe29...new-hints
.. _opened: https://github.com/The-Compiler/qutebrowser/pull/1868
.. _continued: https://github.com/The-Compiler/qutebrowser/compare/new-hints...webengine-hints
