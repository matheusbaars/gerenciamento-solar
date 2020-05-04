from django.shortcuts import render, redirect, get_object_or_404
from .forms import CalculadoraForm
from equipamentos.models import Irradiacao, Modulo_fotovoltaico, Inversor_fotovoltaico
from .models import Resultado

def calculadora(request):
    form = CalculadoraForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        
        if form.is_valid():
            return redirect('resultados')
    return render(request, 'calculadora.html', {'form':form})

def resultados(request):
    
    #Pegando o custo de disponibilidade
    custo_de_disponibilidade = int(request.POST['custo_de_disponibilidade'])

    #Pegando o consumo médio
    consumo_medio = float(request.POST['consumo_medio'])

    #Cálculo da energia consumida
    energia_consumida = consumo_medio - custo_de_disponibilidade

    #Cálculo da energia consumida diária
    energia_consumida_diario = energia_consumida / 30
    print('ENERGIA CONSUMIDAD DIARIA {}: '.format(energia_consumida_diario))

    #Pegando dados de irradiação
    irradiacao = request.POST['irradiacao'] #pegando o ID no banco de dados
    irradiacao_media_valor = Irradiacao.objects.filter(id=irradiacao)
    irradiacao_media_valor = float(irradiacao_media_valor[0].irradiacao_media)
    
    #Cálculo da potência pico
    potencia_pico = round((energia_consumida_diario / irradiacao_media_valor), 2)

    #Inserindo no resultado
    resultado = potencia_pico

    #Pegando a potência do módulo
    modulo= request.POST['modulo']
    modulo_valor = Modulo_fotovoltaico.objects.filter(id=modulo)
    modulo_valor = int(modulo_valor[0].pot_nom_maxima)
    print(modulo_valor)

    #Calculando o número de módulos
    numero_modulos = round((potencia_pico * 1000) / modulo_valor, 0)

    resumo = {
        'numero_modulos':numero_modulos,
        'modulo_valor':modulo_valor,
        'consumo_medio':consumo_medio,
        'resultado':resultado
    }    

    # return render(request, 'resultados.html', {'resultado':resultado})
    return render(request, 'resultados.html', resumo)
