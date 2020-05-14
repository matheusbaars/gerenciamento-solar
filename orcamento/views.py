from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Orcamento
from .forms import OrcamentoForm
from clientes.models import Cliente
from equipamentos.models import Irradiacao, Inversor_fotovoltaico, Modulo_fotovoltaico


def index(request):
    return render(request, 'index.html')

def orcamentos_registrados(request):
    orcamentos = Orcamento.objects.order_by('nome_cliente').all()
    return render(request, 'orcamentos_registrados.html', {'orcamentos':orcamentos})

def registrar_orcamento(request):
    form = OrcamentoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        
        form.save()
        return redirect('orcamentos_registrados')
    return render(request, 'registrar_orcamento.html', {'form':form})