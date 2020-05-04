from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('calculadora.urls')),
    path('', include('equipamentos.urls')),
    path('', include('clientes.urls')),
    path('', include('orcamento.urls')),
    path('admin/', admin.site.urls)
] 
