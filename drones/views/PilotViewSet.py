from rest_framework import viewsets
from drones.models import Pilot
from drones.serializers import PilotSerializer

class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
