from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from receita.models import UsuarioModels


admin.site.register(UsuarioModels, UserAdmin)
