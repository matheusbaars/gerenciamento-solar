from django import forms
from django.forms import ModelForm
from equipamentos.models import Inversor_fotovoltaico, Irradiacao, Modulo_fotovoltaico
from clientes.models import Cliente
from .models import Orcamento

# class OrcamentoForm(forms.Form):
#     # dados_cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), initial='0')
#     model = O

class OrcamentoForm(ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'
    


