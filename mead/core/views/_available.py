from flask import url_for
from mead import app

defaults = dict(
	site_title = app.config['SITE_TITLE'],
	site_root_url = '/',
	static_url = app.config['THEME']
#	url_for('.themes/', filename='style.css')
)


