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
        self.alimentosConsumir = {}

        self.alimentosDieta = []
        self.alimentosDieta_valor = []
        self.alimentosDieta_cantidad = []
        
        self.i_caloriasDieta = 0
        self.fenotipo = 0
        self.aptitud = 0
        

    

    def alimentos(self,listAlimentos,individual_alimentos):
        alimentosEliminar = []
        #lista de nombres de los alimentos que puede cosumir
        nombreAlimentosConsumir = []
        #alimentos que se eliminaran de la lista general
  
        alimentosEliminar = separarAlimentosNoConsumir(individual_alimentos)
        # print('Alimentos eliminar: ',alimentosEliminar)
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
            seleccionAlimentos = random.randint(0,len(nombreAlimentosConsumir)-1)
            #se saca el valor del alimento al azar

            valorDelAlimento = self.alimentosConsumir[nombreAlimentosConsumir[seleccionAlimentos]]
            #se guarda el alimento dentro de la dieta 
            cantidadCaolorias = (valorDelAlimento * cantidad) / 100

            # self.alimentosDieta[nombreAlimentosConsumir[seleccionAlimentos]] = cantidadCaolorias
            self.alimentosDieta.append(nombreAlimentosConsumir[seleccionAlimentos])
            self.alimentosDieta_valor.append(cantidadCaolorias)
            self.alimentosDieta_cantidad.append(cantidad)
            self.i_caloriasDieta = self.i_caloriasDieta + cantidadCaolorias
        
        



    def completarIndividuo(self,caloriasMaximas):
        self.fenotipo = caloriasMaximas - self.i_caloriasDieta

        self.aptitud = (self.fenotipo * 1000) / 15000



    def individuo_cruzado(self,listaNombres_datos,listavalores_datos,listaCantidad_datos):
        self.alimentosDieta = listaNombres_datos
        self.alimentosDieta_valor = listavalores_datos
        self.alimentosDieta_cantidad = listaCantidad_datos
        # print(self.alimentosDieta_valor)
        self.i_caloriasDieta = sum(self.alimentosDieta_valor)
        

    def indiduo_cruz_complementar(self,maximoConsumir):
        self.i_caloriasDieta = sum(self.alimentosDieta_valor)
        self.i_caloriasDieta

    def individuo_mutacion_completar(self,maxiConsumir):
        self.i_caloriasDieta = sum(self.alimentosDieta_valor)
        self.fenotipo = maxiConsumir - self.i_caloriasDieta
        self.aptitud = (self.fenotipo * 1000) / 15000


    def toString(self):
        return  f'alimentos: {self.alimentosDieta}\n'+f'alimentos_valores: {self.alimentosDieta_valor}\n'+f'cantidad: {self.alimentosDieta_cantidad}\n'+f'i calorias: {self.i_caloriasDieta}\n'+f'fenotipo: {self.fenotipo}\n'+f'Aptitud: {self.aptitud}'  


    
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