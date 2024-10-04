from rest_framework import serializers
from core.models import Categoria
from core.models import Autor
from core.models import Livro

class LivroSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:livros-detail")
    autor = serializers.SlugRelatedField(queryset=Autor.objects.all(), slug_field="nome")
    categoria = serializers.SlugRelatedField(queryset=Categoria.objects.all(), slug_field="nome")

    class Meta:
        model = Livro
        fields = "__all__"
