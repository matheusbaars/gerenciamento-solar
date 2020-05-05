from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import logout

def logado(request):
    return render(request, 'logado.html')

def my_logout(request):
    logout(request)
    return render(request, 'index.html')