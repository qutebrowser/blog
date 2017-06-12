##########
First week
##########

:category: config

Phew, days 3, 4 and 5 are over already, and it's more than time for another
update! Lots of code in this one... ;-)

*********
Wednesday
*********

On Wednesday, I took a closer look at the `completion refactoring`_ pull request
and some sqlite performance issues it had. 

I was able to get the performance up to an acceptable level (comparable to the
current completion, but without a web history limit, i.e. searching the full
history) by creating some `SQL indices`_ on the table, and `splitting`_ the
table into two so it looks more like how the data is actually displayed in the
completion. I also needed to add a `cache`_ for QtWebKit's ``historyContains``
(used to color visited links) because for some reason it asked for the same
thing dozens of times in a row...

After that, I did a complete `review`_ of that pull request. Unfortunately it
grow quite big, so the review also took a fair amount of time...

I originally planned to get it merged before starting the config work, but that
made me realize that's not feasible. However, only relatively little config code
is impacted by it, so it seems reasonable to let rcorre (the contributor doing
that PR) work in parallel on that while I'm working on the config.

.. _completion refactoring: https://github.com/qutebrowser/qutebrowser/pull/2295
.. _SQL indices: https://github.com/rcorre/qutebrowser/commit/1e016cd4404df642a87d2855621a1178a9fc1046
.. _splitting: https://github.com/rcorre/qutebrowser/compare/0e6b9b46b0243eaf7fee28b17d43bc5c56632993~2...rcorre:0e6b9b46b0243eaf7fee28b17d43bc5c56632993
.. _cache: https://github.com/rcorre/qutebrowser/commit/939d2823ed3c191303d04a965cc43e3728ab819f
.. _review: https://github.com/qutebrowser/qutebrowser/pull/2295#pullrequestreview-42646196

********
Thursday
********

Yesterday morning I was mostly busy with finishing some work related to the
contribution above. After that, I tried updating my `debug Qt packages`_ for
Qt 5.9 which was `recently released`_, but unfortunately ran into some issues
with building them...

After that, I started branching off to a ``new-config`` branch - with that, the
real work (and breaking everything) could begin.

I started with stubbing out all the old config code, `replacing it`_ by a simple
object which only returns the default settings.

It essentially boils down to this:

.. code-block:: python

    class SectionStub:
    
        def __init__(self, conf, name):
            self._conf = conf
            self._name = name
    
        def __getitem__(self, item):
            return self._conf.get(self._name, item)
    
    
    class NewConfigManager(QObject):
    
        changed = pyqtSignal(str, str)
    
        def __init__(self, parent=None):
            super().__init__(parent)
            self._values = {}
    
        def _key(self, sect, opt):
            return sect + ' -> ' + opt
    
        def read_defaults(self):
            for name, section in configdata.data().items():
                for key, value in section.items():
                    self._values[self._key(name, key)] = value
    
        def get(self, section, option):
            val = self._values[self._key(section, option)]
            return val.typ.transform(val.value())               

It only provides the default config values to the rest of the code and various
stuff (like typing ``:set``) crashes, but it's a great foundation to build the
new config code upon, and much of the old code is deactivated with that.

Next, I converted the old ``configdata.py`` file to a YAML file, as it was very
cumbersome to edit before. The ``configdata`` file contains the definitions of
all available qutebrowser settings, with their types, default values and
description.

This is an example of how it looked:

.. code-block:: python

   ('log-javascript-console',
     SettingValue(typ.String(
         valid_values=typ.ValidValues(
             ('none', "Don't log messages."),
             ('debug', "Log messages with debug level."),
             ('info', "Log messages with info level.")
         )), 'debug'),
     "How to log javascript console messages."),

And this is how the same definition looks in the YAML file, in a more
declarative style:

.. code-block:: yaml

    log_javascript_console:
      type:
        name: String
        valid_values:
          - none: "Don't log messages."
          - debug: "Log messages with debug level."
          - info: "Log messages with info level."
      default: debug
      desc: "How to log javascript console messages."

I hope you agree that this is much more readable and maintainable!

Getting it into that format involved a little bit of automation:

.. code-block:: python

    import yaml
    import collections
    
    from qutebrowser.config import configdata, configtypes
    
    data = configdata.data()
    for sectname, sect in data.items():
        print()
        print("# {}".format(sectname))
        print()
        for optname, opt in sect.items():
            data = {}
    
            if optname in sect.descriptions:
                data['desc'] = sect.descriptions[optname]
    
            if isinstance(opt.typ, configtypes.Bool):
                data['type'] = opt.typ.__class__.__name__
            else:
                data['type'] = {'name': opt.typ.__class__.__name__}
                if opt.typ.valid_values:
                    vv = data['type']['valid_values'] = []
                    typ_vv = opt.typ.valid_values
                    for val in typ_vv:
                        desc = typ_vv.descriptions.get(val)
                        if desc:
                            vv.append({val: desc})
                        else:
                            vv.append(val)
    
            data['default'] = opt.typ.transform(opt.default())
    
            if sectname in ['colors', 'fonts']:
                new_optname = (sectname + '.' +
                               optname.replace('-', '_'))
            else:
                new_optname = optname.replace('-', '_')
    
            print(yaml.dump({new_optname: data},
                            default_flow_style=False))

but still required a lot of tedious manual work. Worth it, though!

.. _debug Qt packages: https://github.com/qutebrowser/qt-debug-pkgbuild/blob/master/README.md
.. _recently released: http://blog.qt.io/blog/2017/05/31/qt-5-9-released/
.. _replacing it: https://github.com/qutebrowser/qutebrowser/commit/3385fe1560409a9125e5ea8713c17dac304bc0ce

******
Friday
******

Today, I continued working on the ``configdata.yml`` file - I cleaned up various
mistakes and wrote the `loading code`_ to actually read that file.

Then I started a `first renaming`_ of config options (as this will be a breaking
config change, now is the time!) to make things clearer and more consistent.

I also opened `an issue`_ to solicit some more feedback about what should be
renamed and how - **please participate**!

I originally thought it wouldn't be possible to have a setting like
``colors.statusbar.bg`` and then another one which has the same "base", like
``colors.statusbar.bg.private`` - because if you did something like
``conf.colors.statusbar.bg = 'black'`` in Python,
``colors.statusbar.bg.private`` would try to access ``.private`` on the string
``'black'``.

However, a small proof of concept (with lots of Python magic) shows that it's
actually possible:

.. code-block:: python

      class ConfigContainer:

          def __init__(self, handler, prefix=''):
              self._handler = handler
              self._prefix = prefix

          def __repr__(self):
              return ('ConfigContainer(handler={!r}, prefix={!r})'
                      .format(self._handler, self._prefix))

          def __getattr__(self, attr):
              return ConfigContainer(handler=self._handler,
                                     prefix=self._join(attr))

          def __setattr__(self, attr, value):
              if attr.startswith('_'):
                  return super().__setattr__(attr, value)
              self._handler(self._join(attr), value)

          def _join(self, attr):
              if self._prefix:
                  return '{}.{}'.format(self._prefix, attr)
              else:
                  return attr


      conf = ConfigContainer(print)
      conf.foo.bar.baz.fish = 42
      conf.foo.bar.baz = 23
      print(conf.foo.bar.baz.fish)


That won't make it possible to retrieve values from the config, though - the last line will print
``ConfigContainer(handler=<built-in function print>, prefix='foo.bar.baz.fish')``.

I'm not sure yet whether I like that. It'd be possible to get the value by calling the object
(``conf.foo.bar.baz()``) but that doesn't seem very intuitive either, especially
if the same thing is going to be used in the plugin API later. I'll have to
think some more about it.

.. _loading code: https://github.com/qutebrowser/qutebrowser/blob/9fdc494373406732556cb2a6559c15e6dde51567/qutebrowser/config/configdata.py#L527
.. _first renaming: https://github.com/qutebrowser/qutebrowser/commit/adba5dba301d0cba1507b92e4985b4b426f72724
.. _an issue: https://github.com/qutebrowser/qutebrowser/issues/2708
