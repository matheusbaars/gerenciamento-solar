from django.urls import path
from . import views

urlpatterns = [
    path('temperaturas_registradas', views.temperaturas_registradas, name='temperaturas_registradas'),
    path('registrar_temperatura', views.registrar_temperatura, name='registrar_temperatura'),
    path('atualizar_temperatura/<int:id>', views.atualizar_temperatura, name='atualizar_temperatura'),
    path('deletar_temperatura/<int:id>', views.deletar_temperatura, name='deletar_temperatura')
]

