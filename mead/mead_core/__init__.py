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

# CONFIGURATION
app.config.from_object('metrics.core.defaults')
try:
	# load from local environment.
	app.config.from_envvar('MEAD_SETTINGS')
except RuntimeError:
	pass

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE']
del app.config['DATABASE']

if __name__ == '__main__':
	app.run()
