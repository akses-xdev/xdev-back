from django.contrib import admin

from apps.teams.models import Role, Technology, Employee

admin.site.register(Role)
admin.site.register(Technology)
admin.site.register(Employee)