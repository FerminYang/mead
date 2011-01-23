from flask import (
	request, session, redirect, url_for,
	abort, render_template, flash
)


from mead import app

from mead.core.models import (
	auth, content, meta
)


@app.route('/', methods=['GET'])
def index():
	"""Receives Application Metrics transmissions."""
	return render_template('index.html')


#@app.route('/', methods=['GET'])
#def hello_world():
#	"""Lists all All Content (for now)"""
#	tests = Content.query.all()


