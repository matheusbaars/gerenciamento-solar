from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_orcamento', views.registrar_orcamento, name='registrar_orcamento'),
    path('orcamentos_registrados', views.orcamentos_registrados, name='orcamentos_registrados')
]