from rest_framework import serializers
from core.models import Colecao, Livro


class ColecaoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:colecoes-detail")
    livros = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Livro.objects.all(),
        view_name="core:livros-detail",
    )
    colecionador = serializers.ReadOnlyField(source="colecionador.username")

    class Meta:
        model = Colecao
        fields = "__all__"
