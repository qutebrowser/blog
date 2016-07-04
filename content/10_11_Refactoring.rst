#######################
Day 10/11: Refactoring!
#######################

:category: webengine

I haven't blogged on Friday, so consider this the blog post for Friday and
Monday!

On Friday I had to go to the dentist again, so not as much time available as
I'd hoped. I was mainly busy with some more organizational stuff for the
crowdfunding and general maintenance. I also finally added the `backers`_ file
to the documentation!

.. _backers: https://github.com/The-Compiler/qutebrowser/blob/master/doc/backers.asciidoc

Today I continued working on refactoring all QtWebKit-specific code so there's
a well-defined API, and most (271) end-to-end tests pass by now:

- backforward
- caret
- history
- javascript
- keyinput
- marks
- misc
- navigate
- open
- prompts
- search
- sessions
- urlmarks
- zoom

The following commands/features now work again with QtWebKit:

- Searching
- Opening a new window via JS
- ``:undo``
- ``:buffer`` completion
- ``:follow-selected``
- ``:debug-clear-ssl-errors``
- Loading of marks
- Loading of sessions
- ``:debug-webaction``
- ``:inspect``
- ``:view-source``
- Passing through keys to a website

13 tests still fail:

- downloads

  - ``test_downloading_as_mhtml_is_available``
  - ``test_downloading_as_mhtml_with_nonascii_headers``
  - ``test_cancelling_a_mhtml_download_issue_1535``

- editor

  - ``test_spawning_an_editor_successfully``

- scroll

  - ``test_scrollpage_with_a_very_big_value``

- spawn

  - ``test_starting_a_userscript_which_doesnt_exist``
  - ``test_running_spawn_with_userscript``

- tabs

  - ``test_buffer_with_a_matching_title``

- yankpaste

  - ``test_pasting_the_primary_selection_into_an_empty_text_field``
  - ``test_pasting_the_primary_selection_into_a_text_field_at_specific_position``
  - ``test_pasting_the_primary_selection_into_a_text_field_with_undo``
  - ``test_pasting_the_primary_selection_without_a_focused_field``
  - ``test_pasting_the_primary_selection_with_a_readonly_field``

The ``scroll`` and ``tabs`` ones should be trivial fixes. For ``downloads``,
``editor``, ``spawn`` and ``yankpaste`` some more work and extending the API
will probably be needed.

I also started implementing the existing API for QtWebEngine - unfortunately
API to get the scroll position from a ``QWebEngineView`` was only implemented
in Qt 5.7, and the current PyQt 5.6 doesn't wrap that yet.

There's also no API to scroll the page - I tried emulating key presses like I
did with QtWebKit, but for some reason that did nothing at all...
