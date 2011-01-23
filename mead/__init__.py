#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    mead.core
    ~~~~~~~~~~~~

    Mead's core. The Honey.

    :copyright: (c) 2011 Kenneth Reitz
    :license: ISC
    :developer: Kenneth Reit

"""


from flask import Flask

app = Flask(__name__)

# =============
# CONFIGURATION
# =============

# Load Mead defaults.
app.config.from_object('mead.core.defaults')


try:
	app.config.from_envvar('MEAD_SETTINGS') # Change if you have multiple instances.
except RuntimeError:
	pass


try:
	# Load from local environment.
	app.config.from_pyfile('local_config.py')
except RuntimeError:
	pass


# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE']
del app.config['DATABASE']


# =====
# VIEWS
# =====

import mead.core.views.content
import mead.core.admin.views

if __name__ == '__main__':
	app.run()
