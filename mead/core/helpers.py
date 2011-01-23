from mead import app
from flask import g
from flaskext.themes import static_file_url, render_theme_template, get_theme


@app.before_request
def get_my_theme():
	g.theme = get_theme('default')
	print g.theme.__dict__

#print app.theme_manager.themes
#print 'fuck'

#print get_theme('default')