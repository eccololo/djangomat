from djangomat.celery import app as celery_app
from django.core.management import call_command
import time

@celery_app.task
def celery_test_task():
    time.sleep(10)
    return "Task executed succesfully!"

@celery_app.task
def import_data_task(corrected_path, model_name):
    try:
        call_command("importdata", corrected_path, model_name)
    except Exception as e:
        raise e
    
    return "Data imported succesfully!"