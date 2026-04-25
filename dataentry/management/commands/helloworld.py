from django.core.management.base import BaseCommand  # type: ignore


class Command(BaseCommand):
    help = "Prints Hello Worlds"

    def handle(self, *args, **kwargs):
        # we write a logic
        self.stdout.write("Hello  World")
