from django.forms import ModelForm
from .models import Temperatura


class TemperaturaForm(ModelForm):
    class Meta:
        model = Temperatura
        fields = '__all__'