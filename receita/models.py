from django.db import models
from django.contrib.auth.models import AbstractUser


# class AutorModels(models.Model):
#     nome = models.CharField(max_length=40, blank=False, null=False)
#     cpf = models.CharField(max_length=11, blank=False, null=False)
#     email = models.EmailField(blank=False, null=False, default="", max_length=40)
#     especializacao = models.CharField(max_length=40, blank=False, null=False)
#
#     def __str__(self):
#         return self.nome

class UsuarioModels(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=15)
    user_email = models.EmailField(unique=True, error_messages={'unique': 'E-mail já cadastrado'})
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class ReceitaModels(models.Model):
    autor_id = models.ForeignKey(UsuarioModels, on_delete=models.CASCADE)
    titulo_receita = models.CharField(max_length=40, blank=False, null=False)
    descricao_receita = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.titulo_receita
