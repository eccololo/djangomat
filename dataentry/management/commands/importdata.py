from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from django.db import DataError
import csv

class Command(BaseCommand):

    help = "Imports data from CSV file to DB."

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help="Path to a CSV file.")
        parser.add_argument('model_name', type=str, help="Name of the model.")

    def handle(self, *args, **kwaregs):
        # Custom command logic.
        csv_filepath = kwaregs["filepath"]
        model_name = kwaregs["model_name"].capitalize()
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
        

        with open(csv_filepath, "r") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                raise CommandError("CSV file is empty or missing headers!")
            
            unique_field = reader.fieldnames[0]
            field_names = [field.name for field in model._meta.get_fields()]

            if unique_field not in field_names:
                raise DataError(f"Fields from CVS file does not match with fields in model '{model_name}'!")

            for data in reader:
                unique_value = data[unique_field]
                record_exists = model.objects.filter(**{unique_field: unique_value}).exists()

                if not record_exists:
                    model.objects.create(**data)
                    self.stdout.write(self.style.SUCCESS(f"Added new record with {unique_field}={unique_value}"))
                else: 
                    self.stdout.write(self.style.WARNING(f"Record with {unique_field}={unique_value} already exists!"))

        self.stdout.write(self.style.SUCCESS("Data inserted from CSV file succesfully!"))