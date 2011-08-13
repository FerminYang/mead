from mead import app
from flask import g
from flaskext.themes import get_theme

import re


@app.before_request
def get_my_theme():
    g.theme = get_theme(app.config['THEME'])


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))
