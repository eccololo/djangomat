from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "It prints the 'Hello World' text." # for --help flag.

    def handle(self, *args, **kwargs):
        # Here is the logic of our custom command.
        self.stdout.write("Hello World!")