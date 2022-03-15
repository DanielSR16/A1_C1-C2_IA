import csv
import random
from re import T
from traceback import print_tb
from alimentos import alimentos as alimentosTotal
from individuo import Individuo
import string
import operator
import pandas as pd
import matplotlib.pyplot as plt
import sys
import PySide6
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from matplotlib import widgets
from tabla_view import Ui_MainWindow
from view import Ui_Dialog


generos = []
pesos = []
estaturas = []
edades = []
tipoActividades = []
alimentos = []

letras = string.ascii_lowercase


poblacionInicial = 10
generaciones = 5
probabilidadMutacion = 0.09
probabilidadMutacionGen = 0.9
poblacionMaxima = 30


listaTotalIndividuos = {}
lista_letras_individuos = []

lista_alimentos_mutacion = []
lista_alimentos_mutacion_valores = []

individuos_finales_ordenados = {}


with open('datos_A1_C1-C2.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        generos.append(row[0])
        pesos.append(int(row[1]))
        estaturas.append(int(row[2]))
        edades.append(int(row[3]))
        tipoActividades.append(row[4])
        new_alimentos = row[5].replace(' ', '').replace('"', '')
        alimentos.append(new_alimentos)

valor = random.randint(0, 24)
individual_genero = generos[valor]
individual_peso = pesos[valor]
individual_estatura = estaturas[valor]
individual_edad = edades[valor]
individual_tipoActicvidad = tipoActividades[valor]
individual_alimentos = alimentos[valor] + ','


class Dialogo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.datosTablas()

     
    def getItems(self):

        generos_m = generos
        pesos_m = pesos
        estaturas_m = estaturas
        edades_m = edades
        tipoActividades_m = tipoActividades
        alimentos_m = alimentos

        index = self.ui.personas.currentIndex().row()

        self.ui.labelGenero.setText(generos_m[index])
        self.ui.labelPeso.setText(f'{pesos_m[index]}')
        self.ui.labelEstatura.setText(f'{estaturas_m[index]}')
        self.ui.labelEdad.setText(f'{edades_m[index]}')
        self.ui.labelAF.setText(tipoActividades_m[index])

        if alimentos_m[index] == 'Todo':
            self.ui.tableAlimentos.clearContents()
            self.ui.tableAlimentos.setRowCount(1)
            a2 = QTableWidgetItem('Le gustan todos los alimentos')
            self.ui.tableAlimentos.setItem(0, 0, a2)

        else:
            
            alimen = alimentos_m[index].split()
            dato = str(alimentos_m[index])
            lista_new = dato.split(',')
   
            self.ui.tableAlimentos.setRowCount(len(lista_new))
            self.ui.tableAlimentos.clearContents()

            # for i in range(len(lista_new)):
            #     alimen[i].replace(',', '')

            row = 0
            for i in lista_new:
                self.ui.tableAlimentos.setRowCount(row+1)
                a2 = QTableWidgetItem(i)
                self.ui.tableAlimentos.setItem(row, 0, a2)
                row += 1

    def datosTablas(self):
        listaTotal = []
        resultadoMain = main()
        self.ui.tabla_dieta.setRowCount(60)
        self.ui.tabla_dieta.setColumnCount(11)
        alimento = []
        cantidad = []
        for i in range(30):
            alimento.append(resultadoMain[0][i].alimentosDieta)
            cantidad.append(resultadoMain[0][i].alimentosDieta_cantidad)
          
      
        
        listaDatosColumna = []
        listaAux = []
        contador = 0
        for x in range(9):

            for y in range(30):
                listaAux.append(alimento[y][contador])
                listaAux.append(cantidad[y][contador])
            contador = contador +1 
            listaDatosColumna.append(listaAux)
            listaAux = []

        listaDias = []
        for dias in range(30):
            dia = 'Dia: ' + str(dias+1)
            listaDias.append(dia)
            listaDias.append("")

        listaDatosColumna.append(listaDias)

        lista_total_Calorias = []
        for c in range(30):
           lista_total_Calorias.append( round(resultadoMain[0][c].i_caloriasDieta,4))
           lista_total_Calorias.append( "")

        listaDatosColumna.append(lista_total_Calorias)

        row = 0
        colum = 0
        
        for a in listaDatosColumna:
            if colum < 9:
                name_horizontal = QTableWidgetItem('Dieta')
                self.ui.tabla_dieta.setHorizontalHeaderItem(colum,name_horizontal)
            elif colum == 9:
                name_horizontal = QTableWidgetItem('Fechas')
                self.ui.tabla_dieta.setHorizontalHeaderItem(colum,name_horizontal)
            elif colum == 10:
                name_horizontal = QTableWidgetItem('Calorias')
                self.ui.tabla_dieta.setHorizontalHeaderItem(colum,name_horizontal)
            for datos in a:
               
                # self.ui.tabla_dieta.setRowCount(row+1)
                a2 = QTableWidgetItem(str(datos))
                

                self.ui.tabla_dieta.setItem(row, colum, a2)
                if row % 2 == 0:
                    name = QTableWidgetItem('Alimentos')
                    
                else:
                    name = QTableWidgetItem('Cantidad')
                self.ui.tabla_dieta.setVerticalHeaderItem(row,name)
                row += 1
            colum += 1
            row = 0
        #Datos Tabla usuario

        lista_datos_usuario = []

        lista_datos_usuario.append('Genero: '+individual_genero)
        lista_datos_usuario.append('Peso: '+str(individual_peso))
        lista_datos_usuario.append('Estatura: '+str(individual_estatura))
        lista_datos_usuario.append('Edad: '+str(individual_edad))
        lista_datos_usuario.append('tipoActividad: '+individual_tipoActicvidad)
        lista_datos_usuario.append('Kg Bajar/mes: '+str(round(resultadoMain[1],4)))
        lista_datos_usuario.append('Calorias reducidad/mes: '+str(round(resultadoMain[2],4)))

        print(lista_datos_usuario)
        self.ui.tabla_datos.setRowCount(7)
        self.ui.tabla_datos.setColumnCount(1)
        row = 0
        name_horizontal = QTableWidgetItem('Datos Persona')
        self.ui.tabla_datos.setHorizontalHeaderItem(0,name_horizontal)
        for i in lista_datos_usuario:
            self.ui.tabla_datos.setRowCount(row+1)
            a2 = QTableWidgetItem(i)
            self.ui.tabla_datos.setItem(row, 0, a2)
            row += 1



            

            

            


        



# print(individual_alimentos)


def calcularFactorActividad(actividad):

    if actividad == 'activo':
        factorActividad = 1.725
    elif actividad == 'medio activo':
        factorActividad = 1.55
    elif actividad == 'sedentario':
        factorActividad = 1.2
    return factorActividad


def calcularCalorias(genero, peso, estatura, edad, actividad):
    if genero == 'Mujer':
        print('mujer')
        print(valor)
        CaloriasConsumir = ((655 + (9.6 * peso)) + ((1.8 * estatura) -
                            (4.7 * edad))) * calcularFactorActividad(actividad)
        print(CaloriasConsumir)
    elif genero == 'Hombre':
        print('hombre')
        print(valor)
        CaloriasConsumir = ((66 + (13.7 * peso)) + ((5 * estatura) -
                            (6.8 * edad))) * calcularFactorActividad(actividad)
    return CaloriasConsumir


caloriasMaximasConsumir = calcularCalorias(
    individual_genero, individual_peso, individual_estatura, individual_edad, individual_tipoActicvidad)
listaCaloriasDieta = []
conta = 0


def primerosIndividuos():
    contador = 0
    while(contador < poblacionInicial):

        dato = Individuo()
        dato.alimentos(alimentosTotal, individual_alimentos)
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
        # se obtiene primer individuo a cruzar

        primerRandom = random.choice(aux_letras)
        aux_letras.pop(aux_letras.index(primerRandom))
        # se obtiene segundo individuo a cruza
        segundoRandom = random.choice(aux_letras)
        aux_letras.pop(aux_letras.index(segundoRandom))
        if(len(aux_letras) == 1):
            primerRandom = random.choice(aux_letras)
            aux_letras.pop(aux_letras.index(primerRandom))
            segundoRandom = primerRandom
        # print(primerRandom)
        # print(segundoRandom)
        # print(lista_letras_individuos)

        # punto donde se cruzaran los valores
        puntoCruza = random.randint(1, 9-1)
        # individuo 1, obtencion de datos
        # print(listaTotalIndividuos.keys())
        # print('Primer Random')
        # print(primerRandom)
        individuo_cruzar_1_nombres = listaTotalIndividuos[primerRandom].alimentosDieta
        individuo_cruzar_1_numeros = listaTotalIndividuos[primerRandom].alimentosDieta_valor
        individuo_cruzar_1_cantidad = listaTotalIndividuos[primerRandom].alimentosDieta_cantidad
        # individuo 2, obtencion de datos
        # print(individuo_cruzar_1_nombres)
        # print('Segundo Random')
        # print(segundoRandom)
        individuo_cruzar_2_nombres = listaTotalIndividuos[segundoRandom].alimentosDieta
        individuo_cruzar_2_numeros = listaTotalIndividuos[segundoRandom].alimentosDieta_valor
        individuo_cruzar_2_cantidad = listaTotalIndividuos[segundoRandom].alimentosDieta_cantidad

        # guardado de valor a intercambiar del individuo 1
        guardar_cruza_1_nombres = individuo_cruzar_1_nombres[puntoCruza:9]
        guardar_cruza_1_numeros = individuo_cruzar_1_numeros[puntoCruza:9]
        guardar_cruza_1_cantidad = individuo_cruzar_1_cantidad[puntoCruza:9]

        # guardado de valor a intercambiar del individuo 2
        guardar_cruza_2_nombres = individuo_cruzar_2_nombres[puntoCruza:9]
        guardar_cruza_2_numeros = individuo_cruzar_2_numeros[puntoCruza:9]
        guardar_cruza_2_cantidad = individuo_cruzar_2_cantidad[puntoCruza:9]

        # valores que se mantendran del individuo 1
        valor_mantiene_1_nombres = individuo_cruzar_1_nombres[0:puntoCruza]
        valor_mantiene_1_numeros = individuo_cruzar_1_numeros[0:puntoCruza]
        valor_mantiene_1_cantidad = individuo_cruzar_1_cantidad[0:puntoCruza]
        # valores que se mantendran del individuo 2
        valor_mantiene_2_nombres = individuo_cruzar_2_nombres[0:puntoCruza]
        valor_mantiene_2_numeros = individuo_cruzar_2_numeros[0:puntoCruza]
        valor_mantiene_2_cantidad = individuo_cruzar_2_cantidad[0:puntoCruza]
        # cruzamos inviduo 1 con 2
        nuevo_individuo_1_nombres = valor_mantiene_1_nombres + guardar_cruza_2_nombres
        nuevo_individuo_1_numeros = valor_mantiene_1_numeros + guardar_cruza_2_numeros
        nuevo_individuo_1_cantidad = valor_mantiene_1_cantidad + guardar_cruza_2_cantidad
        nombre_1 = primerRandom + segundoRandom
        # cruzamos individuo 2 con 1
        nuevo_individuo_2_nombres = valor_mantiene_2_nombres + guardar_cruza_1_nombres
        nuevo_individuo_2_numeros = valor_mantiene_2_numeros + guardar_cruza_1_numeros
        nuevo_individuo_2_cantidad = valor_mantiene_2_cantidad + guardar_cruza_1_cantidad
        nombre_2 = segundoRandom + primerRandom

        # creacion nuevos individuos cruzados AB
        indiv1 = Individuo()
        indiv1.individuo_cruzado(
            nuevo_individuo_1_nombres, nuevo_individuo_1_numeros, nuevo_individuo_1_cantidad)
        indiv1.completarIndividuo(caloriasMaximasConsumir)
        listaTotalIndividuos[nombre_1] = indiv1
        # creacion nuevos individuos cruzados BA
        indiv2 = Individuo()
        indiv2.individuo_cruzado(
            nuevo_individuo_2_nombres, nuevo_individuo_2_numeros, nuevo_individuo_2_cantidad)
        indiv2.completarIndividuo(caloriasMaximasConsumir)
        listaTotalIndividuos[nombre_2] = indiv2

        lista_letras_individuos.append(nombre_1)
        lista_letras_individuos.append(nombre_2)

    aux_letras.clear()


def eliminar_letra(dato_eliminar):
    listaPosiciones_eliminar = []
    for i in lista_letras_individuos:
        if i == dato_eliminar:
            listaPosiciones_eliminar.append(i)
    # print('lista Valores: ',listaPosiciones_eliminar)
    if len(listaPosiciones_eliminar) > 0:
        for borrar in listaPosiciones_eliminar:
            lista_letras_individuos.remove(borrar)

    listaPosiciones_eliminar = []


def mutacion():

    listaEliminar = []
    for indi in listaTotalIndividuos.items():

        randomIndiv = random.uniform(0, 1)

        if(randomIndiv <= probabilidadMutacion):
            # print('INDIVIDUAL***************')
            # print(indi[0])
            # print('random Individual: ',randomIndiv)
            # print('random probmutacion: ',probabilidadMutacion)
            for i in range(0, 9):
                randomGen = random.uniform(0, 1)
                if randomGen <= probabilidadMutacionGen:
                    # print('GEN************')
                    # print('random GEN: ',randomGen)
                    # print('random prob Gen: ',probabilidadMutacionGen)
                    # print('Voy a mutar por gen', i )
                    bandera = False
                    alimento_borrar = indi[1].alimentosDieta[i]
                    # alimento_borrar_valor = indi[1].alimentosDieta_valor[i]
                    while bandera == False:
                        alimentoCambiar = random.choice(
                            lista_alimentos_mutacion)
                        alimentoCambiar_Valor = alimentosTotal[alimentoCambiar]

                        if alimento_borrar != alimentoCambiar:
                            bandera = True
                    cantidad = random.randint(100, 300)
                    indi[1].alimentosDieta[i] = alimentoCambiar
                    indi[1].alimentosDieta_valor[i] = (
                        alimentoCambiar_Valor * cantidad) / 100
                    indi[1].alimentosDieta_cantidad[i] = cantidad

            indi[1].individuo_mutacion_completar(caloriasMaximasConsumir)
        if individual_genero == 'Hombre':
            if indi[1].i_caloriasDieta > caloriasMaximasConsumir or indi[1].i_caloriasDieta < 2000:
                listaEliminar.append(indi[0])
        elif individual_genero == 'Mujer':
            if indi[1].i_caloriasDieta > caloriasMaximasConsumir or indi[1].i_caloriasDieta < 1800:
                listaEliminar.append(indi[0])

    if len(listaEliminar) > 0:
        # print('lista elimanr: ',listaEliminar)
        for nombre_eliminar1 in listaEliminar:
            # print('valor eliminar: ',nombre_eliminar1)
            # print('Total Nombre : ',lista_letras_individuos)
            listaTotalIndividuos.pop(nombre_eliminar1)

            eliminar_letra(nombre_eliminar1)
            # print('Total Nombre Despues: ',lista_letras_individuos)


def poda():
    aptitudes_indi = {}
    peoresAptitudes = []
    for aptitud in listaTotalIndividuos.items():
        aptitudes_indi[aptitud[0]] = aptitud[1].aptitud

    aptitudes_sort = sorted(aptitudes_indi.items(),
                            key=operator.itemgetter(1), reverse=True)
    contador = 0
    for name in enumerate(aptitudes_sort):

        # print(name[1][0])
        if contador > poblacionMaxima-1:
            peoresAptitudes.append(name[1][0])
        contador = contador + 1

    if len(peoresAptitudes) > 0:
        for nombre_eliminar2 in peoresAptitudes:
            listaTotalIndividuos.pop(nombre_eliminar2)

            eliminar_letra(nombre_eliminar2)


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
    for i in range(generaciones):

        ejecutarGeneracion = False
        while(ejecutarGeneracion == False):
            # print(lista_letras_individuos)
            # print(listaTotalIndividuos.keys())
            cruza()
            mutacion()

            if(len(listaTotalIndividuos) == poblacionMaxima):
                ejecutarGeneracion = True
            elif (len(listaTotalIndividuos) > poblacionMaxima):
                # print('entre a podar')
                ejecutarGeneracion = True
                poda()

    aptitudes_indi_final = {}
    for aptitud in listaTotalIndividuos.items():
        aptitudes_indi_final[aptitud[0]] = aptitud[1].aptitud

    aptitudes_sort = sorted(aptitudes_indi_final.items(),
                            key=operator.itemgetter(1), reverse=True)

    for name in enumerate(aptitudes_sort):
        individuos_finales_ordenados[name[1][0]
                                     ] = listaTotalIndividuos[name[1][0]]
        # print(name[1][0])
    Suma_total_pesos = 0
    suma_total_calorias_reducir = 0
    for indi in individuos_finales_ordenados.items():
        # print(indi[0])
        print(indi[1].toString())
        Suma_total_pesos = Suma_total_pesos + indi[1].aptitud
        suma_total_calorias_reducir = suma_total_calorias_reducir + \
            indi[1].fenotipo
        print("______________________________________________ Final")

    print('Total a bajar:', Suma_total_pesos)
    print("Total de calorias reducidas", suma_total_calorias_reducir)
    listIndividuosFinales = []
    for valor in individuos_finales_ordenados.items(): 
        listIndividuosFinales.append(valor[1])

    return listIndividuosFinales,Suma_total_pesos,suma_total_calorias_reducir


def a():
  print('holis ')
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
sys.exit(app.exec())
