#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Moiz Farooq'
SITENAME = 'Cella Digital'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Etc/GMT+5'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('Home', '#home-section'),
        ('About', '#about-section'),
        ('Services', '#services-section'),
        ('Contact', '#schedule-a-call-section'),
        )

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/celladigital'),
          ('instagram', 'https://www.instagram.com/celladigital/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/celladigital'

# LOAD_CONTENT_CACHE = False 

from datetime import date
# STARTYEAR = 2020
CURRENTYEAR = date.today().year