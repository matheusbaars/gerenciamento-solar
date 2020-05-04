from django.db import models
from equipamentos.models import Irradiacao

class Resultado(models.Model):
    irradiacao = models.ForeignKey(Irradiacao, on_delete=models.CASCADE)
    teste = models.CharField(max_length=10, blank=True, null=True)
    
    
    def __str__(self):
        return self.irradiacao
