from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):

    help = "It insert data to database."

    def handle(self, *args, **kwargs):
        # Custom method logic.

        dataset = [
            { 
                "roll_no": 1010, 
                "name": "Jack", 
                "age": 33
            },
            { 
                "roll_no": 1020, 
                "name": "Kate", 
                "age": 35
            },
            { 
                "roll_no": 1030, 
                "name": "Hugo", 
                "age": 27
            },
            { 
                "roll_no": 1040, 
                "name": "Sawyer", 
                "age": 37
            },
            { 
                "roll_no": 1050, 
                "name": "Sun", 
                "age": 22
            }
        ]

        for data in dataset:
            roll_no = data["roll_no"]
            record_exists = Student.objects.filter(roll_no=roll_no).exists()
            if not record_exists:
                Student.objects.create(roll_no=roll_no, name=data["name"], age=data["age"])
            else: 
                self.stdout.write(self.style.WARNING(f"Student with roll_no {roll_no} already exists in DB!"))

        self.stdout.write(self.style.SUCCESS("Data inserted succesfully!"))