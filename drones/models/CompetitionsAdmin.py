from drones.models import Competition
from django.contrib import admin


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("pilot", "drone", "distance_in_feet", "distance_achievement_date")
    search_fields = ("pilot__name", "drone__name")
    list_filter = ("distance_achievement_date", "drone__drone_category")
    date_hierarchy = "distance_achievement_date"
    save_on_top = True

    fieldsets = (
        (
            "Selecionar Piloto e Drone",
            {
                "fields": (
                    "pilot",
                    "drone",
                )
            },
        ),
        (
            "Adicionar Detalhes da Competição",
            {
                "fields": (
                    "distance_in_feet",
                    "distance_achievement_date",
                )
            },
        ),
    )
