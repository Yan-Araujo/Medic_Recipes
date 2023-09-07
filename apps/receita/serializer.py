from rest_framework import serializers
from apps.receita.models import ReceitaModels


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceitaModels
        fields = '__all__'
