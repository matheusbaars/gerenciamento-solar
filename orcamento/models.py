from django.db import models
from clientes.models import Cliente
from equipamentos.models import Inversor_fotovoltaico, Modulo_fotovoltaico, Irradiacao


class Orcamento(models.Model):
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    inversor_cliente = models.ForeignKey(Inversor_fotovoltaico, on_delete=models.CASCADE, blank=True, null=True)
    modulo_cliente = models.ForeignKey(Modulo_fotovoltaico, on_delete=models.CASCADE)
    Irradiacao_cliente = models.ForeignKey(Irradiacao, on_delete=models.CASCADE)
    num_mod_cliente = models.IntegerField()
    potencia = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    geracao_estimada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome_cliente

