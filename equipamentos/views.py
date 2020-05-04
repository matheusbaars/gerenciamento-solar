from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Irradiacao, Inversor_fotovoltaico, Modulo_fotovoltaico
from .forms import IrradiacaoForm, Modulo_fotovoltaicoForm, Inversor_fotovoltaicoForm

#==================================================================================
#                              MÓDULOS FOTOVOLTAICOS
#==================================================================================
def modulos_fotovoltaicos_registrados(request):
    modulos = Modulo_fotovoltaico.objects.order_by('modelo').all()
    return render(request, 'modulos_fotovoltaicos_registrados.html', {'modulos':modulos})

def registrar_modulo_fotovoltaico(request):
    form = Modulo_fotovoltaicoForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('modulos_fotovoltaicos_registrados')
    return render(request, 'registrar_modulo_fotovoltaico.html', {'form':form})

def atualizar_modulo_fotovoltaico(request, id):
    modulo = get_object_or_404(Modulo_fotovoltaico, pk=id)
    form = Modulo_fotovoltaicoForm(request.POST or None, request.FILES or None, instance=modulo)
    
    if form.is_valid():
        form.save()
        return redirect('modulos_fotovoltaicos_registrados')
    return render(request, 'registrar_modulo_fotovoltaico.html', {'form':form})

def deletar_modulo_fotovoltaico(request, id):
    modulo = get_object_or_404(Modulo_fotovoltaico, pk=id)

    if request.method == 'POST':
        modulo.delete()
        return redirect('modulos_fotovoltaicos_registrados')
    return render(request, 'confirmar_deletar_modulo_fotovoltaico.html', {'modulo':modulo})
#================================FIM MÓDULOS FOTOVOLTAICOS============================




#==================================================================================
#                               Irradiação
#==================================================================================
def irradiacao_registrados(request):
    irradiacao = Irradiacao.objects.order_by('cidade').all()
    return render(request, 'irradiacao_registrados.html', {'irradiacao':irradiacao})

def registrar_irradiacao(request):
    form = IrradiacaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('irradiacao_registrados')
    return render(request, 'registrar_irradiacao.html', {'form':form})

def atualizar_irradiacao(request, id):
    irradiacao = get_object_or_404(Irradiacao, pk=id)
    form = IrradiacaoForm(request.POST or None, request.FILES or None, instance=irradiacao)

    if form.is_valid():
        form.save()
        return redirect('irradiacao_registrados')
    return render(request, 'registrar_irradiacao.html', {'form':form})

def deletar_irradiacao(request, id):
    irradiacao = get_object_or_404(Irradiacao, pk=id)

    if request.method == 'POST':
        irradiacao.delete()
        return redirect('irradiacao_registrados')
    return render(request, 'confirmar_deletar_irradiacao.html', {'irradiacao':irradiacao})

#====================================FIM IRRADIACAO=======================================


#==================================================================================
#                               INVERSOR
#==================================================================================
def inversores_registrados(request):
    inversores = Inversor_fotovoltaico.objects.order_by('modelo').all()
    return render(request, 'inversores_registrados.html', {'inversores':inversores})

def registrar_inversor(request):
    form = Inversor_fotovoltaicoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('inversores_registrados')
    return render(request, 'registrar_inversor.html', {'form':form})

def atualizar_inversor(request, id):
    inversor = get_object_or_404(Inversor_fotovoltaico, pk=id)
    form = Inversor_fotovoltaicoForm(request.POST or None, request.FILES or None, instance=inversor)

    if form.is_valid():
        form.save()
        return redirect('inversores_registrados')
    return render(request, 'registrar_inversor.html', {'form':form})

def deletar_inversor(request, id):
    inversor = get_object_or_404(Inversor_fotovoltaico, pk=id)

    if request.method == 'POST':
        inversor.delete()
        return redirect('inversores_registrados')
    return render(request, 'confirmar_deletar_inversor.html', {'inversor':inversor})
#===============================FIM INVERSOR==========================================