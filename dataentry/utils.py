from django.apps import apps
from django.core.management.base import CommandError
from django.core.mail import EmailMessage
from django.conf import settings
from emails.models import Email, Sent
import csv
import datetime
import os

def get_all_custom_models():
    """This function returns all custom models in Django project."""
    custom_models = set()
    all_models = set()
    # Default models from Django installation. If a new model will be added it should be added to this list.
    # YOu can add "User" model to this list to prevent from importing user data to DB.
    default_models = {"LogEntry", "Permission", "Group", "ContentType", "Session", "Upload", "User"}

    for model in apps.get_models():
        all_models.add(model.__name__)

    custom_models = all_models - default_models
    custom_models = list(custom_models)

    return sorted(custom_models)


def check_csv_errors(file_path, model_name):
    """This function checks for errors associated with CSV file like correct headers and others."""
    model = None

     # Search for model across all installed apps.
    for app_config in apps.get_app_configs():
        try:
            model = apps.get_model(app_config.label, model_name)
            break # model found 
        except LookupError:
            continue # model not found, continue searching.

    if not model:
        raise CommandError(f"Model '{model_name}' not found in any app!")
    
    # Get field names from model (excluding 'id')
    field_names = [field.name for field in model._meta.get_fields() if field.name != 'id']
    
    reader = None

    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            # Check if all CSV fields are present in the model
            missing_fields = [field for field in reader.fieldnames if field not in field_names]
            if missing_fields:
                raise CommandError(f"CSV file contains fields that are not in model '{model_name}': {', '.join(missing_fields)}")

            if not reader.fieldnames:
                raise CommandError("CSV file is empty or missing headers!")
            
            unique_field = reader.fieldnames[0]

            if unique_field not in field_names:
                raise CommandError(f"CSV's unique field '{unique_field}' does not exist in model '{model_name}'!")
    except Exception as e:
        # Handle file read errors and other exceptions
        if reader is None:
            raise CommandError("Failed to read CSV file or file is empty!")
        raise CommandError(f"Error processing CSV file: {e}")
    
    return model


def send_email_notification(subject, message, to_email, attachment=None, email_id=None):
    """This function sends email notification to recepient."""
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(subject, message, from_email, to=to_email)

        if attachment is not None:
            mail.attach_file(attachment)

        # HTML email content will be rendered properly in mailbox.
        mail.content_subtype = "html"
        mail.send()

        # Store total sent email in Sent model.
        email = Email.objects.get(pk=email_id)
        sent = Sent()
        sent.email = email
        sent.total_sent = email.email_list.count_emails()
        sent.save()
        
    except Exception as e:
        raise e



def generate_csv_filepath(model_name):
    """This function returns proper CSV filename."""

    timestamp = datetime.datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
    filename = f"exported-{model_name.lower()}-{timestamp}.csv"
    export_dir = "exports"
    filepath = os.path.join(settings.MEDIA_ROOT, export_dir, filename)

    return filepath
