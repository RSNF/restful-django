from django.db import models


class DroneCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
