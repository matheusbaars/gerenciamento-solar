from django.urls import path
from . import views

urlpatterns = [
    path('modulos_fotovoltaicos_registrados', views.modulos_fotovoltaicos_registrados, name='modulos_fotovoltaicos_registrados' ),
    path('irradiacao_registrados', views.irradiacao_registrados, name='irradiacao_registrados'),
    path('registrar_irradiacao', views.registrar_irradiacao, name='registrar_irradiacao'),
    path('atualizar_irradiacao/<int:id>', views.atualizar_irradiacao, name='atualizar_irradiacao'),
    path('deletar_irradiacao/<int:id>', views.deletar_irradiacao, name='deletar_irradiacao'),
    path('registrar_modulo_fotovoltaico', views.registrar_modulo_fotovoltaico, name='registrar_modulo_fotovoltaico'),
    path('atualizar_modulo_fotovoltaico/<int:id>', views.atualizar_modulo_fotovoltaico, name='atualizar_modulo_fotovoltaico'),
    path('deletar_modulo_fotovoltaico/<int:id>', views.deletar_modulo_fotovoltaico, name='deletar_modulo_fotovoltaico'),
    path('inversores_registrados', views.inversores_registrados, name='inversores_registrados'),
    path('registrar_inversor', views.registrar_inversor, name='registrar_inversor'),
    path('atualizar_inversor/<int:id>', views.atualizar_inversor, name='atualizar_inversor'),
    path('deletar_inversor/<int:id>', views.deletar_inversor, name='deletar_inversor'),
]