import os
import time
from celery import Celery


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)



@celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    print(''+str(x)+'-'+str(y))
    return x + y

@celery.task(name='tasks.sendSMS')
def sendSMS(to: str, msg: str) ->str:
    print('send message '+msg)
    # logger.info('send message '+msg)
    import requests
    res = requests.get('http://google.com')
    # print(res)
    # logger.info(res)
    return res.text