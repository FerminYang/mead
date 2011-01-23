from flask import (
	request, session, redirect, url_for,
	abort, render_template, flash, g
)
from flaskext.themes import render_theme_template, get_theme, get_themes_list

from mead import app

from _available import defaults

from mead.core.models import (
	auth, content, meta
)


THEME = app.config['THEME']

@app.route('/')
def index():
	"""Receives Application Metrics transmissions."""
	return render_theme_template(g.theme, 'index.html',
	**defaults
	)

