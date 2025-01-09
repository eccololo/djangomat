from djangomat.celery import app as celery_app
from dataentry.utils import send_email_notification

@celery_app.task
def send_email_task(subject, message, to_email, attachment, email_id):
    send_email_notification(subject, message, to_email, attachment, email_id)
    return "Emails sent succesfully!"