
from django.template.defaultfilters import slugify

from pullupclub.models import Student


def generate_student_slug(name: str) -> str:
    """ Given a student name, generate a unique slug for that student
    """

    slug = slugify(name)
    if not Student.objects.filter(slug=slug).exists():
        return slug

    # Duplicate found, add integer to end until it's unique
    counter = 1
    while True:
        modified_slug = f"{slug}-{counter}"
        if not Student.objects.filter(slug=modified_slug).exists():
            return modified_slug
        counter += 1
