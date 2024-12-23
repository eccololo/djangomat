from djangomat.celery import app as celery_app
import time

@celery_app.task
def celery_test_task():
    time.sleep(10)
    return "Task executed succesfully!"