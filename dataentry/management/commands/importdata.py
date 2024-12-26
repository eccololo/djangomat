from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from dataentry.utils import check_csv_errors
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

        model = check_csv_errors(csv_filepath, model_name)

        with open(csv_filepath, "r") as file:
            reader = csv.DictReader(file)
            unique_field = reader.fieldnames[0]

            for data in reader:
                unique_value = data[unique_field]
                record_exists = model.objects.filter(**{unique_field: unique_value}).exists()

                if not record_exists:
                    # Filtering only string keys.
                    data = {key: value for key, value in data.items() if isinstance(key, str)}

                    # Logging excluded keys from data dict.
                    non_str_keys = [key for key in data if not isinstance(key, str)]
                    if non_str_keys:
                        # TODO:
                        # 1. Add logging to log system of this below action.
                        print(f"Non-string keys were deleted: {non_str_keys}")

                    model.objects.create(**data)
                    self.stdout.write(self.style.SUCCESS(f"Added new record with {unique_field}={unique_value}"))
                else: 
                    self.stdout.write(self.style.WARNING(f"Record with {unique_field}={unique_value} already exists!"))

        self.stdout.write(self.style.SUCCESS("Data inserted from CSV file succesfully!"))