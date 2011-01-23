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

import os

from flask import Flask
from werkzeug import cached_property
from jinja2 import ChoiceLoader, FileSystemLoader


class MeadFlask(Flask):
	""" Enhanced Flask class for smart mead template loading
	"""
	@cached_property
	def jinja_loader(self):
		return ChoiceLoader([
			super(MeadFlask, self).jinja_loader,
			FileSystemLoader('/Users/kreitz/repos/public/mead/mead/themes/default/'),
			FileSystemLoader('core/admin/templates/'),

		])

	def set_theme(self, theme_name):

#		def load(loader):
#			return loader
#
#		loader =  ChoiceLoader([
#			FileSystemLoader('themes/%s/' % (theme_name)),
#			FileSystemLoader('core/admin/templates/'),
#			super(MeadFlask, self).jinja_loader,
#		])
		pass


app = MeadFlask(__name__)

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


# Debug?
#if os.uname()[1] in app.config['DEBUG_HOSTS']:
if 1:
	app.config.debug = True


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
