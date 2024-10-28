from django.db import models
from .Pilot import Pilot
from .Drone import Drone


class Competition(models.Model):
    pilot = models.ForeignKey(
        Pilot, related_name="competitions", on_delete=models.CASCADE
    )
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-distance_in_feet",)
