import os
from celery import Celery
import requests
import json
import time
env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='mytasks.add')
def add(x, y):
    time.sleep(1) # lets sleep for a while before doing the gigantic addition task!
    print(''+str(x)+'-'+str(y))
    # return x+y
    raise Exception("Sorry, no numbers below zero")

# return list_failed_task_id
@celery.task(name='mytasks.find_task_fail')
def find_task_fail():
    response = requests.get('http://0.0.0.0:5555/api/tasks?state=FAILURE')
    json_response = json.loads(response.text)
    failed_task_id = json_response.keys()
    list_task_id = []
    for task_id in failed_task_id: 
        list_task_id.append(task_id)
        # Retry task_id
        celery.send_task('mytasks.retry', task_id=task_id)
    
    if len(list_task_id) == 0:
        return 'No list failed task'
    else:
        return list_task_id

# return response of retry_task_fail
@celery.task(name='mytasks.retry')
def retry_task_fail():
    return 'retry success'