from rest_framework import viewsets
from core.models import Livro
from core.serializers import LivroSerializer
from core.filters import LivroFilter


class LivroView(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    filterset_class = LivroFilter
    search_fields = ["^titulo"]
    ordering_fields = ["titulo", "autor", "categoria", "publicado_em"]
