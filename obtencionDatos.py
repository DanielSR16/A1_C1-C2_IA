import csv
import random
from re import T
from traceback import print_tb
from alimentos import alimentos as alimentosTotal
from individuo import Individuo
import string
import operator

generos = []
pesos = []
estaturas = []
edades = []
tipoActividades = []
alimentos = []

letras = string.ascii_lowercase


poblacionInicial = 7
generaciones = 5 
probabilidadMutacion = 0.09
probabilidadMutacionGen = 0.7
poblacionMaxima = 30


listaTotalIndividuos = {}
lista_letras_individuos = []

lista_alimentos_mutacion = []
lista_alimentos_mutacion_valores = []



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
# print(individual_alimentos)


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
        print(valor)
        CaloriasConsumir = ((655 + (9.6 * peso)) + ((1.8 * estatura ) - ( 4.7 * edad))) * calcularFactorActividad(actividad)
        print(CaloriasConsumir)
    elif genero == 'Hombre':
        print('hombre')
        print(valor)
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
            if individual_genero == 'Mujer':
                if dato.i_caloriasDieta > 1800:
                    lista_letras_individuos.append(letras[contador])

                    listaTotalIndividuos[letras[contador]] = dato
                    
                    contador = contador + 1
            elif individual_genero == 'Hombre':

                if dato.i_caloriasDieta > 2000:
                    lista_letras_individuos.append(letras[contador])

                    listaTotalIndividuos[letras[contador]] = dato
                    
                    contador = contador + 1

            

    
  


def cruza():
    aux_letras = []
    aux_letras.extend(lista_letras_individuos)
   
    while (len(aux_letras) > 0):
        #se obtiene primer individuo a cruzar
  
        primerRandom = random.choice(aux_letras)
        aux_letras.pop(aux_letras.index(primerRandom))
        # se obtiene segundo individuo a cruza
        segundoRandom = random.choice(aux_letras)
        aux_letras.pop(aux_letras.index(segundoRandom))
        if(len(aux_letras) == 1):
            primerRandom = random.choice(aux_letras)
            aux_letras.pop(aux_letras.index(primerRandom))
            segundoRandom =  primerRandom
        # print(primerRandom)
        # print(segundoRandom)
        # print(lista_letras_individuos)

        #punto donde se cruzaran los valores
        puntoCruza = random.randint(1,9-1)
        #individuo 1, obtencion de datos
        # print(listaTotalIndividuos.keys())
        # print('Primer Random')
        # print(primerRandom)
        individuo_cruzar_1_nombres = listaTotalIndividuos[primerRandom].alimentosDieta
        individuo_cruzar_1_numeros = listaTotalIndividuos[primerRandom].alimentosDieta_valor
        #individuo 2, obtencion de datos
        # print(individuo_cruzar_1_nombres)
        # print('Segundo Random')
        # print(segundoRandom)
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
        #cruzamos inviduo 1 con 2
        nuevo_individuo_1_nombres =  valor_mantiene_1_nombres + guardar_cruza_2_nombres
        nuevo_individuo_1_numeros =  valor_mantiene_1_numeros + guardar_cruza_2_numeros
        nombre_1 = primerRandom + segundoRandom
        #cruzamos individuo 2 con 1
        nuevo_individuo_2_nombres =  valor_mantiene_2_nombres + guardar_cruza_1_nombres
        nuevo_individuo_2_numeros =  valor_mantiene_2_numeros + guardar_cruza_1_numeros
        nombre_2 = segundoRandom + primerRandom 
       
        #creacion nuevos individuos cruzados AB
        indiv1 = Individuo()
        indiv1.individuo_cruzado(nuevo_individuo_1_nombres,nuevo_individuo_1_numeros)
        indiv1.completarIndividuo(caloriasMaximasConsumir)
        listaTotalIndividuos[nombre_1] = indiv1
        #creacion nuevos individuos cruzados BA
        indiv2 =  Individuo()
        indiv2.individuo_cruzado(nuevo_individuo_2_nombres,nuevo_individuo_2_numeros)
        indiv2.completarIndividuo(caloriasMaximasConsumir)
        listaTotalIndividuos[nombre_2] = indiv2

        lista_letras_individuos.append(nombre_1)
        lista_letras_individuos.append(nombre_2)

    aux_letras.clear()
    


        




def mutacion():
    
    
    listaEliminar = []
    for indi in listaTotalIndividuos.items():

        randomIndiv = random.uniform(0,1)
    
        if(randomIndiv <= probabilidadMutacion):
            # print('INDIVIDUAL***************')
            # print(indi[0])
            # print('random Individual: ',randomIndiv)
            # print('random probmutacion: ',probabilidadMutacion)
            for i in range(0,9):
                randomGen = random.uniform(0,1)
                if randomGen <= probabilidadMutacionGen:
                    # print('GEN************')
                    # print('random GEN: ',randomGen)
                    # print('random prob Gen: ',probabilidadMutacionGen)
                    # print('Voy a mutar por gen', i )
                    bandera = False
                    alimento_borrar = indi[1].alimentosDieta[i] 
                    # alimento_borrar_valor = indi[1].alimentosDieta_valor[i] 
                    while bandera == False:
                        alimentoCambiar = random.choice(lista_alimentos_mutacion)
                        alimentoCambiar_Valor = alimentosTotal[alimentoCambiar]
                        if alimento_borrar != alimentoCambiar:
                            bandera =True
                    cantidad =  random.randint(100,250)
                    indi[1].alimentosDieta[i] = alimentoCambiar
                    indi[1].alimentosDieta_valor[i] = (alimentoCambiar_Valor * cantidad) / 100

            indi[1].individuo_mutacion_completar(caloriasMaximasConsumir)
        if indi[1].i_caloriasDieta > caloriasMaximasConsumir or indi[1].i_caloriasDieta < 2000:
      
            listaEliminar.append(indi[0])
            # print('Se eliminarn: ',indi[0])
            
   
    if len(listaEliminar) > 0:
        
        for  nombre in listaEliminar:
     
            listaTotalIndividuos.pop(nombre)
            


            lista_letras_individuos.remove(nombre)
            segundaVeS = nombre in lista_letras_individuos
            if segundaVeS == True:
                lista_letras_individuos.remove(nombre)

            print(lista_letras_individuos)

    

                         
def poda():
    aptitudes_indi = {}
    peoresAptitudes = []
    for aptitud in listaTotalIndividuos.items():
        aptitudes_indi[aptitud[0]] = aptitud[1].aptitud
    
    

    aptitudes_sort = sorted(aptitudes_indi.items(),key=operator.itemgetter(1),reverse=True)
    contador = 0
    for name in enumerate(aptitudes_sort):
        
        # print(name[1][0])
        if contador > poblacionMaxima-1:
            peoresAptitudes.append(name[1][0])
        contador = contador + 1
    
    if len(peoresAptitudes) > 0:
        for nombre in peoresAptitudes:
            listaTotalIndividuos.pop(nombre)
            # for a in range(len(lista_letras_individuos)-1):
            #     if lista_letras_individuos[a] == nombre:
            #         lista_letras_individuos.pop(a)
            del lista_letras_individuos[lista_letras_individuos.index(nombre)] 
            repetido = nombre in lista_letras_individuos
         
            if repetido == True:
                del lista_letras_individuos[lista_letras_individuos.index(nombre)] 
            # lista_letras_individuos.remove(nombre)
            print(' se elimino =  :',name)    




                    

def eleccionAlimento():
    for alimento in alimentosTotal.items():
        validacionAlimentos = alimento[0] in individual_alimentos
        if validacionAlimentos == False:
            lista_alimentos_mutacion.append(alimento[0])
            lista_alimentos_mutacion_valores.append(alimento[1])

# eleccionAlimento()
# primerosIndividuos()
# cruza()

# mutacion()
# poda()

def main():

    eleccionAlimento()
    primerosIndividuos()
    for i in range(5):
      
        ejecutarGeneracion = False
        while(ejecutarGeneracion == False):
            # print(lista_letras_individuos)
            # print(listaTotalIndividuos.keys())
            cruza()
            mutacion()

            if(len(listaTotalIndividuos) == 30):
                ejecutarGeneracion = True
            elif (len(listaTotalIndividuos) > 30):
                print('entre a podar')
                ejecutarGeneracion = True
                poda()
            
  
    for indi in listaTotalIndividuos.items():
        print(indi[0])
        print(indi[1].toString())
        print("______________________________________________S")
        print(len(listaTotalIndividuos))
main()
print(caloriasMaximasConsumir)
# lista = ['ab','ab','a']
# lista.remove('ab')
# print(lista)