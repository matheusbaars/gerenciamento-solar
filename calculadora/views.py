from django.shortcuts import render, redirect, get_object_or_404
from .forms import CalculadoraForm, CalculadoraCompletaForm
from equipamentos.models import Irradiacao, Modulo_fotovoltaico, Inversor_fotovoltaico
from temperatura.models import Temperatura
from .models import Resultado
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


@login_required
def calculadora(request):

    form = CalculadoraForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        
        if form.is_valid():
            return redirect('resultados')
    return render(request, 'calculadora.html', {'form':form})

@login_required
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

def calculadora_completa(request):
    form = CalculadoraCompletaForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            return redirect('resultado_completo')
    return render(request, 'calculadora_completa.html', {'form':form})

def resultado_completo(request):
    #Pegando o custo de disponibilidade
    custo_de_disponibilidade = int(request.POST['custo_de_disponibilidade'])

    #Pegando o consumo médio
    consumo_medio = float(request.POST['consumo_medio'])

    #Cálculo da energia consumida
    energia_consumida = consumo_medio - custo_de_disponibilidade

    #Cálculo da energia consumida diária
    energia_consumida_diario = energia_consumida / 30
    

    #Pegando dados de irradiação
    irradiacaoID = request.POST['irradiacao']
    irradiacao = Irradiacao.objects.filter(id=irradiacaoID)
    irradiacao_media = float(irradiacao[0].irradiacao_media)
    irradiacao_janeiro = float(irradiacao[0].irradiacao_janeiro)
    irradiacao_fevereiro = float(irradiacao[0].irradiacao_fevereiro)
    irradiacao_marco = float(irradiacao[0].irradiacao_marco)
    irradiacao_abril = float(irradiacao[0].irradiacao_abril)
    irradiacao_maio = float(irradiacao[0].irradiacao_maio)
    irradiacao_junho = float(irradiacao[0].irradiacao_junho)
    irradiacao_julho = float(irradiacao[0].irradiacao_julho)
    irradiacao_agosto = float(irradiacao[0].irradiacao_agosto)
    irradiacao_setembro = float(irradiacao[0].irradiacao_setembro)
    irradiacao_outubro = float(irradiacao[0].irradiacao_outubro)
    irradiacao_novembro = float(irradiacao[0].irradiacao_novembro)
    irradiacao_dezembro = float(irradiacao[0].irradiacao_dezembro)

    #valores de irradiacao
    irradiacao = [
        irradiacao_janeiro,
        irradiacao_fevereiro,
        irradiacao_marco,
        irradiacao_abril,
        irradiacao_maio,
        irradiacao_junho,
        irradiacao_julho,
        irradiacao_agosto,
        irradiacao_setembro,
        irradiacao_outubro,
        irradiacao_novembro,
        irradiacao_dezembro,
        irradiacao_media
    ]

    #Cálculo da potência pico
    potencia_pico = round((energia_consumida_diario / irradiacao_media), 2)
    
    #Obtendo valor da temperatura ambiente
    temperatura_ambiente = int(request.POST['temperatura_ambiente'])

    #temperatura de referência
    temperatura_referencia = 25

    #Temperatura de cálculo
    temperatura_cidadeID = request.POST['temperatura_media']
    temperatura_cidade = Temperatura.objects.filter(id=temperatura_cidadeID)
    temperatura_media = float(temperatura_cidade[0].temperatura_media)
    temperatura_janeiro = float(temperatura_cidade[0].temperatura_janeiro)
    temperatura_fevereiro = float(temperatura_cidade[0].temperatura_fevereiro)
    temperatura_marco = float(temperatura_cidade[0].temperatura_marco)
    temperatura_abril = float(temperatura_cidade[0].temperatura_abril)
    temperatura_maio = float(temperatura_cidade[0].temperatura_maio)
    temperatura_junho = float(temperatura_cidade[0].temperatura_junho)
    temperatura_julho = float(temperatura_cidade[0].temperatura_julho)
    temperatura_agosto = float(temperatura_cidade[0].temperatura_agosto)
    temperatura_setembro = float(temperatura_cidade[0].temperatura_setembro)
    temperatura_outubro = float(temperatura_cidade[0].temperatura_outubro)
    temperatura_novembro = float(temperatura_cidade[0].temperatura_novembro)
    temperatura_dezembro = float(temperatura_cidade[0].temperatura_dezembro)

    temperatura_cidade = [
        temperatura_janeiro,
        temperatura_fevereiro,
        temperatura_marco,
        temperatura_abril,
        temperatura_maio,
        temperatura_junho,
        temperatura_julho,
        temperatura_agosto,
        temperatura_setembro,
        temperatura_outubro,
        temperatura_novembro,
        temperatura_dezembro,
        temperatura_media
    ]

    #array de perdas por temperatura mensal
    perdas_temp_mensal = []
    for temperatura in temperatura_cidade:
        perda_temp_mensal = temperatura + (temperatura_ambiente - temperatura_referencia)
        perdas_temp_mensal.append(perda_temp_mensal) 

    #calculando rendimento de potência
    temperatura_de_calculo = temperatura_media + (temperatura_ambiente - temperatura_referencia)
    
    #pegando dados do módulo
    #dado de coeficiente de potência
    moduloID = request.POST['modulo']
    modulo = Modulo_fotovoltaico.objects.filter(id=moduloID)
    modulo_potencia = int(modulo[0].pot_nom_maxima)
    modulo_modelo = modulo[0].modelo
    modulo_comprimento = float(modulo[0].comprimento)
    modulo_largura = float(modulo[0].largura)

    #dado de coeficiente de Pmax
    modulo_coeficiente_potenciapmax = float(modulo[0].coeficiente_de_temperatura_Pmax)
    
    #calculando perdas em porcentagem
    novo_valor_temperatura_array = []
    for temperatura in perdas_temp_mensal:
        novo_valor_temperatura = temperatura * modulo_coeficiente_potenciapmax
        novo_valor_temperatura_array.append(novo_valor_temperatura)


    #RENDIMENTO POR MÊS
    rendimento_mensal_array = []
    for rendimento in novo_valor_temperatura_array:
        randimento_mensal = 100 + rendimento
        rendimento_mensal_array.append(randimento_mensal)
    

    #perda por temperatura
    perda_por_temperatura = round(modulo_coeficiente_potenciapmax * temperatura_de_calculo, 2)

    #rendimento do módulo
    rendimento_modulo = round(((100 + perda_por_temperatura) / 100) * modulo_potencia, 0)

    #cálculo de perdas por sombreamento, sujeira etc
    sombreamento = (100 - float(request.POST['perda_sombreamento'])) / 100
    sujeira = (100 - float(request.POST['perda_sujeira'])) / 100
    tolerancia_potencia = (100 - float(request.POST['perda_tolerancia_potencia'])) / 100
    mismatching = (100 - float(request.POST['perda_mismatching'])) / 100
    cabeamento_cc = (100 - float(request.POST['perda_cabeamento_cc'])) / 100
    mppt = (100 - float(request.POST['perda_spmp'])) / 100
    conversao_ccca = (100 - float(request.POST['perda_conversao_ccca'])) / 100
    cabeamento_ca = (100 - float(request.POST['perda_cabeamento_ca'])) / 100
    
    perdas_fisicas_media = round((sombreamento * sujeira * tolerancia_potencia * mismatching * cabeamento_cc * mppt * conversao_ccca * cabeamento_ca), 2)
    
    #desempenho global
    desempenho_global_mes = []
    for desempenho in rendimento_mensal_array:
        desempenho_por_mes = desempenho * perdas_fisicas_media / 100
        desempenho_global_mes.append(round(desempenho_por_mes, 2))

    

    #número de módulos
    numero_de_modulos = int((potencia_pico * 1000) / rendimento_modulo)
    
    #área mínima necessária
    modulos_area_total = round((modulo_comprimento * modulo_largura * numero_de_modulos) / 1000000, 2)

    #nova potência pico
    nova_potencia_pico = numero_de_modulos * modulo_potencia / 1000
    
    #energia gerada em cada mês
    energia_gerada_mensal = []
    for energia in desempenho_global_mes:
        energia_gerada = nova_potencia_pico * energia
        energia_gerada_mensal.append(round(energia_gerada, 2))
    
    energia_gerada_final = []
    for energia, irr in zip(energia_gerada_mensal, irradiacao):
        valor = energia * irr * 30
        energia_gerada_final.append(round(valor, ))

    #geracao anual
    geracao_anual = round(energia_gerada_final[12] * 12, 0)

    #perdas em %
    perdas = round(100 - (energia_gerada_final[12] / energia_consumida) * 100, 2)

    #tarifa de energia
    tarifa = float(request.POST['tarifa_energia'])

    arrecadacao_mensal = []
    for ganho in energia_gerada_final:
        arrecadacao = ganho * tarifa
        arrecadacao_mensal.append(round(arrecadacao, 2))

    ganho_anual = round(geracao_anual * tarifa, 2)

    meses_ano = [
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro',
        'Média anual'
    ]

    resumo = {
        'modulo_modelo': modulo_modelo,
        'modulo_potencia': modulo_potencia,
        'numero_de_modulos': numero_de_modulos,
        'modulos_area_total': modulos_area_total,
        'custo_de_disponibilidade': custo_de_disponibilidade,
        'nova_potencia_pico': nova_potencia_pico,
        'energia_gerada_final': energia_gerada_final,
        'geracao_anual': geracao_anual,
        'perdas': perdas,
        'meses_ano': meses_ano,
        'tarifa': tarifa,
        'arrecadacao_mensal': arrecadacao_mensal,
        'ganho_anual': ganho_anual,
    }

    return render(request, 'resultado_completo.html', resumo)


def gera_relatorio(request):
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, 'Teste')
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
