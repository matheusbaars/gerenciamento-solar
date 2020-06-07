from django import forms
from equipamentos.models import Irradiacao, Modulo_fotovoltaico,Inversor_fotovoltaico
from temperatura.models import Temperatura
from django.shortcuts import get_object_or_404

class CalculadoraForm(forms.Form):

    CDD = (
        (30, 'Monofásico'),
        (50, 'Bifásico'),
        (100, 'Trifásico')
    )

    # custo_de_disponibilidade = forms.IntegerField(label='Custo de disponibilidade')
    custo_de_disponibilidade = forms.ChoiceField(label='Custo de disponibilidade', choices=CDD)
    consumo_medio = forms.DecimalField(label='Consumo médio', decimal_places=2)
    irradiacao = forms.ModelChoiceField(queryset=Irradiacao.objects.all(), initial='0')
    modulo = forms.ModelChoiceField(queryset=Modulo_fotovoltaico.objects.all(), initial='0')
    #inversor = forms.ModelChoiceField(queryset=Inversor_fotovoltaico.objects.all(), initial='0')

class CalculadoraCompletaForm(forms.Form):
    CDD = (
        (30, 'Monofásico'),
        (50, 'Bifásico'),
        (100, 'Trifásico')
    )

    TEMP = (
        (22, 'Estrutura totalmente elevada (solo)'),
        (28, 'Laje ou telhado (com espaço/inclinação)'),
        (29, 'Sobre o telhado (com ventilação)'),
        (32, 'integrado (sem ventilação)')
    )

    custo_de_disponibilidade = forms.ChoiceField(label='Custo de disponibilidade', choices=CDD, initial='0')
    consumo_medio = forms.FloatField(label='Consumo médio')
    irradiacao = forms.ModelChoiceField(queryset=Irradiacao.objects.all(), initial='0')
    modulo = forms.ModelChoiceField(queryset=Modulo_fotovoltaico.objects.all(), initial='0')
    inversor = forms.ModelChoiceField(queryset=Inversor_fotovoltaico.objects.all(), initial='0')
    temperatura_ambiente = forms.ChoiceField(label='Temperatura no local de instalação', choices=TEMP)
    temperatura_media = forms.ModelChoiceField(queryset=Temperatura.objects.all(), initial='0')
    perda_sombreamento = forms.FloatField(label='Perdas por sombreamento', initial=2)
    perda_sujeira = forms.FloatField(label='Perdas por sujeira', initial=0)
    perda_tolerancia_potencia = forms.FloatField(label='Perdas por Tolerância de potência', initial=0)
    perda_mismatching = forms.FloatField(label='Perdas por mismatching', initial=1)
    perda_cabeamento_cc = forms.FloatField(label='Perdas por cabeamento CC', initial=1)
    perda_spmp = forms.FloatField(label='Perdas por MPPT', initial=0)
    perda_conversao_ccca = forms.FloatField(label='Perdas por conversão CC CA', initial=2.40)
    perda_cabeamento_ca = forms.FloatField(label='Perdas por cabeamento CA', initial=1)
    tarifa_energia = forms.FloatField(label='Tarifa de energia elétrica', initial='0.92')
    


    