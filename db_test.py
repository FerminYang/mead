#!/usr/bin/env python
# -*- coding: utf-8 -*-


from mead import app
from mead.core.models.content import Page, db
# 
def add(x):

	db.session.add(x)
	db.session.commit()



app.test_request_context('/').push()

pages = Page.query.all()
print pages
# 
# for user in users:
# 	print user.username


	
if __name__ == '__main__':
#	# pass
#	db.create_all()
#
#	page = Page()
#	page.title = 'This is Mead'
#	page.title = 'LOREM IPSUM OMG'
#	page.type = 'page'
#
#	add(page)
#
#	add(page)
#	#
	pass