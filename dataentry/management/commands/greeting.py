from django.core.management.base import BaseCommand  # type: ignore


# Proposed command  = python manage.py greeting Name
# proposed output = Hi {Name} , Have a good day


class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Specifies user name")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        greeting = f"Hi {name}, Have a good day"
        self.stdout.write(self.style.SUCCESS(greeting))
