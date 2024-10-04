from rest_framework import viewsets
from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    search_fields = ["^nome"]
    ordering_fields = ["nome",]
