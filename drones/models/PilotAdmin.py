from drones.models import Pilot
from django.contrib import admin


@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    pass
