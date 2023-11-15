from rest_framework import viewsets, filters
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from receita.models import ReceitaModels, UsuarioModels
from receita.serializer import ReceitaSerializer, UsuarioSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = ReceitaModels.objects.all()
    serializer_class = ReceitaSerializer

    # """Implementando Autentificação de Login e permissões"""
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    """Implementando Filtros, Barra de busca e ordenação da API"""
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo_receita']
    search_fields = ['titulo_receita', 'autor_id']
    filterset_fields = ['autor_id']


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioModels.objects.all()
    serializer_class = UsuarioSerializer

    # """Implementando Autentificação de Login e permissões"""
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    """Implementando Filtros, Barra de busca e ordenação da API"""
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    filterset_fields = ['nome']


class ListaUsuarios(generics.ListAPIView):
    def get_queryset(self):
        queryset = UsuarioModels.objects.all()
        return queryset
    serializer_class = UsuarioSerializer


