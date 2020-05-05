from django.urls import path
from . import views


urlpatterns = [
    path('logado', views.logado, name='logado'),
    path('logout/', views.my_logout, name='logout')
]