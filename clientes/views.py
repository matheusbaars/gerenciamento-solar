from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def registrar_cliente(request):
    form = ClienteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        print(form.errors)
        return redirect('clientes_registrados')
    return render(request,'registrar_cliente.html', {'form':form})

def clientes_registrados(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes_registrados.html', {'clientes': clientes})

def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('clientes_registrados')
    
    return render(request, 'registrar_cliente.html', {'form':form})

def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_registrados')
    
    return render(request, 'confirmar_deletar_cliente.html', {'cliente':cliente})