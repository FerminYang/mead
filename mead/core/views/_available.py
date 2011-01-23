from flask import url_for
from mead import app

from mead.core.models.content import Page, Post

app.test_request_context('/').push()

defaults = dict(
	site_title = app.config['SITE_TITLE'],
	site_root_url = '/',
	static_url = app.config['THEME'],
	pages = Page.query.all()

#	url_for('.themes/', filename='style.css')
)


