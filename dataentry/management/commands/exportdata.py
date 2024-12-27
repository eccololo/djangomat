from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
from django.apps import apps
from dataentry.utils import generate_csv_filepath
import csv

# Command - python manage.py exportdata <model_name>

class Command(BaseCommand):

    help = "Exports data from database to CSV file."

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="Name of the model.")

    def handle(self, *args, **kwaregs):
        # Custom command logic.
        
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
        

        # Converting file name to with timestamp.
        filepath = generate_csv_filepath(model_name)

        data = model.objects.all()
   

        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)

            # Write the header
            writer.writerow([field.name for field in model._meta.get_fields()])

            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS("Data exported succesfully!"))
