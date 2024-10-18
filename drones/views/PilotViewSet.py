from rest_framework import viewsets
from drones.models import Pilot
from drones.serializers import PilotSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

    filterset_fields = ("gender", "races_count")
    search_fields = ("^name",)
    ordering_fields = ("name", "races_count")

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
