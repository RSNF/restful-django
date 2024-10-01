from django.db import models
from .DroneCategory import DroneCategory

class Drone(models.Model):
    name = models.CharField(max_length=250, unique=True)
    drone_category = models.ForeignKey(DroneCategory, related_name="drones", on_delete=models.CASCADE)
    manufacturing_date = models.DateField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
