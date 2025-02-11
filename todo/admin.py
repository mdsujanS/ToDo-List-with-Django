from django.contrib import admin
from . import models 

# Register your models here.
@admin.register(models.Task)
class Taskadmin(admin.ModelAdmin):
    list_display=['title']