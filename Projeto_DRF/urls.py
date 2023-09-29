from django.contrib import admin
from django.urls import path
from rest_framework import routers
from apps.receita.views import ReceitaViewSet, AutorViewSet

router = routers.DefaultRouter()
router.register('receitas', ReceitaViewSet, basename='Receita')
router.register('autores', AutorViewSet, basename='Autor')


urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
