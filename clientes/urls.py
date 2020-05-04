from django.urls import path
from . import views

urlpatterns = [
    path('clientes_registrados', views.clientes_registrados, name='clientes_registrados'),
    path('registrar_cliente', views.registrar_cliente, name='registrar_cliente'),
    path('atualizar_cliente/<int:id>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('deletar_cliente/<int:id>', views.deletar_cliente, name='deletar_cliente')
]