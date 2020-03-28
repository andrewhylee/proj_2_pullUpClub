from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=10)
    slug = models.SlugField(unique=True)


class PullUpSession(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_of_pullups = models.IntegerField()