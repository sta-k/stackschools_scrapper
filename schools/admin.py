from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import School,CeleryTasks, School2

admin.site.register(School)
admin.site.register(School2)
admin.site.register(CeleryTasks)