from rest_framework import viewsets
from core.models import Autor
from core.serializers import AutorSerializer

class AutorView(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
