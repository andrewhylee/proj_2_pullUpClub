
import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from pullupclub.utils import generate_student_slug
from pullupclub.models import Student, PullUpSession

""" add fake students and pullup sessions
"""

FAKE_NAMES = (
    "Stan Marsh", "Eric Cartman", "Kyle Broflowsky", "Kenny McCorrmick", "Randy Marsh",
    "Wendy Testiberger", "Mr Garrison", "Token Black", "Chef", "Towelie", "Santa Clause",
    "Butters Stotch",)

# no one should be able to do more in 1 session
MAX_PULLUPS_PER_SESSION = 45

def _fake_nickname_from_name(name: str) -> str:
    chars = [c for c in name if c != " "]
    random.shuffle(chars)
    return "".join(chars[:3]).upper()

def _true_or_false(probability_true=0.5):
    x = random.randint(1, 100)
    return (probability_true * 100) > x


class Command(BaseCommand):
    def handle(self, *args, **options):
        for name in FAKE_NAMES:
            # Create Student
            slug = generate_student_slug(name)
            nickname = _fake_nickname_from_name(name)
            student = Student.objects.create(
                name=name, slug=slug, nickname=nickname)
            print("created student", student)

            # Add pullups sessions over time
            now = timezone.now()
            current_time_pointer = now - timedelta(days=360)
            pullups_per_session = random.randint(0, 10)
            while current_time_pointer < now:

                if pullups_per_session < MAX_PULLUPS_PER_SESSION:
                    got_stronger = _true_or_false(probability_true=0.15)
                    if got_stronger:
                        pullups_per_session += 1

                # Add some variance. sometimes we can do more, sometimes less
                pullups_this_session = pullups_per_session + random.randint(-3, 1)
                pullups_this_session = max(0, pullups_this_session)

                pus = PullUpSession.objects.create(
                    student=student,
                    count=pullups_this_session)
                pus.time = current_time_pointer
                pus.save(update_fields=['time'])

                # Fast forward in time
                hours_to_advance = random.randint(3, 72)
                current_time_pointer = current_time_pointer + timedelta(hours=hours_to_advance)



