from django.core.management.base import BaseCommand
from dataentry.models import Student

# I want to add some data to the database using the custom command

class Command(BaseCommand):
    help = "It will insert data to the database"

    def handle(self, *args, **kwargs):
        # logic goes here
        # add one data 

        dataset = [
            {'roll_no':102, 'name': "Sahil", 'age' : 21},
            {'roll_no':106, 'name': "Deep", 'age' : 22},
            {'roll_no':104, 'name': "Chaitan", 'age' : 22},
            {'roll_no':105, 'name': "Sohan", 'age' : 22}
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])

            else:
                self.stdout.write(self.style.WARNING(f'student with roll no{roll_no} already esist ! '))

        self.stdout.write(self.style.SUCCESS('Data inserted Successfully ! '))
