from rest_framework import viewsets
from core.models import Categoria
from core.serializers import CategoriaSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categoria"])
class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    search_fields = ["^nome"]
    ordering_fields = [
        "nome",
    ]
