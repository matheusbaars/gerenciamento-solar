from django.db import models

class Temperatura(models.Model):
    cidade = models.CharField(max_length=40)
    temperatura_janeiro = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_fevereiro = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_marco = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_abril = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_maio = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_junho = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_julho = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_agosto = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_setembro = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_outubro = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_novembro = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_dezembro = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura_media = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cidade
