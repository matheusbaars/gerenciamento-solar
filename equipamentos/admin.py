from django.contrib import admin
from .models import Modulo_fotovoltaico, Inversor_fotovoltaico, Irradiacao

admin.site.register(Modulo_fotovoltaico)
admin.site.register(Inversor_fotovoltaico)
admin.site.register(Irradiacao)
