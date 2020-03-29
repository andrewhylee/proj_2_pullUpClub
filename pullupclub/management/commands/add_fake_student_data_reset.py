
from django.core.management.base import BaseCommand
from django.core.management import call_command

from pullupclub.models import Student

""" Delete all student data then re-add fake students and pullup sessions
"""

class Command(BaseCommand):
    def handle(self, *args, **options):
        count = Student.objects.all().delete()
        print("students deleted", count)

        call_command("add_fake_student_data")
