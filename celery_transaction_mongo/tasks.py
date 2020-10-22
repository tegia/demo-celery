from operator import add
import os
from os import name
from threading import Lock
import time
from celery import Celery
import requests
import json
import celeryconfig
from pymongo import MongoClient
from random import randint
import logging
from logging.handlers import RotatingFileHandler

import stacktracer
import uuid
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('log/app.log', maxBytes=1024000*1024000, backupCount=2)
logger.addHandler(handler)

env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

client = MongoClient(env.get('MONGO_DB_NAME', 'localhost'), 27017
, username=env.get('MONGO_INITDB_ROOT_USERNAME', 'admin')
, password=env.get('MONGO_INITDB_ROOT_PASSWORD', 'admin'))
db = client['tutorial']
test_collection = db['test-collection']

celery.config_from_object(celeryconfig)

stacktracer.trace_start("trace.html")
lock=Lock()
@celery.task(name='mytasks.add')
def add_task(id, y):
    if id is None:
        id = 1
    temp_document = test_collection.find_one({"_id": id})
    random = randint(0, 1)
    if random == 1: 
        time.sleep(0.8)
    else:
        time.sleep(0.5)
    
    # if id == 1:
    #     temp_document = test_collection.find_one({"_id": id})
    #     if temp_document['count'] < 30:
    with lock:
        temp_document = test_collection.find_one({"_id": id})
        logger.info(temp_document)
        time.sleep(0.05)
        if temp_document['count'] < 30:
            currentCount = temp_document['count']
            temp_document['count'] = currentCount + 1
            test_collection.update_one({"_id": id}, {"$set": {"count": temp_document['count']}})
    # else:
    #     temp_document = test_collection.find_one({"_id": id})
    #     logger.info(temp_document)
    #     time.sleep(0.5)
    #     if temp_document['count'] < 30:
    #         currentCount = temp_document['count']
    #         temp_document['count'] = currentCount + 1
    #         test_collection.update_one({"_id": id}, {"$set": {"count": temp_document['count']}})
        # with client.start_session() as session:
        #     session.start_transaction()
        #     try:
        #         document = test_collection.find_one({"_id": id})
        #         currentCount = document['count']
        #         document['count'] = currentCount + 1
        #         test_collection.update_one({"_id": id}, {"$set": {"count": document['count']}})
        #         # session.commit_transaction()
        #         # session.endSession()
        #     except Exception as ex:
        #         logger.info(ex)
    return id

@celery.task(name='mytasks.periodic')
def periodic():
    add_task(1,2)
