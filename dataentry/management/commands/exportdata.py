from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
import csv
import os
import datetime

class Command(BaseCommand):

    help = "Exports data from Student model to CSV file."

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help="Name of CSV file.")

    def handle(self, *args, **kwaregs):
        # Custom command logic.
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = kwaregs["filename"]
        if ".csv" in filename:
            parts = filename.split(".")
            filename = f"{parts[0]}-{timestamp}-{parts[1]}"
        else:
            raise CommandError("File must be a CSV file.")

        students = Student.objects.all()
        filepath = os.path.join(os.getcwd(), "datasets", filename)

        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)

            # Write the header
            writer.writerow(["Roll No", "Name", "Age"])

            for student in students:
                writer.writerow([student.roll_no, student.name, student.age])

        self.stdout.write(self.style.SUCCESS("Data exported succesfully!"))
