from djangomat.celery import app as celery_app
from django.core.management import call_command
from django.conf import settings
from .utils import send_email_notification
import time

@celery_app.task
def celery_test_task():
    time.sleep(10)
    # Send test email
    subject = "Mateusz Hyla - Test Email"
    message = "This is test email send from Djangomat." 
    to_email = settings.DEFAULT_TO_EMAIL

    send_email_notification(subject, message, to_email)

    return "Task executed succesfully!"

@celery_app.task
def import_data_task(corrected_path, model_name):
    try:
        call_command("importdata", corrected_path, model_name)
    except Exception as e:
        raise e
    
    # Send notification email
    subject = "Djangomat.com - Success."
    message = "Your data has been imported succesfully." 
    to_email = settings.DEFAULT_TO_EMAIL

    send_email_notification(subject, message, to_email)

    return "Task Completed: Data imported succesfully!"