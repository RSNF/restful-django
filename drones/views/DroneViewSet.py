from rest_framework import viewsets, filters
from django_filters import rest_framework
from drones.models import Drone
from drones.serializers import DroneSerializer

class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    filterset_fields = (
        "drone_category",
        "has_it_competed"
    )

    search_fields = ("^name",)

    ordering_fields = (
        "name",
        "manufacturing_date",
    )
