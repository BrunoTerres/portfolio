from django.contrib import admin

from .models import DevIntro, ProgrammingLanguages, Technologies, Projects

admin.site.register(DevIntro)
admin.site.register(ProgrammingLanguages)
admin.site.register(Technologies)
admin.site.register(Projects)