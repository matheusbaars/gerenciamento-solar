from django.urls import path
from . import views

urlpatterns = [
    path('calculadora', views.calculadora, name='calculadora'),
    path('resultados', views.resultados, name='resultados'),
    path('calculadora_completa', views.calculadora_completa, name='calculadora_completa'),
    path('resultado_completo', views.resultado_completo, name='resultado_completo'),
    path('gera_relatorio', views.gera_relatorio, name='gera_relatorio')
]