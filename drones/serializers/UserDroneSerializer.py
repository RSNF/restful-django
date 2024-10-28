from rest_framework import serializers
from drones.models import Drone


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = ("url", "name")
