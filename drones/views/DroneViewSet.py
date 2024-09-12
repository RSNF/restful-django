from rest_framework import viewsets
from drones.models import Drone
from drones.serializers import DroneSerializer

class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
