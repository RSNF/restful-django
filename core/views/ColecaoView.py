from rest_framework import viewsets
from core.models import Colecao
from core.serializers import ColecaoSerializer
from rest_framework import permissions
from core import custom_permissions


class ColecaoView(viewsets.ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer

    search_fields = "^nome"
    ordering_fields = ("nome", "descricao", "livros", "colecionador")

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserCollectorOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)
