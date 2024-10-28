from rest_framework import viewsets
from drones.models import Drone
from drones.serializers import DroneSerializer
from rest_framework import permissions
from drones import custom_permissions
from rest_framework.throttling import ScopedRateThrottle

class DroneViewSet(viewsets.ModelViewSet):
    throttle_scope = "drones"
    throttle_classes = (ScopedRateThrottle,)

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

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
