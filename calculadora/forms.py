from django import forms
from equipamentos.models import Irradiacao 
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
    # irradiacao = forms.ModelChoiceField(queryset=Irradiacao.objects.get(), initial='0')
    potencia_painel = forms.IntegerField(label='Potência')