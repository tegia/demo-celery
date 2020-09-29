import os
import time
from celery import Celery
import requests
import json
from kombu import Queue
env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

celery.conf.result_backend = CELERY_RESULT_BACKEND
celery.conf.broker_url = CELERY_BROKER_URL

celery.conf.task_default_queue = "b-medium"

celery.conf.task_create_missing_queues = True

#app.conf.task_default_priority = 3

celery.conf.broker_transport_options = {"queue_order_strategy": "sorted"}

# celery.conf.worker_prefetch_multiplier = 1

celery.conf.task_inherit_parent_priority = True

#app.conf.broker_transport_options = {
#    'priority_steps': list(range(10)),
#}

celery.conf.task_queues = (
    Queue("a-high"),
    Queue("b-medium"),
    Queue("c-low"),
)

celery.conf.task_routes = {
    f'tasks.low_priority_wait': {
        'queue': 'c-low',
        'routing_key': 'c-low.priority',
    },
    f'tasks.high_priority_wait': {
        'queue': 'a-high',
        'routing_key': 'a-high.priority',
    },
}

@celery.task(name='mytasks.add')
def add(x, y):
    # time.sleep(5) # lets sleep for a while before doing the gigantic addition task!
    print(''+str(x)+'-'+str(y))
    return x+y
    # raise Exception("Sorry, no numbers below zero")

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

# celery.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'mytasks.find_task_fail',
#         'schedule': 30.0
#     },
# }

celery.conf.timezone = 'UTC'