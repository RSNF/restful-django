from rest_framework import viewsets
from drones.models import Pilot
from drones.serializers import PilotSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.throttling import ScopedRateThrottle
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Pilot"])
class PilotViewSet(viewsets.ModelViewSet):
    throttle_scope = "pilots"
    throttle_classes = (ScopedRateThrottle,)

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

    filterset_fields = ("gender", "races_count")
    search_fields = ("^name",)
    ordering_fields = ("name", "races_count")

    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
