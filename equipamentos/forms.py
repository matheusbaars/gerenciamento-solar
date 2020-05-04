from django.forms import ModelForm
from .models import Irradiacao, Modulo_fotovoltaico, Inversor_fotovoltaico

class IrradiacaoForm(ModelForm):
    class Meta:
        model = Irradiacao
        fields = '__all__'

class Modulo_fotovoltaicoForm(ModelForm):
    class Meta:
        model = Modulo_fotovoltaico
        fields = '__all__'

class Inversor_fotovoltaicoForm(ModelForm):
    class Meta:
        model = Inversor_fotovoltaico
        fields = '__all__'