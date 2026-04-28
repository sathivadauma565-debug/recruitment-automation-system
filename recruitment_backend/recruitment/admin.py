from django.contrib import admin
from .models import Job, Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'score', 'status')

admin.site.register(Job)
admin.site.register(Application, ApplicationAdmin)