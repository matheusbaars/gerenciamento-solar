from django.db import models
from equipamentos.models import Irradiacao, Modulo_fotovoltaico, Inversor_fotovoltaico

class Resultado(models.Model):
    irradiacao = models.ForeignKey(Irradiacao, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo_fotovoltaico, on_delete=models.CASCADE, blank=True, null=True, default='')
    inversor = models.ForeignKey(Inversor_fotovoltaico, on_delete=models.CASCADE, blank=True, null=True, default='')
    
    
    def __str__(self):
        return self.irradiacao
