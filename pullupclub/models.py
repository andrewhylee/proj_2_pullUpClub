from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, default="Sam Doe")
    nickname = models.CharField(max_length=10, default="Anonymous")
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class PullUpSession(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return ("No. " + str(self.pk))

class Award(models.Model):
    TYPE = (
        ('BD', 'By Distance'),
        ('BC', 'By Count'),
    )
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=2, choices=TYPE)
    arm_length_inches = models.PositiveSmallIntegerField(default=0)
    threshold_to_achieve = models.PositiveSmallIntegerField(default=0)
    # Doesn't work --> if(type == 'BD'):
    distance_covered = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
