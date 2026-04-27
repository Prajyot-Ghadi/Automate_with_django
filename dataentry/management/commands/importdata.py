from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

# proposed command = python manage.py importdata file_path model_name


class Command(BaseCommand):
    help = "Import data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the CSV file")
        parser.add_argument("model_name", type=str, help="Name of the model")

    def handle(self, *args, **kwargs):
        # logic goes here

        file_path = kwargs["file_path"]
        model_name= kwargs['model_name']



        # Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # Try to search for the model 
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue  # model is not found in this app, continue ssearching in next app.

        
        if not model:
            raise CommandError(f"Model {model_name} is not found in any app")
        

        # Open CSV safely
        try:
            file = open(file_path, "r")
        except FileNotFoundError:
            raise CommandError(f"File '{file_path}' not found")


        reader = csv.DictReader(file)     #maps the information in a CSV file into a dictionary

        count = 0
        for row in reader:
            try:
                model.objects.create(**row)
                count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error in row {row}: {e}"))

            file.close()

            self.stdout.write(self.style.SUCCESS(f"{count} records imported successfully!"))