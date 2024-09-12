from rest_framework import viewsets
from drones.models import Competition
from drones.serializers import CompetitionSerializer

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
