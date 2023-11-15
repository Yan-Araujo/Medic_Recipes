from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.receita.models import ReceitaModels, AutorModels
from apps.receita.serializer import ReceitaSerializer, AutorSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = ReceitaModels.objects.all()
    serializer_class = ReceitaSerializer

    """Implementando Autentificação de Login e permissões"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    """Implementando Filtros, Barra de busca e ordenação da API"""
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo_receita']
    search_fields = ['titulo_receita', 'autor_id']
    filterset_fields = ['autor_id']


class AutorViewSet(viewsets.ModelViewSet):
    queryset = AutorModels.objects.all()
    serializer_class = AutorSerializer

    """Implementando Autentificação de Login e permissões"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    """Implementando Filtros, Barra de busca e ordenação da API"""
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['nome']
