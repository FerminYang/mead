from flaskext.sqlalchemy import SQLAlchemy
from mead import app

__version__ = '0.0.0'

db = SQLAlchemy(app)


class Test(db.Model):
	"""The :class:`Test` object is a test of the app structure.
	"""
	__tablename__ = 'tests'

	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Text)

	def __init__(self, value):
		self.value = value

	def __repr__(self):
		return '<Test #%r>' % self.id


# meta class page
# meta class post