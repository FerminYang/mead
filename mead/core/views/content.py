from flask import (
	request, session, redirect, url_for,
	abort, render_template, flash
)


from mead import app

from _available import defaults

from mead.core.models import (
	auth, content, meta
)



THEME = app.config['THEME']

@app.route('/', methods=['GET'])
def index():
	"""Receives Application Metrics transmissions."""
	return render_template('%s/index.html' % THEME,
	**defaults
	)

