from django.shortcuts import render, get_object_or_404, redirect
from .models import Temperatura
from .forms import TemperaturaForm
from django.contrib.auth.decorators import login_required

@login_required
def temperaturas_registradas(request):
    temperaturas = Temperatura.objects.order_by('cidade')
    return render(request, 'temperaturas_registradas.html', {'temperaturas': temperaturas})

@login_required
def registrar_temperatura(request):
    form = TemperaturaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('temperaturas_registradas')
    return render(request, 'registrar_temperatura.html', {'form':form})

@login_required
def atualizar_temperatura(request, id):
    temperatura = get_object_or_404(Temperatura, pk=id)
    form = TemperaturaForm(request.POST or None, request.FILES or None, instance=temperatura)

    if form.is_valid():
        form.save()
        return redirect('temperaturas_registradas')
    return render(request, 'registrar_temperatura.html', {'form':form})

@login_required
def deletar_temperatura(request, id):
    temperatura = get_object_or_404(Temperatura, pk=id)

    if request.method == 'POST':
        temperatura.delete()
        return redirect('temperaturas_registradas')
    return render(request, 'confirmar_deletar_temperatura.html', {'temperatura':temperatura})