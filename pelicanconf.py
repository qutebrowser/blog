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
               'QtWebEngine crowdfunding</a>.</br></br>'
               '<a href="http://www.qutebrowser.org/">qutebrowser website</a>'
               '<br/><a href="feeds/all.atom.xml">atom feed</a>')

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'devlog'
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
