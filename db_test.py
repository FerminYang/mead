#!/usr/bin/env python
# -*- coding: utf-8 -*-


from mead import app
from mead.core.models.content import Page, db
#
def add(x):

    db.session.add(x)
    db.session.commit()



#app.test_request_context('/').push()
#
#pages = Page.query.all()
#print pages
##
# for user in users:
#       print user.username

db.create_all()

if __name__ == '__main__':
#       # pass


    page = Page()
    page.title = 'This is Mead'
    page.content = 'LOREM IPSUM OMG'
    page.type = 'page'

    add(page)
#       #
    pass
