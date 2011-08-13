from flask import (
        request, session, redirect, url_for,
        abort, render_template, flash, g
)
from flaskext.themes import render_theme_template, get_theme, get_themes_list

from mead import app
from mead.core.models.content import Page

from available import defaults

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


@app.route('/<pagetype>/id/<int:pageref>')
def get_page_by_id(pagetype, pageref):
    """Receives Application Metrics transmissions."""
    page = Page.query.filter_by(type=pagetype, id=pageref).first_or_404()

    return render_theme_template(g.theme, 'page.html',
    page=page,
    **defaults
    )

@app.route('/<pagetype>/<pageslug>')
def get_page_by_slug(pagetype, pageref):
    """Receives Application Metrics transmissions."""
    page = Page.query.filter_by(type=pagetype, id=pageref).first_or_404()

    return render_theme_template(g.theme, 'page.html',
    page=page,
    **defaults
    )
