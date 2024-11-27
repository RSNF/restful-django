from drones.models import DroneCategory
from django.contrib import admin


@admin.register(DroneCategory)
class DroneCategoryAdmin(admin.ModelAdmin):
    pass
