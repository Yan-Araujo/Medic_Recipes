from rest_framework import viewsets
from apps.receita.models import ReceitaModels
from apps.receita.serializer import ReceitaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = ReceitaModels.objects.all()
    serializer_class = ReceitaSerializer
