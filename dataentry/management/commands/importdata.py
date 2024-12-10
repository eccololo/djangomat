from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv

class Command(BaseCommand):

    help = "Imports data from CSV file to DB."

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help="Path to a CSV file.")

    def handle(self, *args, **kwaregs):
        # Custom command logic.
        csv_filepath = kwaregs["filepath"]
        
        with open(csv_filepath, "r") as file:
            reader = csv.DictReader(file)
            for data in reader:
                roll_no = data["roll_no"]
                record_exists = Student.objects.filter(roll_no=roll_no).exists()
                if not record_exists:
                    Student.objects.create(**data)
                else: 
                    self.stdout.write(self.style.WARNING(f"Student with roll_no {roll_no} already exists in DB!"))

        self.stdout.write(self.style.SUCCESS("Data inserted from CSV file succesfully!"))