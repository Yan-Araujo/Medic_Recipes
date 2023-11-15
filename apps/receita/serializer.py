from rest_framework import serializers
from apps.receita.models import ReceitaModels, AutorModels
from apps.receita.validators import *


class ReceitaSerializer(serializers.ModelSerializer):
    autor_nome = serializers.ReadOnlyField(source='autor_id.nome')

    class Meta:
        model = ReceitaModels
        fields = "__all__"


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorModels
        fields = '__all__'

    def validate(self, data):
        if not validated_nome(data['nome']):
            raise serializers.ValidationError({'nome': 'Nome deve conter apenas Letras e espaços'})

        if not validated_cpf(data['cof']):
            raise serializers.ValidationError({'cpf': 'CPF deve possuir 11 digitos, conter apenas números e caracteres'
                                                      'válidos.'})

        return data
