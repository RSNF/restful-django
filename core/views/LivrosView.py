from rest_framework import viewsets
from core.models import Livro
from core.serializers import LivroSerializer

class LivroView(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
