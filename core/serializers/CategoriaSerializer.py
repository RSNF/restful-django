from rest_framework import serializers
from core.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:categorias-detail")

    class Meta:
        model = Categoria
        fields = "__all__"
