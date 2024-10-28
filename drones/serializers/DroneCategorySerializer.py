from rest_framework import serializers
from drones.models.DroneCategory import DroneCategory


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="drones:dronecategory-detail")
    drones = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="drones:drones-detail"
    )

    class Meta:
        model = DroneCategory
        fields = (
            "url",
            "id",
            "name",
            "drones",
        )
