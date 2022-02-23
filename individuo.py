import csv
import random
generos = []
pesos = []
estaturas = []
edades = []
tipoActividades = []
alimentos = []

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

class Individuo():
    def __init__(self):
        self.caloriasMaxConsumir_1 =  0

        self.genero = ''
        self.tipoActividad = ''

        self.alimentosDieta = {}
        self.alimentosConsumir = {}

        self.i_caloriasDieta = 0
        self.fenotipo = 0
        self.aptitud = 0
        

    def caloriasConsumirIndividuo(self,listAlimentos):
        valor = random.randint(0,24)
        individual_genero = generos[valor]
        individual_peso = pesos[valor]
        individual_estatura = estaturas[valor]
        individual_edad = edades[valor]
        individual_tipoActicvidad = tipoActividades[valor]
        individual_alimentos = alimentos[valor]
        # print('peso',individual_peso)
        # print('estatuta',individual_estatura)
        # print('edad',individual_edad)
        # print('actividad',individual_tipoActicvidad)
        # print(individual_tipoActicvidad)
    
        self.caloriasMaxConsumir_1 =round(calcularCalorias(individual_genero,individual_peso,individual_estatura,individual_edad,individual_tipoActicvidad))
        
        self.genero = individual_genero
        self.tipoActividad = individual_tipoActicvidad
        self.alimentos(listAlimentos,individual_alimentos)

    def alimentos(self,listAlimentos,individual_alimentos):
        #lista de nombres de los alimentos que puede cosumir
        nombreAlimentosConsumir = []
        #alimentos que se eliminaran de la lista general
        alimentosEliminar = separarAlimentosNoConsumir(individual_alimentos)
        # print(alimentosEliminar)
        # aqui se eliminaran omitiran los alimentos que al individuo no le gustan, mientras de False podra ingresar a los alimentos a consumir
        for alimentos in listAlimentos.items():
            eliminar = alimentos[0] in alimentosEliminar
            if eliminar == False:
                self.alimentosConsumir[alimentos[0]] = alimentos[1]
        #llenado de lista de nombres de alimentos a consumir
        for alimentoConsumir in self.alimentosConsumir.items():
           nombreAlimentosConsumir.append(alimentoConsumir[0])

        for i in range(0,9):
            #se selecciona un nombre al azar de alimento
            cantidad =  random.randint(100,300)
            seleccionAlimentos = random.randint(0,len(nombreAlimentosConsumir))
            #se saca el valor del alimento al azar
            valorDelAlimento = self.alimentosConsumir[nombreAlimentosConsumir[seleccionAlimentos]]
            #se guarda el alimento dentro de la dieta 
            cantidadCaolorias = (valorDelAlimento * cantidad) / 100
            self.alimentosDieta[nombreAlimentosConsumir[seleccionAlimentos]] = cantidadCaolorias

            self.i_caloriasDieta = self.i_caloriasDieta + cantidadCaolorias
        # print('valor del alimento',valorDelAlimento)
        # print('primero',nombreAlimentosConsumir[0])



    def completarIndividuo(self):
        sumador = 0
        for valores in self.alimentosDietaValor:
            sumador = sumador + valores
        self.i_caloriasDieta = sumador

        self.fenotipo = self.caloriasMaxConsumir_1 - self.i_caloriasDieta





    def toString(self):
        return  f'calorias: {self.alimentosDieta}\n'+f'total: {self.i_caloriasDieta}\n'+f'Maximo Consumir:{self.caloriasMaxConsumir_1}\n' 



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
        CaloriasConsumir = ((655 + (9.6 * peso)) + ((1.8 * estatura ) - ( 4.7 * edad) )) * calcularFactorActividad(actividad)
    elif genero == 'Hombre':
        print('hombre')
        CaloriasConsumir = ((66 + (13.7 * peso)) + ((5 * estatura ) - ( 6.8 * edad))) * calcularFactorActividad(actividad)
    return CaloriasConsumir


def separarAlimentosNoConsumir(alimentosNoConsumir):
    listAlimentos = []
    stringAux = ''
    for dato in alimentosNoConsumir:
        if dato != ',':
          stringAux = stringAux + dato
        elif dato == ',':
            listAlimentos.append(stringAux)
            stringAux = ''
    return listAlimentos