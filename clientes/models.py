from django.db import models

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=200)
    cidade_cliente = models.CharField(max_length=200)
    estado_cliente = models.CharField(max_length=2)
    cep_cliente = models.CharField(max_length=9)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_cliente