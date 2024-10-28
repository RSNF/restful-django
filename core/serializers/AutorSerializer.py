from rest_framework import serializers
from core.models import Autor


class AutorSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="core:autores-detail")

    class Meta:
        model = Autor
        fields = "__all__"
