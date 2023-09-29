from rest_framework import viewsets
from apps.receita.models import ReceitaModels, AutorModels
from apps.receita.serializer import ReceitaSerializer, AutorSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = ReceitaModels.objects.all()
    serializer_class = ReceitaSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = AutorModels.objects.all()
    serializer_class = AutorSerializer
