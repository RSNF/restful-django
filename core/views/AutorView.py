from rest_framework import viewsets
from core.models import Autor
from core.serializers import AutorSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Autor"])
class AutorView(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    search_fields = ["^nome"]
    ordering_fields = [
        "nome",
    ]
