from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Qualification)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Project)