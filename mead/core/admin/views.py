from flask import (
        request, session, redirect, url_for,
        abort, render_template, flash
)


from mead import app

from mead.core.models import auth, content, meta


#@app.route('/')
#@app.route('content/<content-type>/<content-ref>')
#@app.route('settings')

#@app.route('/', methods=['GET'])
#def hello_world():
#       """Lists all All Tests (for now)"""
#       pass
