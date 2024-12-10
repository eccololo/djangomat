from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):


    # Custom command --help text.
    help = "Greets the user with his or hers name."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Specifies user name.")

    def handle(self, *args, **kwargs):
        # Custom command logic.
        self.now_time = datetime.now().hour

        name = kwargs['name']

        if name is None:
            greeting = self.style.ERROR(f"Please give a name parameter to this custom command.")
        else:
            if self.now_time <= 12 and self.now_time >= 6:
                greeting = self.style.SUCCESS(f"Good morning, {name}.")
            elif self.now_time > 12 and self.now_time < 18:
                greeting = self.style.SUCCESS(f"Good afternoon, {name}.")
            else:
                greeting = self.style.SUCCESS(f"Good night, {name}.")

        self.stdout.write(greeting)