from django.contrib import admin
from .models import Student, PullUpSession, Award

# Register your models here.
admin.site.register(Student)
admin.site.register(PullUpSession)
admin.site.register(Award)

