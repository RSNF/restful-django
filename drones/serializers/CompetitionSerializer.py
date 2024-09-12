from rest_framework import serializers
from drones.models import Competition
from .DroneSerializer import DroneSerializer

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer

    class Meta:
        model = Competition
        fields = (
            "url",
            "id",
            "distance_in_feet",
            "distance_achievement_date",
            "inserted_timestamp",
            "drone",
            "pilot"
        )
