from django.db import models


# Create your models here.
class ReceitaModels(models.Model):
    titulo_receita = models.CharField(max_length=40, blank=False, null=False)
    descricao_receita = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.titulo_receita

