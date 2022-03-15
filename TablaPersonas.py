from re import I
import sys
import PySide6
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from matplotlib import widgets
from view import Ui_Dialog


class Dialogo(QMainWindow):
	
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.tableAlimentos.setColumnWidth(0,400)
		self.ui.botonMostrar.clicked.connect(self.getItems)
		
		# self.ui.botonAceptar.clicked.connect()
		
	def getItems(self):
		
		generos = ['Hombre','Hombre','Hombre','Hombre','Mujer']
		pesos = [93,78,63,85,56]
		estaturas = [180,175,175,183,155]
		edades = [20,20,20,21,20]
		tipoActividades = ['activo','medio activo','sedentario','medio activo','activo']
		alimentos = ['almejas, frambuesa, salsa_de_soya','Todo','pollo, pavo, pato, pavo',
			'anchoas atun bogavante calamar camarones/gambas cangrejo almejas mejillones pulpo ostras vieras',
			'ternera pato visceras venado bufalo carne_de_caza jamon_de_pollo jamon_serrano lomo_embuchado mortadela tofu_extra_firme natto escalfados pasados_por_agua cazuelas/gratinados chaffles muffins_de_huevo panqueques_de_huevo pasta_keto quesadillas_keto quiches acelgas alcachofas berenjena berzas brotes calabaza coliflor colinabo colrizada escarola esparragos grelos guisantes/arvejas_y_tirabeques hojas_de_mostaza hojas_de_nabo nabos nopal okra puerros raiz_de_apio rucula setas zapallo aceitunas ajo chalotas pepinillos coco nueces_pecanas nueces_de_Brasil nueces_de_macadamia nueces pinones brie feta kefir aceite_de_coco alioli mantequilla_de_almendras mostaza pesto vinagreta']
		
		index = self.ui.personas.currentIndex().row()
		
		self.ui.labelGenero.setText(generos[index])
		self.ui.labelPeso.setText(f'{pesos[index]}')
		self.ui.labelEstatura.setText(f'{estaturas[index]}')
		self.ui.labelEdad.setText(f'{edades[index]}')
		self.ui.labelAF.setText(tipoActividades[index])
		if alimentos[index] == 'Todo':			
			self.ui.tableAlimentos.clearContents()
			self.ui.tableAlimentos.setRowCount(1)
			a2= QTableWidgetItem('Le gustan todos los alimentos')
			self.ui.tableAlimentos.setItem(0,0,a2)

		else:
			alimen = alimentos[index].split()
			self.ui.tableAlimentos.setRowCount(len(alimen))
			self.ui.tableAlimentos.clearContents()
			
			for i in range (len(alimen)):
				alimen[i].replace(',','')
				
			row= 0
			for i in alimen:
				self.ui.tableAlimentos.setRowCount(row+1)
				a2= QTableWidgetItem('a')
				self.ui.tableAlimentos.setItem(row,0,a2)
				row +=1 
						
		
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
sys.exit(app.exec())