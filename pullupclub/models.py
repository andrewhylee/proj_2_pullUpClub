from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    age = models.IntegerField()
    pullUpCount = models.IntegerField()
    record_date = models.DateTimeField()
    slug = models.SlugField()