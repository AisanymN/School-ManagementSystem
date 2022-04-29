from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Grade)