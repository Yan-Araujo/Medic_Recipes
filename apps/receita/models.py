from django.db import models


class AutorModels(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    especializacao = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return self.nome


class ReceitaModels(models.Model):
    autor_id = models.ForeignKey(AutorModels, on_delete=models.CASCADE)
    titulo_receita = models.CharField(max_length=40, blank=False, null=False)
    descricao_receita = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.titulo_receita
