from django.apps import apps
from django.core.management.base import CommandError
from django.db import DataError
import csv

def get_all_custom_models():
    """This function returns all custom models in Django project."""
    custom_models = set()
    all_models = set()
    # Default models from Django installation. If a new model will be added it should be added to this list.
    # YOu can add "User" model to this list to prevent from importing user data to DB.
    default_models = {"LogEntry", "Permission", "Group", "ContentType", "Session", "Upload"}

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