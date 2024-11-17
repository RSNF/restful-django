from rest_framework import viewsets
from drones.models import Competition
from drones.serializers import CompetitionSerializer
from drones.filters import CompetitionFilter
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Competition"])
class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    filterset_class = CompetitionFilter
    ordering_field = (
        "distance_in_feet",
        "distance_achievement_date",
    )
