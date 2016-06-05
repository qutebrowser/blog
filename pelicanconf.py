#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Florian Bruhin'
SITENAME = 'qutebrowser development blog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['thumbnailer']
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images'
THUMBNAIL_SIZES = {'small': '200x?'}

THEME = './pelican-themes/monospace'
DESCRIPTION = ('Daily(-ish) blog for the '
               '<a href="http://igg.me/at/qutebrowser">qutebrowser '
               'QtWebEngine crowdfunding</a>.<br/><br/>'
               '<a href="http://www.qutebrowser.org/">website</a><br/>'
               '<a href="https://github.com/The-Compiler/qutebrowser">GitHub'
               '</a><br/>feeds: <a href="feeds/all.atom.xml">atom</a> / '
               '<a href="feeds/all.rss.xml">rss</a>')

SITEURL = 'http://blog.qutebrowser.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = ''

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
