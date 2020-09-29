import os
from flask import Flask
from flask import url_for
from worker import celery
from celery.result import AsyncResult
import celery.states as states
import uuid
import time

env=os.environ
app = Flask(__name__)

@app.route('/add/<int:param1>/<int:param2>/<param3>')
def add(param1,param2,param3):
    task = celery.send_task('mytasks.add', args=[param1, param2], kwargs={}, task_id=param3)
    return "<a href='{url}'>check status of {id} time add to queue </a>".format(id=task.id,
                url=url_for('check_task',id=task.id,_external=True))

@app.route('/check/<string:id>')
def check_task(id):
    res = celery.AsyncResult(id)
    if res.state==states.PENDING:
        return res.state
    else:
        return str(res.result)

