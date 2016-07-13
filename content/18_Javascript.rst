##################
Day 18: Javascript
##################

:category: webengine

Today I was mostly busy with javascript related functionality and writing some
javascript:

- Added `logging`_ for javascript console logging with QtWebEngine
- `Don't fail`_ tests with QtWebEngine ``STUB: ...`` messages
- Implement :`scroll-perc`_ via javascript
- Implement :`scroll-px`_ and ``scroll.to_point`` (used for e.g. marks) via javascript
- Implement :`scroll-page`_ via javascript
- Various related changes to tests

I also added `run_js_blocking`_ to the tab API which runs javascript and
returns the result. I then tried to use that API to handle getting scroll
positions, but I didn't get it to work correctly yet (loading websites now
just hangs). Things are unfortunately a bit tricky as it involves a nested
local Qt event loop and three languages (Javascript, C++, Python)... I'll
continue trying to debug it tomorrow, and I have an alternative solution not
needing a blocking JS method in mind.

.. _logging: https://github.com/The-Compiler/qutebrowser/commit/9c49900f9e98fc9f11115ce2bca864ece6899b59
.. _Don't fail: https://github.com/The-Compiler/qutebrowser/commit/e0ab70c8cff1c096d7a8d8c0ede043fe9fc57147
.. _scroll-perc: https://github.com/The-Compiler/qutebrowser/commit/b78b89f04f75c3b113e62179a863dca3395112ec
.. _scroll-px: https://github.com/The-Compiler/qutebrowser/commit/602d10c495b2ba5eb3318fd346d968008625bb44
.. _scroll-page: https://github.com/The-Compiler/qutebrowser/commit/c83a8a64dcb56e9b47aff4473a6e273b9ca7ca74
.. _run_js_blocking: https://github.com/The-Compiler/qutebrowser/commit/5b1cca92ab199798337d873f8a708df7acebe12a
