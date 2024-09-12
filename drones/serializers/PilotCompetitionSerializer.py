from rest_framework import serializers
from drones.models import Competition, Pilot, Drone

class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field="name")
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field="name")

    class Meta:
        model = Competition
        fields = (
            "url",
            "id",
            "distance_in_feet",
            "distance_achievement_date",
            "pilot",
            "drone"
        )
