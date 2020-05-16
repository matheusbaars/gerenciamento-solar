from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def logado(request):
    return render(request, 'logado.html')

@login_required
def my_logout(request):
    logout(request)
    return render(request, 'index.html')

@login_required
def database(request):
    return render(request, 'database.html')