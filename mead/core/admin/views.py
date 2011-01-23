from flask import (
	request, session, redirect, url_for,
	abort, render_template, flash, Flask
)


from mead import app

from mead.core.models import auth, content, meta


#@app.route('/', methods=['GET'])
#def hello_world():
#	"""Lists all All Tests (for now)"""
#	tests = Test.query.all()
#	metrics = AppMetric.query.all()
#	metric_logs = AppMetricLog.query.all()
#	migrations = Migration.query.all()
#	migration_logs = MigrationLog.query.all()
#
#	return render_template('test.html',
#		tests=tests, metrics=metrics, metric_logs=metric_logs,
#		migrations=migrations, migration_logs=migration_logs,
#		config=app.config
#	)
