import csv
import random
from re import T
from alimentos import alimentos as alimentosTotal
from individuo import Individuo












# contador = 0
# listaAuxAlimentos = []
# listaAuxAlimentos.extend(separarAlimentos())

# if len(separarAlimentos()) != 1:
#     for i in separarAlimentos():

#         for alim in alimentosTotal.items():
#             if i == alim[0]:
#                 # print('encontre: ',i)
#                 sacar = listaAuxAlimentos.index(i)
#                 listaAuxAlimentos.pop(sacar)
#                 contador = contador +1   

# elif len(separarAlimentos()) == 1:
#     print('come de todo')
# print(listaAuxAlimentos)

dato = Individuo()
dato.caloriasConsumirIndividuo(alimentosTotal)
print(dato.toString())