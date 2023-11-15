from django.urls import path, include
from .views import ReceitaViewSet, UsuarioViewSet, ListaUsuarios

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('cadastrar_usuario', UsuarioViewSet, basename='Cadastrar Usuário')
router.register('receitas', ReceitaViewSet, basename='Receita')

urlpatterns = [
    path('', include(router.urls)),
    path('cadastrar_usuario/', ListaUsuarios.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
