from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, default="Sam Doe")
    nickname = models.CharField(max_length=10, default="Anonymous")
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class PullUpSession(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_of_pullups = models.IntegerField()
    def __str__(self):
        return ("No. " + str(self.pk))