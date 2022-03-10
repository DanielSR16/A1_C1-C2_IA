import csv
import random
from re import T
from traceback import print_tb
from alimentos import alimentos as alimentosTotal
from individuo import Individuo
import string


generos = []
pesos = []
estaturas = []
edades = []
tipoActividades = []
alimentos = []

letras = string.ascii_lowercase


poblacionInicial = 7
generaciones = 5 
probabilidadMutacion = 0.4
probabilidadMutacionGen = 0.7
poblacionMaxima = 30


listaTotalIndividuos = {}
lista_letras_individuos = []


with open('datos_A1_C1-C2.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        generos.append(row[0])
        pesos.append(int(row[1]))
        estaturas.append(int(row[2]))
        edades.append(int(row[3]))
        tipoActividades.append(row[4])
        new_alimentos = row[5].replace(' ','').replace('"','') 
        alimentos.append(new_alimentos+',')


valor = random.randint(0,24)
individual_genero = generos[valor]
individual_peso = pesos[valor]
individual_estatura = estaturas[valor]
individual_edad = edades[valor]
individual_tipoActicvidad = tipoActividades[valor]
individual_alimentos = alimentos[valor]


def calcularFactorActividad(actividad):
  
    if actividad == 'activo':
        factorActividad = 1.725
    elif actividad == 'medio activo':
        factorActividad = 1.55
    elif actividad == 'sedentario':
        factorActividad = 1.2
    return factorActividad

def calcularCalorias(genero,peso,estatura,edad,actividad):
    if genero == 'Mujer':
        print('mujer')
        CaloriasConsumir = ((655 + (9.6 * peso)) + ((1.8 * estatura ) - ( 4.7 * edad))) * calcularFactorActividad(actividad)
    elif genero == 'Hombre':
        print('hombre')
        CaloriasConsumir = ((66 + (13.7 * peso)) + ((5 * estatura ) - ( 6.8 * edad))) * calcularFactorActividad(actividad)
    return CaloriasConsumir
        
caloriasMaximasConsumir = calcularCalorias(individual_genero,individual_peso,individual_estatura,individual_edad,individual_tipoActicvidad)
listaCaloriasDieta = []
conta = 0




def primerosIndividuos():
    contador = 0
    while(contador < poblacionInicial):
        
        dato = Individuo()
        dato.alimentos(alimentosTotal,individual_alimentos)
        dato.completarIndividuo(caloriasMaximasConsumir)

        if dato.i_caloriasDieta < caloriasMaximasConsumir:
            lista_letras_individuos.append(letras[contador])

            listaTotalIndividuos[letras[contador]] = dato
            
            contador = contador + 1

    
  


def cruza():
    
    while (len(lista_letras_individuos) > 0):
        #se obtiene primer individuo a cruzar
        aux_letras = lista_letras_individuos
        primerRandom = random.choice(aux_letras)
        aux_letras.pop(aux_letras.index(primerRandom))
        # se obtiene segundo individuo a cruza
        segundoRandom = random.choice(aux_letras)
        aux_letras.pop(aux_letras.index(segundoRandom))
        if(len(lista_letras_individuos) == 1):
            primerRandom = random.choice(lista_letras_individuos)
            lista_letras_individuos.pop(lista_letras_individuos.index(primerRandom))
            segundoRandom =  primerRandom
        # print(primerRandom)
        # print(segundoRandom)
        # print(lista_letras_individuos)

        #punto donde se cruzaran los valores
        puntoCruza = random.randint(1,9-1)
        #individuo 1, obtencion de datos
        individuo_cruzar_1_nombres = listaTotalIndividuos[primerRandom].alimentosDieta
        individuo_cruzar_1_numeros = listaTotalIndividuos[primerRandom].alimentosDieta_valor
        #individuo 2, obtencion de datos
        # print(individuo_cruzar_1_nombres)
        individuo_cruzar_2_nombres = listaTotalIndividuos[segundoRandom].alimentosDieta
        individuo_cruzar_2_numeros = listaTotalIndividuos[segundoRandom].alimentosDieta_valor
        #guardado de valor a intercambiar del individuo 1
        guardar_cruza_1_nombres = individuo_cruzar_1_nombres[puntoCruza:9]
        guardar_cruza_1_numeros = individuo_cruzar_1_numeros[puntoCruza:9]

        #guardado de valor a intercambiar del individuo 2
        guardar_cruza_2_nombres = individuo_cruzar_2_nombres[puntoCruza:9]
        guardar_cruza_2_numeros = individuo_cruzar_2_numeros[puntoCruza:9]

        #valores que se mantendran del individuo 1
        valor_mantiene_1_nombres =  individuo_cruzar_1_nombres[0:puntoCruza]
        valor_mantiene_1_numeros =  individuo_cruzar_1_numeros[0:puntoCruza]
        # valores que se mantendran del individuo 2
        valor_mantiene_2_nombres =  individuo_cruzar_2_nombres[0:puntoCruza]
        valor_mantiene_2_numeros =  individuo_cruzar_2_numeros[0:puntoCruza]

        nuevo_individuo_1_nombres =  valor_mantiene_1_nombres + guardar_cruza_2_nombres
        nuevo_individuo_1_numeros =  valor_mantiene_1_numeros + guardar_cruza_2_numeros

        nuevo_individuo_2_nombres =  valor_mantiene_2_nombres + guardar_cruza_1_nombres
        nuevo_individuo_2_numeros =  valor_mantiene_2_numeros + guardar_cruza_1_numeros

        nombre_1 = primerRandom + segundoRandom
        nombre_2 = segundoRandom + primerRandom 
        # print(nuevo_individuo_1_nombres)
        # print(nuevo_individuo_1_numeros)
        indiv1 = Individuo()
        indiv1.individuo_cruzado(nuevo_individuo_1_nombres,nuevo_individuo_1_numeros)
        indiv1.completarIndividuo(caloriasMaximasConsumir)
        listaTotalIndividuos[nombre_1] = indiv1

        indiv2 =  Individuo()
        indiv2.individuo_cruzado(nuevo_individuo_2_nombres,nuevo_individuo_2_numeros)
        indiv2.completarIndividuo(caloriasMaximasConsumir)
        listaTotalIndividuos[nombre_2] = indiv2

        lista_letras_individuos.append(nombre_1)
        lista_letras_individuos.append(nombre_2)


    
primerosIndividuos()
cruza()

        

for indi in listaTotalIndividuos.items():
    print(indi[0])
    print(indi[1].toString())
    print("______________________________________________S")
 
print(len(lista_letras_individuos))