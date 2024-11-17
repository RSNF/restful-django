from rest_framework import viewsets
from drones.models import DroneCategory
from drones.serializers import DroneCategorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Drone Category"])
class DroneCategoryViewSet(viewsets.ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer

    search_fields = ("^name",)
    ordering_fields = ("name",)
