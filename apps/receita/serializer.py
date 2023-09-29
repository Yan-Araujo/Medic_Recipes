from rest_framework import serializers
from apps.receita.models import ReceitaModels, AutorModels


class ReceitaSerializer(serializers.ModelSerializer):
    autor = serializers.ReadOnlyField(source='autor.nome')

    class Meta:
        model = ReceitaModels
        exclude = ('id',)


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorModels
        fields = "__all__"
