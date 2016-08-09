#############################
Days 31/32: More web elements
#############################

:category: webengine

Apart from `fixing`_ some QtWebEngine `bugs`_, yesterday and today I made some
big progress with the web element code. I successfully `split`_ the web element
code into a generic and a QtWebKit part, and then did a first `implementation`_
of the web element code for QtWebEngine, which made ``:navigate prev`` and
``:navigate forward`` work.

After `implementing`_ some more missing web element stubs (and adding a missing
``.lower()`` call), I got ``:open-editor`` to work as well.

I then noticed the javascript linter qutebrowser is using (`eslint`_) didn't
actually report anything. I tracked this down to a v1.0.0 release which turns
off all rules by default, which I somehow missed. After `reconfiguring`_ it, I
had more useful output and cleaned up some style issues.

Then I properly `modularized`_ the javascript code and did some other cleanups
to ensure it doesn't remain in its initial proof-of-concept state for any
longer.

By chance I noticed that ``flake8`` (one of the Python linters qutebrowser is
using) also didn't do much anymore, which was due to me not passing a file path
to it. I `fixed`_ that and also `cleaned up`_ some issues which went unnoticed
in the meantime.

I planned to work on the hint drawing code, but since various pull requests
related to hints were opened today, I decided to postpone that to after they
are merged.

.. _fixing: https://github.com/The-Compiler/qutebrowser/commit/627f743c26f72792293126e12118d3e53f25d161
.. _bugs: https://github.com/The-Compiler/qutebrowser/commit/27330bd4d1ed67447ce610a0b03784e0b3baaadf
.. _split: https://github.com/The-Compiler/qutebrowser/commit/dfbadaf7c24f3245e387f33f1347c2e53d74b820
.. _implementation: https://github.com/The-Compiler/qutebrowser/commit/b8e2d5f8f6a3547fede59e1dbc8e65f5e3c7358f
.. _implementing: https://github.com/The-Compiler/qutebrowser/commit/9a17591fb7761bbe31c853ca01d22f1c82037944
.. _eslint: https://www.eslint.org/
.. _reconfiguring: https://github.com/The-Compiler/qutebrowser/commit/4da53480c20d2d5943be9137357ef9bdf1a34acc
.. _modularized: https://github.com/The-Compiler/qutebrowser/commit/6b7a39685e43a8728eaf24567b407b0f625cff7a
.. _fixed: https://github.com/The-Compiler/qutebrowser/commit/2cbb147e33bcbdf2471294c42b66da9774170fa5
.. _cleaned up: https://github.com/The-Compiler/qutebrowser/commit/fb3da578c56b3b33aaee4cd8d92a5767995cfcdc
