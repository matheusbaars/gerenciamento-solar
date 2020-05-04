from django.urls import path
from . import views

urlpatterns = [
    path('calculadora', views.calculadora, name='calculadora'),
    path('resultados', views.resultados, name='resultados')
]