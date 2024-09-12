from rest_framework import serializers
from drones.models.Drone import Drone
from drones.models.DroneCategory import DroneCategory

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field="name")

    class Meta:
        model = Drone
        fields = (
            "url",
            "id",
            "name",
            "drone_category",
            "manufacturing_date",
            "has_it_completed",
            "inserted_timestamp",
        )
