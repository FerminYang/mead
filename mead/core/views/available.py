from sqlalchemy.exc import OperationalError
#from flask import url_for
from flaskext.sqlalchemy import SQLAlchemy

from mead import app
from mead.core.models.content import Page


app.test_request_context('/').push()

db = SQLAlchemy()

defaults = dict(
        site_title = app.config['SITE_TITLE'],
        site_root_url = '/',
        static_url = app.config['THEME'],
#       url_for('.themes/', filename='style.css')
)


try:
    defaults.update(dict(pages = Page.query.all()))
except OperationalError:
    db.create_all()
