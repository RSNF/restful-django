from rest_framework import viewsets
from drones.models import DroneCategory
from drones.serializers import DroneCategorySerializer


class DroneCategoryViewSet(viewsets.ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer

    search_fields = ("^name",)
    ordering_fields = ("name",)
