import os
import time
from celery import Celery
env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='mytasks.add')
def add(x, y):
    time.sleep(5) # lets sleep for a while before doing the gigantic addition task!
    print(''+str(x)+'-'+str(y))
    return x+y
    # raise Exception("Sorry, no numbers below zero")

celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'mytasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

celery.conf.timezone = 'UTC'