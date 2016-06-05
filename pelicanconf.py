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
               '<br/>feeds: <a href="feeds/all.atom.xml">atom</a> / '
               '<a href="feeds/all.rss.xml">rss</a>')

SITEURL = 'http://blog.qutebrowser.org'
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

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

DEFAULT_CATEGORY = ''

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
