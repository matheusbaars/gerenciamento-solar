from django.db import models

class Irradiacao(models.Model):
    cidade = models.CharField(max_length=40)
    irradiacao_janeiro = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_fevereiro = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_marco = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_abril = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_maio = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_junho = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_julho = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_agosto = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_setembro = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_outubro = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_novembro = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_dezembro = models.DecimalField(max_digits=10, decimal_places=2)
    irradiacao_media = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cidade

class Modulo_fotovoltaico(models.Model):
    TIPO_CELULA = (
        ('MONOCRISTALINA','MONOCRISTALINA'),
        ('POLICRISTALINA','POLICRISTALINA'),
    )
    fabricante = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    pot_nom_maxima = models.IntegerField()
    tensao_de_operacao = models.DecimalField(max_digits=3, decimal_places=1)
    corrente_de_operacao = models.DecimalField(max_digits=3, decimal_places=1)
    tensao_circuito_aberto = models.DecimalField(max_digits=3, decimal_places=1, blank=True, default=None)
    corrente_de_curto_circuito = models.DecimalField(max_digits=3, decimal_places=1)
    eficiencia_modulo = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    fusivel = models.IntegerField(blank=True)
    tolerancia_de_pot_min = models.IntegerField()
    tolerancia_de_pot_max = models.IntegerField()
    tipo_celula = models.CharField(max_length=15, choices=TIPO_CELULA)
    comprimento = models.DecimalField(max_digits=8, decimal_places=1)
    largura = models.DecimalField(max_digits=8, decimal_places=1)
    profundidade = models.DecimalField(max_digits=8, decimal_places=1)
    peso = models.DecimalField(max_digits=8, decimal_places=1)
    coeficiente_de_temperatura_Pmax = models.DecimalField(max_digits=8, decimal_places=2)
    coeficiente_de_temperatura_Voc = models.DecimalField(max_digits=8, decimal_places=2)
    coeficiente_de_temperatura_Isc = models.DecimalField(max_digits=8, decimal_places=2)
    tier = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return self.modelo

class Inversor_fotovoltaico(models.Model):
    fabricante = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    #dados de entrada
    num_de_MPPT = models.IntegerField(blank=True)
    corrente_max_entrada = models.DecimalField(max_digits=8, decimal_places=1)
    corrente_max_curto = models.DecimalField(max_digits=8, decimal_places=1)
    faixa_de_tensao_entrada_min = models.DecimalField(max_digits=8, decimal_places=1)
    faixa_de_tensao_entrada_max = models.DecimalField(max_digits=8, decimal_places=1)
    tensao_de_inicio = models.IntegerField(blank=True)
    range_op_DC_MPPT_min = models.IntegerField(blank=True)
    range_op_DC_MPPT_max = models.IntegerField(blank=True)
    qtd_conexoes = models.DecimalField(max_digits=8, decimal_places=1)
    pot_pico = models.IntegerField()
    #dados de saída
    pot_nominal_CA = models.IntegerField(blank=True)
    pot_maxima_CA = models.IntegerField(blank=True)
    pot_maxima_saida_CA = models.IntegerField(blank=True)
    tensao_max_CA = models.IntegerField(blank=True)
    tensao_min_CA = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.modelo
