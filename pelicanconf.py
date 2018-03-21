#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General Settings

AUTHOR = 'Dan'
SITENAME = 'danielmichaels'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/ACT'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About Me', '#'),('Projects', '#'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('github', 'danielmichaels'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Save As Settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'

# Themes and Plugins

THEME = 'add-ons/themes/taman'
TAGLINE = 'Technocrat, Aspiring Developer, Thinker, Practitioner of Shosin.' # Taman theme specific
PLUGIN_PATHS = ['add-ons/plugins']
PLUGINS = ['assets']

# Static and Extra Paths

STATIC_PATHS = [
        'images',
        'extra/favicon.ico',
        'extra/cover.jpeg'
        ]
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path':'favicon.ico'},
        'extra/cover.jpeg': {'path':'cover.jpeg'}
        }

USER_FAVICON_URL = '/favicon.ico'
USER_LOGO_URL = '/cover.jpeg'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
