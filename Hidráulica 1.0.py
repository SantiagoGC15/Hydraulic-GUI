import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QColor, QPixmap
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import pyqtgraph as pg
import numpy as np
import sympy as sp
import math

from pyqtgraph.graphicsItems.ViewBox.axisCtrlTemplate_pyqt5 import *
from pyqtgraph.graphicsItems.PlotItem.plotConfigTemplate_pyqt5 import *
from pyqtgraph.imageview.ImageViewTemplate_pyqt5 import *
from pyqtgraph.console.template_pyqt5 import *

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

class ventana_principal(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_principal, self).__init__(parent)
        loadUi("Hidráulica.ui", self)
        
        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Sizegrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Configuración Geometría y Caudal
        self.geometria.clicked.connect(self.abrirMenuGeometrica)
        
        # Configuración Flujo Normal
        self.flujonormal.clicked.connect(self.abrirMenuFlujoNormal)
        
        # Configuración Flujo Critico
        self.flujocritico.clicked.connect(self.abrirMenuFlujoCritico)

        # Configuración Energía Específica
        self.energiaespecifica.clicked.connect(self.abrirMenuEnergiaEspecifica)
        
        # Configuración Estructuras de Control
        self.estructurascontrol.clicked.connect(self.abrirMenuEstructuras)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()
    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

    def abrirMenuGeometrica(self):
        self.hide()
        ventana2 = menuGeometrica(self)
        ventana2.show()
    
    def abrirMenuFlujoNormal(self):
        self.hide()
        ventana2 = menuFlujoNormal(self)
        ventana2.show()
    
    def abrirMenuFlujoCritico(self):
        self.hide()
        ventana2 = menuFlujoCritico(self)
        ventana2.show()

    def abrirMenuEnergiaEspecifica(self):
        self.hide()
        ventana2 = menuEnergiaEspecifica(self)
        ventana2.show()
        
    def abrirMenuEstructuras(self):
        self.hide()
        ventana2 = menuEstructuras(self)
        ventana2.show()
        
###################################### Error B<b ###################################################
class ventana_ErrorB(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_ErrorB, self).__init__(parent)
        loadUi("ErrorB.ui", self)
        
        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Control barra de titulos y boton aceptar
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.Aceptar.clicked.connect(lambda: self.close())

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
        
###################################### Error y3 ###################################################
class ventana_Errory3(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_Errory3, self).__init__(parent)
        loadUi("Errory3.ui", self)
        
        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Control barra de titulos y boton aceptar
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.Aceptar.clicked.connect(lambda: self.close())

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
        
###################################### Error Numérico ###################################################
class ventana_ErrorNumerico(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_ErrorNumerico, self).__init__(parent)
        loadUi("ErrorNumerico.ui", self)
        
        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Control barra de titulos y boton aceptar
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.Aceptar.clicked.connect(lambda: self.close())

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
    
###################################### Error Resultado ###################################################
class ventana_ErrorResultado(QMainWindow):

    def __init__(self, parent=None):
        super(ventana_ErrorResultado, self).__init__(parent)
        loadUi("ErrorResultado.ui", self)
        
        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Control barra de titulos y boton aceptar
        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.Aceptar.clicked.connect(lambda: self.close())

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
###################################### VENTANA-COEFICIENTE DE CORIOLIS #################################
class Coriolis(QMainWindow):

    def __init__(self, parent=None):
        super(Coriolis, self).__init__(parent)
        loadUi("Coriolis.ui", self)
        
        #Interactuar entre ventanas
        self.parent = parent
        self.Aceptar.clicked.connect(self.actualizarLineEdit)
        
        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar_2.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar_2.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

        #Combobox
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Tipo.addItem('')


        self.Tipo.addItem('Recto sin obstáculos')  
        self.Tipo.addItem('Rectangulares con paredes de madera') 
        self.Tipo.addItem('Rectangulares con obstáculos') 
        self.Tipo.addItem('Trapeciales con paredes de madera') 
        self.Tipo.addItem('Trapeciales con paredes de mampostería') 
        self.Tipo.addItem('Trapeciales excavados en tierra') 
        self.Tipo.addItem('Semicirculares revestidos de cemento') 
        self.Tipo.addItem('Semicirculares con fondo de arena y grava') 
        self.Tipo.addItem('Descarga de turbina Kaplan') 
        self.Tipo.addItem('Rectangulares, acueductos y de descarga en vertederos') 
        self.Tipo.addItem('Corrientes naturales y torrentes') 
        self.Tipo.addItem('Ríos de valle después de un meandro') 
        self.Tipo.addItem('Ríos bajo una cubierta de hielo') 
        self.Tipo.addItem('Ríos de valle desbordados en planicie') 
        self.Tipo.addItem('Si vo/vs=1.00') 
        self.Tipo.addItem('Si vo/vs=0.67') 
        self.Tipo.addItem('Si vo/vs=0.50') 
        self.Tipo.addItem('Si vo/vs=0.20') 
        self.Tipo.addItem('Si vo=0,vs=2V') 
        layout.addWidget(self.Tipo)

        self.Tipo.currentTextChanged.connect(self.seleccionTipo)

    def seleccionTipo(self):
        valor=self.Tipo.currentText()
        
        if valor=='Recto sin obstáculos':
            Coef=1.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='Rectangulares con paredes de madera':
            Coef=1.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='Rectangulares con obstáculos':
            Coef=1.41
            self.Coeficiente.setText(str(Coef))
        elif valor=='Trapeciales con paredes de madera':
            Coef=1.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='Trapeciales con paredes de mampostería':
            Coef=1.07
            self.Coeficiente.setText(str(Coef))
        elif valor=='Trapeciales excavados en tierra':
            Coef=1.1
            self.Coeficiente.setText(str(Coef))
        elif valor=='Semicirculares revestidos de cemento':
            Coef=1.025
            self.Coeficiente.setText(str(Coef))
        elif valor=='Semicirculares con fondo de arena y grava':
            Coef=1.09
            self.Coeficiente.setText(str(Coef))
        elif valor=='Descarga de turbina Kaplan':
            Coef=1.74
            self.Coeficiente.setText(str(Coef))
        elif valor=='Rectangulares, acueductos y de descarga en vertederos':
            Coef=1.15
            self.Coeficiente.setText(str(Coef))
        elif valor=='Corrientes naturales y torrentes':
            Coef=1.3
            self.Coeficiente.setText(str(Coef))
        elif valor=='Ríos de valle después de un meandro':
            Coef=1.35
            self.Coeficiente.setText(str(Coef))
        elif valor=='Ríos bajo una cubierta de hielo':
            Coef=1.5
            self.Coeficiente.setText(str(Coef))
        elif valor=='Ríos de valle desbordados en planicie':
            Coef=1.75
            self.Coeficiente.setText(str(Coef))
        elif valor=='Si vo/vs=1.00':
            Coef=1
            self.Coeficiente.setText(str(Coef))
        elif valor=='Si vo/vs=0.67':
            Coef=1.04
            self.Coeficiente.setText(str(Coef))
        elif valor=='Si vo/vs=0.50':
            Coef=1.09
            self.Coeficiente.setText(str(Coef))
        elif valor=='Si vo/vs=0.20':
            Coef=1.09
            self.Coeficiente.setText(str(Coef))
        elif valor=='Si vo=0,vs=2V':
            Coef=2
            self.Coeficiente.setText(str(Coef))
            
    def updateCaracteristicas(self, index):
        self.Caracteristicas.clear()
        caract = self.Tipo.itemData(index)
        if caract:
            self.Caracteristicas.addItems(caract)

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()
    
    def actualizarLineEdit(self):
        # Obtener texto del QLineEdit
        texto = self.Coeficiente.text()

        # Insertar texto en el QLineEdit de la ventana principal
        self.parent.Coriolis.setText(texto)  

###################################### VENTANA-COEFICIENTE DE MANNING #################################
class Manning(QMainWindow):

    def __init__(self, parent=None):
        super(Manning, self).__init__(parent)
        loadUi("Manning.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Interactuar entre ventanas
        self.parent = parent
        self.Aceptar.clicked.connect(self.actualizarLineEdit)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()
            
        #Combobox
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Tipo.addItem('')
        self.Caracteristicas.addItem('')

        self.Tipo.addItem('Canales revestidos o desarmables', ['Acero corrugado', 'Acero pintado', 'Acero sin pintar', 'Asfalto Liso',
                                                               'Asfalto Rugoso', 'Bloques de Piedra Labrados', 'Cemento Mortero', 'Cemento Pulido',
                                                               'Concreto Lanzado','Concetro Pulido con grava en el fondo','Concreto sobre roca', 'Concreto, Terminado llana madera',
                                                               'Concreto, Terminado llana metálica', 'Fondo de concreto, lados de mampostería de piedra',
                                                               'Fondo de concreto, lados de piedra labrada', 'Fondo de concreto, lados de piedra suelta',
                                                               'Fondo de gravas, lados de concreto encofrado', 'Fondo de gravas, lados de piedra', 'Ladrillo, Barnizado',
                                                               'Madera Cepillada', 'Madera sin cepillar', 'Mampostería, piedra cementada', 'Mampostería, Piedra suelta', 'Revestimiento vegetal'])  
        self.Tipo.addItem('Cauces Naturales, con ancho mayor a 30 metros', ['Sección irregular y rugosa', 'Sección rectangular, sin cantos rodados, ni matorrales'])  
        self.Tipo.addItem('Cauces Naturales, con ancho menor a 30 metros', ['Corrientes montañosas, sin vegetación, fondo: cantos rodados y rocas grandes', 
                                                                            'Corrientes montañosas, sin vegetación, fondo: Gravas y algunas rocas', 
                                                                            'En planicies, canales de crecientes con muchos árboles con matorrales', 'En planicies, limpio, recto, máximo nivel, con piedras y maleza',
                                                                            'En planicies, limpio, recto, máximo nivel, sin montículos', 'En planicies, limpio, serpenteante, algunos matorrales y muchas piedras', 
                                                                            'En planicies, limpio, serpenteante, algunos matorrales y piedras', 'En planicies, limpio, serpenteante, algunos pozos y banco de arena',
                                                                            'En planicies, limpio, serpenteante, niveles bajos', 'En planicies, tramos con mucha maleza, pozos profundos',
                                                                            'En planicies, tramos lentos con malezas y pozos profundos'])  
        self.Tipo.addItem('Cauces naturales, planicies de inundación', ['Arboles, densos, troncos caídos, nivel alto', 'Arboles, densos, troncos caídos, nivel bajo',
                                                                        'Arboles, sauces denso, rectos, verano', 'Arboles, terreno limpio, con troncos sin retoños',
                                                                        'Arboles, terreno limpio, con troncos y muchos retoños', 'Áreas cultivadas, campos de cultivos maduros',
                                                                        'Áreas cultivadas, cultivos en línea maduros', 'Áreas cultivadas, sin cultivo',
                                                                        'Matorrales, dispersos, arboles, en invierno', 'Matorrales, dispersos, arboles, en verano',
                                                                        'Matorrales, dispersos, mucha maleza', 'Matorrales, medios a densos, invierno',
                                                                        'Matorrales, medios a densos, verano', 'Pastizales, sin matorrales, pastos alto',
                                                                        'Pastizales, sin matorrales, pastos corto'])  
        self.Tipo.addItem('Conductos cerrados que fluyen parcialmente llenos', ['Acero','Arcilla','Concreto alcantarillado','Concreto bien terminado', 'Concreto sin pulir', 'Hierro forjado',
                                                                                'Hierro fundido','Latón','Lucita','Madera', 'Mampostería de ladrillo', 'Mampostería de piedra', 'Metal corrugado', 'Vidrio'])
        self.Tipo.addItem('Excavado o dragrado', ['Cortes en roca, afilados e irregulares','Cortes en roca, lisos y uniformes', 'En tierra, recto, limpio recién terminado',
                                                  'En tierra, recto, limpio, con grava, uniforme', 'En tierra, recto, limpio, expuesto a la intemperie',
                                                  'En tierra, recto, pasto corto, y algunas malezas', 'En tierra, serpenteante y lento, fondo cantos rodados, lados limpios',
                                                  'En tierra, serpenteante y lento, fondo pedregoso y bancas maleza','En tierra, serpenteante y lento, fondo tierra, lados piedra',
                                                  'En tierra, serpenteante y lento, maleza densa','En tierra, serpenteante y lento, pastos y algunas malezas',
                                                  'En tierra, serpenteante y lento, sin vegetación','Excavado, matorrales ligeros', 'Excavado, sin vegetación',
                                                  'Sin mantenimiento, fondo limpio, lados con matorrales', 'Sin mantenimiento, igual, nivel máximo de flujo', 'Sin mantenimiento, malezas, densas', 
                                                  'Sin mantenimiento, matorrales densos, nivel alto'])
        
        layout.addWidget(self.Tipo)

        layout.addWidget(self.Caracteristicas)

        self.Tipo.currentIndexChanged.connect(self.updateCaracteristicas)

        self.updateCaracteristicas(self.Tipo.currentIndex())

        #Boton aceptar
        self.Caracteristicas.currentTextChanged.connect(self.seleccionTipo)

    def seleccionTipo(self):
        valor=self.Caracteristicas.currentText()
        
        if valor=='Acero corrugado':
            Coef=0.025
            self.Coeficiente.setText(str(Coef))
        elif valor=='Sin mantenimiento, matorrales densos, nivel alto':
            Coef=0.1
            self.Coeficiente.setText(str(Coef))
        elif valor=='Sin mantenimiento, malezas, densas':
            Coef=0.08
            self.Coeficiente.setText(str(Coef))
        elif valor=='Sin mantenimiento, igual, nivel máximo de flujo':
            Coef=0.07
            self.Coeficiente.setText(str(Coef))
        elif valor=='Sin mantenimiento, fondo limpio, lados con matorrales':
            Coef=0.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='Excavado, sin vegetación':
            Coef=0.028
            self.Coeficiente.setText(str(Coef))
        elif valor=='Excavado, matorrales ligeros':
            Coef=0.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, serpenteante y lento, sin vegetación':
            Coef=0.025
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, serpenteante y lento, pastos y algunas malezas':
            Coef=0.03
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, serpenteante y lento, maleza densa':
            Coef=0.035
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, serpenteante y lento, fondo tierra, lados piedra':
            Coef=0.03
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, serpenteante y lento, fondo pedregoso y bancas maleza':
            Coef=0.035
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, serpenteante y lento, fondo cantos rodados, lados limpios':
            Coef=0.04
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, recto, pasto corto, y algunas malezas':
            Coef=0.027
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, recto, limpio, expuesto a la intemperie':
            Coef=0.022
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, recto, limpio, con grava, uniforme':
            Coef=0.025
            self.Coeficiente.setText(str(Coef))
        elif valor=='En tierra, recto, limpio recién terminado':
            Coef=0.035
            self.Coeficiente.setText(str(Coef))
        elif valor=='Cortes en roca, lisos y uniformes':
            Coef=0.035
            self.Coeficiente.setText(str(Coef))
        elif valor=='Acero pintado':
            Coef=0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Acero sin pintar':
            Coef = 0.012
            self.Coeficiente.setText(str(Coef))
        elif valor=='Asfalto Liso':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Asfalto Rugoso':
            Coef = 0.016
            self.Coeficiente.setText(str(Coef))
        elif valor=='Bloques de Piedra Labrados':
            Coef = 0.015
            self.Coeficiente.setText(str(Coef))
        elif valor=='Cemento Mortero':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Cemento Pulido':
            Coef = 0.011
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concreto Lanzado':
            Coef = 0.019
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concetro Pulido con grava en el fondo':
            Coef = 0.017
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concreto sobre roca':
            Coef = 0.022
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concreto, Terminado llana madera':
            Coef = 0.015
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concreto, Terminado llana metálica':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Fondo de concreto, lados de mampostería de piedra':
            Coef = 0.025
            self.Coeficiente.setText(str(Coef))
        elif valor=='Fondo de concreto, lados de piedra labrada':
            Coef = 0.017
            self.Coeficiente.setText(str(Coef))
        elif valor=='Fondo de concreto, lados de piedra suelta':
            Coef = 0.03
            self.Coeficiente.setText(str(Coef))
        elif valor=='Fondo de gravas, lados de concreto encofrado':
            Coef = 0.02
            self.Coeficiente.setText(str(Coef))
        elif valor=='Fondo de gravas, lados de piedra':
            Coef = 0.023
            self.Coeficiente.setText(str(Coef))
        elif valor=='Ladrillo, Barnizado':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Madera Cepillada':
            Coef = 0.012
            self.Coeficiente.setText(str(Coef))
        elif valor=='Madera sin cepillar':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Mampostería, piedra cementada':
            Coef = 0.025
            self.Coeficiente.setText(str(Coef))
        elif valor=='Mampostería, Piedra suelta':
            Coef = 0.032
            self.Coeficiente.setText(str(Coef))
        elif valor=='Revestimiento vegetal':
            Coef = 0.04
            self.Coeficiente.setText(str(Coef))
        elif valor=='Sección irregular y rugosa':
            Coef = 0.068
            self.Coeficiente.setText(str(Coef))
        elif valor=='Sección rectangular, sin cantos rodados, ni matorrales':
            Coef = 0.043
            self.Coeficiente.setText(str(Coef))
        elif valor=='Corrientes montañosas, sin vegetación, fondo: cantos rodados y rocas grandes':
            Coef = 0.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='Corrientes montañosas, sin vegetación, fondo: gravas y algunas rocas':
            Coef = 0.04
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, canales de crecientes con muchos árboles con matorrales':
            Coef = 0.1
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, limpio, recto, máximo nivel, con piedras y maleza':
            Coef = 0.035
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, limpio, recto, máximo nivel, sin montículos':
            Coef = 0.035
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, limpio, serpenteante, algunos matorrales y muchas piedras':
            Coef = 0.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, limpio, serpenteante, algunos matorrales y piedras':
            Coef = 0.045
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, limpio, serpenteante, algunos pozos y banco de arena':
            Coef = 0.04
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, limpio, serpenteante, niveles bajos':
            Coef = 0.048
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, tramos con mucha maleza, pozos profundos':
            Coef = 0.1
            self.Coeficiente.setText(str(Coef))
        elif valor=='En planicies, tramos lentos con malezas y pozos profundos':
            Coef = 0.07
            self.Coeficiente.setText(str(Coef))
        elif valor=='Arboles, densos, troncos caídos, nivel alto':
            Coef = 0.12
            self.Coeficiente.setText(str(Coef))
        elif valor=='Arboles, densos, troncos caídos, nivel bajo':
            Coef = 0.1
            self.Coeficiente.setText(str(Coef))   
        elif valor=='Arboles, sauces denso, rectos, verano':
            Coef = 0.15
            self.Coeficiente.setText(str(Coef))
        elif valor=='Arboles, terreno limpio, con troncos sin retoños':
            Coef = 0.04
            self.Coeficiente.setText(str(Coef))
        elif valor=='Arboles, terreno limpio, con troncos y muchos retoños':
            Coef = 0.06
            self.Coeficiente.setText(str(Coef))
        elif valor=='Áreas cultivadas, campos de cultivos maduros':
            Coef = 0.04
            self.Coeficiente.setText(str(Coef))
        elif valor=='Áreas cultivadas, cultivos en línea maduros':
            Coef = 0.035
            self.Coeficiente.setText(str(Coef))
        elif valor=='Áreas cultivadas, sin cultivo':
            Coef = 0.03
            self.Coeficiente.setText(str(Coef))
        elif valor=='Matorrales, dispersos, arboles, en invierno':
            Coef = 0.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='Matorrales, dispersos, arboles, en verano':
            Coef = 0.06
            self.Coeficiente.setText(str(Coef))
        elif valor=='Matorrales, dispersos, mucha maleza':
            Coef = 0.05
            self.Coeficiente.setText(str(Coef))
        elif valor=='Matorrales, medios a densos, invierno':
            Coef = 0.07
            self.Coeficiente.setText(str(Coef))
        elif valor=='Matorrales, medios a densos, verano':
            Coef = 0.1
            self.Coeficiente.setText(str(Coef))
        elif valor=='Pastizales, sin matorrales, pastos alto':
            Coef = 0.35
            self.Coeficiente.setText(str(Coef))
        elif valor=='Pastizales, sin matorrales, pastos corto':
            Coef = 0.3
            self.Coeficiente.setText(str(Coef))
        elif valor=='Acero':
            Coef = 0.012
            self.Coeficiente.setText(str(Coef))
        elif valor=='Arcilla':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concreto alcantarillado':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concreto bien terminado':
            Coef = 0.012
            self.Coeficiente.setText(str(Coef))
        elif valor=='Concreto sin pulir':
            Coef = 0.014
            self.Coeficiente.setText(str(Coef))
        elif valor=='Hierro forjado':
            Coef = 0.014
            self.Coeficiente.setText(str(Coef))
        elif valor=='Hierro fundido':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Latón':
            Coef = 0.01
            self.Coeficiente.setText(str(Coef))
        elif valor=='Lucita':
            Coef = 0.009
            self.Coeficiente.setText(str(Coef))
        elif valor=='Madera':
            Coef = 0.017
            self.Coeficiente.setText(str(Coef))
        elif valor=='Mampostería de ladrillo':
            Coef = 0.013
            self.Coeficiente.setText(str(Coef))
        elif valor=='Mampostería de piedra':
            Coef = 0.025
            self.Coeficiente.setText(str(Coef))
        elif valor=='Metal corrugado':
            Coef = 0.019
            self.Coeficiente.setText(str(Coef))
        elif valor=='Vidrio':
            Coef = 0.01
            self.Coeficiente.setText(str(Coef))
        elif valor=='Cortes en roca, afilados e irregulares':
            Coef = 0.04
            self.Coeficiente.setText(str(Coef))
    
    def actualizarLineEdit(self):
        # Obtener texto del QLineEdit
        texto = self.Coeficiente.text()

        # Insertar texto en el QLineEdit de la ventana principal
        self.parent.Manning.setText(texto)   
        
    def updateCaracteristicas(self, index):
        self.Caracteristicas.clear()
        caract = self.Tipo.itemData(index)
        if caract:
            self.Caracteristicas.addItems(caract)

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()
###################################### VENTANA MENU GEOMETRICA ######################################

class menuGeometrica(QMainWindow):

    def __init__(self, parent=None):
        super(menuGeometrica, self).__init__(parent)
        loadUi("Menú_Geometrica.ui", self)

        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        
        #Control de botones
        self.Trapezoidal.clicked.connect(self.abrirTrape)
        self.Circular.clicked.connect(self.abrirCircular)
        self.Parabolica.clicked.connect(self.abrirParabo)
        self.Atras.clicked.connect(self.AbrirVP)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()


    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
        
    def control_bt_minimizar(self):
        self.showMinimized()
        
    def abrirTrape(self):
        self.hide()
        ventana2 = GeometriaTrapezoidal(self)
        ventana2.show()

    def abrirParabo(self):
        self.hide()
        ventana2 = GeometriaParabolica(self)
        ventana2.show()

    def abrirCircular(self):
        self.hide()
        ventana2 = GeometriaCircular(self)
        ventana2.show()

    def AbrirVP(self):
        self.hide()
        ventana2 = ventana_principal(self)
        ventana2.show()

####################### VENTANA GEOMETRIA-SECCION TRAPEZOIDALl,Rec,Trian #######################
class GeometriaTrapezoidal(QMainWindow):

    def __init__(self, parent=None):
        super(GeometriaTrapezoidal, self).__init__(parent)
        loadUi("GeometriaTrapezoidal.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Combobox
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Incognita.addItem('')
        self.Incognita.addItem('Tirante (y)')
        self.Incognita.addItem('Base (b)')
        self.Incognita.addItem('Estándar')
        layout.addWidget(self.Incognita)
        
        self.Incognita.currentTextChanged.connect(self.on_combobox_changed)
        
        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
        
    def on_combobox_changed(self, value):
        Inc=self.Incognita.currentText()
        
        if Inc=='Tirante (y)':
            self.TVariable.setText('Base (b)')
            self.TVariable_2.setText('Área Hidráulica (A)')
            self.TituloR_incognita.setText('Tirante (y)')
        elif Inc=='Base (b)':
            self.TVariable.setText('Tirante (y)')
            self.TVariable_2.setText('Área Hidráulica (A)')
            self.TituloR_incognita.setText('Base (b)')
        elif Inc=='Estándar':
            self.TVariable.setText('Tirante (y)')
            self.TVariable_2.setText('Base (b)')
            self.TituloR_incognita.setText('Área Hidráulica (A)')
            
    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuGeometrica(self)
        ventana2.show()
        
    def limpiar(self):
        self.R_incognita.setText("")
        self.Variable.setText("")
        self.Variable2.setText("")
        self.Perimetro.setText("")
        self.Taludk1.setText("")
        self.Taludk2.setText("")
        self.Radio.setText("")
        self.Ancho.setText("")
        self.Imagen.clear()
    
    def calculos(self):
        
        Inc=self.Incognita.currentText()
        
        if Inc=='Tirante (y)':
            A=self.Variable2.text()
            b=self.Variable.text()
            k1=self.Taludk1.text()
            k2=self.Taludk2.text()
        
            if isfloat(A) and isfloat(b) and isfloat(k1) and isfloat(k2):
                A=float(self.Variable2.text())
                b=float(self.Variable.text())
                k1=float(self.Taludk1.text())
                k2=float(self.Taludk2.text())
                
                if k1!=0 and k2!=0 and b!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    y=round((-b+np.sqrt(b**2+2*A*(k1+k2)))/(k1+k2),4)
                    P=round(b+y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(b+y*(k1+k2),4)
                    Rh=round(A/P,4) 
            
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(y))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                    
                elif k1==0 and k2==0 and b!=0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    y=round(A/b,4)
                    P=round(b+2*y,4)
                    T=round(b,4)
                    Rh=round(A/P,4)
                    
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(y))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                
                elif b==0:
                    qpixmap=QPixmap('Triangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    y=round(np.sqrt(2*A/(k1+k2)))
                    P=round(y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(y*(k1+k2),4)
                    Rh=round(A/P,4)
                    
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(y))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                    
            else: ventana_ErrorNumerico(self).show() 
                
        elif Inc=='Base (b)':
            A=self.Variable2.text()
            y=self.Variable.text() 
            k1=self.Taludk1.text()
            k2=self.Taludk2.text()
        
            if isfloat(A) and isfloat(y) and isfloat(k1) and isfloat(k2) and y!=0:
                A=float(self.Variable2.text())
                y=float(self.Variable.text())
                k1=float(self.Taludk1.text())
                k2=float(self.Taludk2.text())
                
                if k1!=0 and k2!=0 and b!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    b=round((2*A-y**2*(k1+k2))/2*y,4)
                    P=round(b+y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(b+y*(k1+k2),4)
                    Rh=round(A/P,4) 
                
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(b))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                    
                elif k1==0 and k2==0 and b!=0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    b=round(2*A/2*y,4)
                    P=round(b+2*y,4)
                    T=round(b,4)
                    Rh=round(A/P,4) 
                
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(b))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
            
            else: ventana_ErrorNumerico(self).show() 
                
        elif Inc=='Estándar':
            y=self.Variable.text() 
            b=self.Variable2.text()
            k1=self.Taludk1.text()
            k2=self.Taludk2.text()
        
            if isfloat(y) and isfloat(b) and isfloat(k1) and isfloat(k2):
                y=float(self.Variable.text())
                b=float(self.Variable2.text())
                k1=float(self.Taludk1.text())
                k2=float(self.Taludk2.text())
                
                if k1!=0 and k2!=0 and b!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    A=round(b*y+((k1+k2)/2)*y**2,4)
                    P=round(b+y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(b+y*(k1+k2),4)
                    Rh=round(A/P,4) 
                
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(A))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                    
                elif k1==0 and k2==0 and b!=0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    A=round(b*y,4)
                    P=round(b+2*y,4)
                    T=round(b,4)
                    Rh=round(A/P,4) 
                
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(A))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                    
                elif b==0:
                    qpixmap=QPixmap('Triangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    A=round(((k1+k2)/2)*y**2,4)
                    P=round(y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(y*(k1+k2),4)
                    Rh=round(A/P,4)
                    
                    self.Perimetro.setText(str(P))
                    self.R_incognita.setText(str(A))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                    
            else: ventana_ErrorNumerico(self).show()        

####################### VENTANA GEOMETRIA-SECCION PARABOLICA #######################
class GeometriaParabolica(QMainWindow):

    def __init__(self, parent=None):
        super(GeometriaParabolica, self).__init__(parent)
        loadUi("GeometriaParabolica.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuGeometrica(self)
        ventana2.show()
    
    def limpiar(self):
        self.Tirante.setText("")
        self.Ancho.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.ConstanteK.setText("")
        
    def calculos(self):
        
        y=self.Tirante.text()
        T=self.Ancho.text()
        
        if isfloat(y) and isfloat(T):
            y=float(self.Tirante.text())
            T=float(self.Ancho.text())
            
            A=round(2/3*T*y,4)
            k=round((4*y)/T**2,4)
            Xa=round(4*y/T,4)
            raiz=round(np.sqrt(1+Xa**2),4)
            Rh=round((2*T**2*y)/(3*T+8*y**2),4)

            if 0<Xa<=1:
                P=round(T+8/3*(y**2/T),4)
            else:
                P=round(T/2*(raiz+(1/Xa)*np.log(Xa+raiz)),4)
            
            self.Perimetro.setText(str(P))
            self.Area.setText(str(A))
            self.Radio.setText(str(Rh))
            self.ConstanteK.setText(str(k))
            
        else: ventana_ErrorNumerico(self).show() 
            
####################### VENTANA GEOMETRIA-SECCION CIRCULAR #######################
class GeometriaCircular(QMainWindow):

    def __init__(self, parent=None):
        super(GeometriaCircular, self).__init__(parent)
        loadUi("GeometriaCircular.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuGeometrica(self)
        ventana2.show()
    
    def limpiar(self):
        self.Tirante.setText("")
        self.Diametro.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.Ancho.setText("")
    
    def calculos(self):
        
        y=self.Tirante.text()
        D=self.Diametro.text()
        
        if isfloat(y) and isfloat(D):
            y=float(self.Tirante.text())
            D=float(self.Diametro.text())
            
            r=D/2
            theta=2*np.arccos(1-y/r)
            A=round((D**2/8)*(theta-np.sin(theta)),4)
            P=round((theta*D)/2,4)
            Rh=round(D/4*(1-np.sin(theta)/theta),4)
            T=round(D*np.sin(theta/2),4)
            
            self.Perimetro.setText(str(P))
            self.Area.setText(str(A))
            self.Radio.setText(str(Rh))
            self.Ancho.setText(str(T))
            
        else: ventana_ErrorNumerico(self).show() 

###################################### VENTANA MENU FLUJO NORMAL ######################################

class menuFlujoNormal(QMainWindow):

    def __init__(self, parent=None):
        super(menuFlujoNormal, self).__init__(parent)
        loadUi("Menú_FNormalyCritico.ui", self)

        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #Control de botones
        self.Trapezoidal.clicked.connect(self.abrirTrape)
        self.Circular.clicked.connect(self.abrirCircular)
        self.Atras.clicked.connect(self.AbrirVP)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()


    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def abrirTrape(self):
        self.hide()
        ventana2 = FNormalTrapezoidal(self)
        ventana2.show()

    def abrirCircular(self):
        self.hide()
        ventana2 = FNormalCircular(self)
        ventana2.show()

    def AbrirVP(self):
        self.hide()
        ventana2 = ventana_principal(self)
        ventana2.show()

####################### VENTANA FLUJO NORMAL-SECCION TRAPEZOIDAL #######################
class FNormalTrapezoidal(QMainWindow):

    def __init__(self, parent=None):
        super(FNormalTrapezoidal, self).__init__(parent)
        loadUi("FNormalTrapezoidal.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Combobox
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Incognita.addItem('')
        self.Incognita.addItem('Tirante (y)')
        self.Incognita.addItem('Base (b)')
        self.Incognita.addItem('Pendiente (S)')
        layout.addWidget(self.Incognita)
        
        self.Incognita.currentTextChanged.connect(self.on_combobox_changed)
        
        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        self.Coeficientes.clicked.connect(self.AbrirManning)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()
    
    def on_combobox_changed(self, value):
        Inc=self.Incognita.currentText()
        
        if Inc=='Tirante (y)':
            self.TVariable.setText('Pendiente (S)')
            self.TVariable_2.setText('Base (b)')
            self.TVariable_3.setText('')
            self.TituloR_incognita.setText('Tirante (y)')
            self.TituloR_incognita_2.setText('Velocidad (v)')
            self.TituloR_incognita_3.setText('Área Hidráulica (A)')
        elif Inc=='Base (b)':
            self.TVariable_2.setText('Tirante (y)')
            self.TVariable_3.setText('Área Hidráulica (A)')
            self.TVariable.setText('Pendiente (S)')
            self.TituloR_incognita.setText('Base (b)')
            self.TituloR_incognita_2.setText('Velocidad (v)')
            self.TituloR_incognita_3.setText('')
        elif Inc=='Pendiente (S)':
            self.TVariable.setText('Tirante (y)')
            self.TVariable_2.setText('Velocidad (v)')
            self.TVariable_3.setText('Área Hidráulica (A)')
            self.TituloR_incognita.setText('Pendiente (S)')
            self.TituloR_incognita_2.setText('Base (b)')
            self.TituloR_incognita_3.setText('')  

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuFlujoNormal(self)
        ventana2.show()
        
    def AbrirManning(self):
        ventana=Manning(self)
        ventana.show()
        
    def limpiar(self):
        self.R_incognita.setText("")
        self.Manning.setText("")
        self.Froude.setText("")
        self.Regimen.setText("")
        self.R_incognita2.setText("")
        self.Energia.setText("")
        self.Variable2.setText("")
        self.Variable.setText("")
        self.Caudal.setText("")
        self.Taludk1.setText("")
        self.Taludk2.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.Ancho.setText("")
        self.Imagen.clear()
    
    def calculos(self):
        Inc=self.Incognita.currentText()
            
        if Inc=='Tirante (y)':
            S=self.Variable.text()
            b=self.Variable2.text()
            n=self.Manning.text()
            Q=self.Caudal.text()
            k1=self.Taludk1.text()
            k2=self.Taludk2.text()
        
            if isfloat(Q) and isfloat(b) and isfloat(k1) and isfloat(k2) and isfloat(S) and isfloat(n):
                def newton(f,Df,x0,epsilon=0.0001,max_iter=50):
                    xn = x0
                    for n in range(0,max_iter):
                        fxn = f.subs(y1,xn)
                        if abs(fxn) < epsilon:
                            return xn
                        Dfxn = Df.subs(y1,xn)
                        if Dfxn == 0:
                            return None
                        xn = xn - fxn/Dfxn
                    return None
                
                g=9.806665
                n=float(n)
                S=float(S)
                Q=float(Q)
                b=float(b)
                k1=float(k1)
                k2=float(k2)
                
                if k1!=0 and k2!=0 and b!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    'Ecuaciones Simbólicas'
                    y1=sp.Symbol('y1')
                    Al=b*y1+((k1+k2)/2)*y1**2
                    Pl=b+y1*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2))
                    Kn=n*Q/np.sqrt(S)
                    fy=Al**(5/3)/Pl**(2/3)-Kn
                    diffy=sp.diff(fy,y1)

                    y=float(newton(fy,diffy,b))

                    'Ecuaciones numéricas'
                    A=b*y+((k1+k2)/2)*y**2
                    P=b+y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2))
                    T=b+y*(k1+k2)
                    Rh=A/P
                    v=1/n*Rh**(2/3)*np.sqrt(S)
                    Ep=y+Q**2/(2*g*A**2)
                    Fr=v/(g*A/T)**0.5
            
                    self.R_incognita.setText(str(round(y,4)))
                    self.R_incognita2.setText(str(round(v,4)))
                    self.Energia.setText(str(round(Ep,4)))
                    self.Froude.setText(str(round(Fr,4)))
                    self.Perimetro.setText(str(round(P,4)))
                    self.Area.setText(str(round(A,4)))
                    self.Radio.setText(str(round(Rh,4)))
                    self.Ancho.setText(str(round(T,4)))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                        
                elif k1==0 and k2==0 and b!=0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    'Ecuaciones Simbólicas'
                    y1=sp.Symbol('y1')
                    Al=b*y1
                    Pl=b+2*y1
                    Kn=n*Q/np.sqrt(S)
                    fy=Al**(5/3)/Pl**(2/3)-Kn
                    diffy=sp.diff(fy,y1)

                    y=float(newton(fy,diffy,b))

                    'Ecuaciones numéricas'
                    A=b*y
                    P=b+2*y
                    T=b
                    Rh=A/P
                    v=1/n*Rh**(2/3)*np.sqrt(S)
                    Ep=y+Q**2/(2*g*A**2)
                    Fr=v/(g*A/T)**0.5
            
                    self.R_incognita.setText(str(round(y,4)))
                    self.Velocidad.setText(str(round(v,4)))
                    self.Energia.setText(str(round(Ep,4)))
                    self.Froude.setText(str(round(Fr,4)))
                    self.Perimetro.setText(str(round(P,4)))
                    self.Area.setText(str(round(A,4)))
                    self.Radio.setText(str(round(Rh,4)))
                    self.Ancho.setText(str(round(T,4)))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                    
                elif b==0:
                    qpixmap=QPixmap('Triangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    'Ecuaciones Simbólicas'
                    y1=sp.Symbol('y1')
                    Al=((k1+k2)/2)*y1**2
                    Pl=y1*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2))
                    Kn=n*Q/np.sqrt(S)
                    fy=Al**(5/3)/Pl**(2/3)-Kn
                    diffy=sp.diff(fy,y1)

                    y=float(newton(fy,diffy,b))

                    'Ecuaciones numéricas'
                    A=((k1+k2)/2)*y**2
                    P=y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2))
                    T=y*(k1+k2)
                    Rh=A/P
                    v=1/n*Rh**(2/3)*np.sqrt(S)
                    Ep=y+Q**2/(2*g*A**2)
                    Fr=v/(g*A/T)**0.5
            
                    self.R_incognita.setText(str(round(y,4)))
                    self.Velocidad.setText(str(round(v,4)))
                    self.Energia.setText(str(round(Ep,4)))
                    self.Froude.setText(str(round(Fr,4)))
                    self.Perimetro.setText(str(round(P,4)))
                    self.Area.setText(str(round(A,4)))
                    self.Radio.setText(str(round(Rh,4)))
                    self.Ancho.setText(str(round(T,4)))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')    
            else: ventana_ErrorNumerico(self).show() 
                
        if Inc=='Base (b)':
            S=self.Variable.text()
            y=self.Variable2.text()
            A=self.Variable3.text()
            n=self.Manning.text()
            Q=self.Caudal.text()
            k1=self.Taludk1.text()
            k2=self.Taludk2.text() 
            
            if isfloat(Q) and isfloat(A) and isfloat(k1) and isfloat(k2) and isfloat(y) and isfloat(n) and isfloat(S):
                g=9.806665
                S=float(S)
                A=float(A)
                y=float(y)
                Q=float(Q)
                n=float(n)
                k1=float(k1)
                k2=float(k2)
                
                if k1!=0 and k2!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)

                    'Ecuaciones numéricas'
                    b=round((2*A-y**2*(k1+k2))/2*y,4)
                    P=round(b+y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(b+y*(k1+k2),4)
                    Rh=round(A/P,4) 
                    v=round(1/n*Rh**(2/3)*np.sqrt(S),4)
                    Ep=round(y+Q**2/(2*g*A**2),4)
                    Fr=round(v/(g*A/T)**0.5,4)
            
                    self.R_incognita.setText(str(b))
                    self.R_incognita2.setText(str(v))
                    self.Energia.setText(str(Ep))
                    self.Froude.setText(str(Fr))
                    self.Perimetro.setText(str(P))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                        
                elif k1==0 and k2==0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)

                    'Ecuaciones numéricas'
                    b=round(2*A,4)
                    P=round(b+2*y,4)
                    T=round(b,4)
                    Rh=round(A/P,4) 
                    v=round(1/n*Rh**(2/3)*np.sqrt(S),4)
                    Ep=round(y+Q**2/(2*g*A**2),4)
                    Fr=round(v/(g*A/T)**0.5,4)
            
                    self.R_incognita.setText(str(b))
                    self.R_incognita2.setText(str(v))
                    self.Energia.setText(str(Ep))
                    self.Froude.setText(str(Fr))
                    self.Perimetro.setText(str(P))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                    
            else: ventana_ErrorNumerico(self).show() 
        
        if Inc=='Pendiente (S)':
            y=self.Variable.text()
            A=self.Variable2.text()
            v=self.Variable3.text()
            n=self.Manning.text()
            Q=self.Caudal.text()
            k1=self.Taludk1.text()
            k2=self.Taludk2.text() 
            
            if isfloat(Q) and isfloat(A) and isfloat(k1) and isfloat(k2) and isfloat(y) and isfloat(n) and isfloat(v):
                g=9.806665
                A=float(A)
                y=float(y)
                v=float(y)
                n=float(n)
                Q=float(Q)
                k1=float(k1) 
                k2=float(k2) 
                
                if k1!=0 and k2!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)

                    'Ecuaciones numéricas'
                    b=round((2*A-y**2*(k1+k2))/2*y,4)
                    P=round(b+y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(b+y*(k1+k2),4)
                    Rh=round(A/P,4) 
                    S=(n**2*v**2)/Rh**(4/3)
                    Ep=round(y+Q**2/(2*g*A**2),4)
                    Fr=round(v/(g*A/T)**0.5,4)
            
                    self.R_incognita.setText(str(S))
                    self.R_incognita2.setText(str(b))
                    self.Energia.setText(str(Ep))
                    self.Froude.setText(str(Fr))
                    self.Perimetro.setText(str(P))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                        
                elif k1==0 and k2==0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)

                    'Ecuaciones numéricas'
                    b=round(2*A,4)
                    P=round(b+2*y,4)
                    T=round(b,4)
                    Rh=round(A/P,4) 
                    S=(n**2*v**2)/Rh**(4/3)
                    Ep=round(y+Q**2/(2*g*A**2),4)
                    Fr=round(v/(g*A/T)**0.5,4)
            
                    self.R_incognita.setText(str(S))
                    self.R_incognita2.setText(str(b))
                    self.Energia.setText(str(Ep))
                    self.Froude.setText(str(Fr))
                    self.Perimetro.setText(str(P))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                        
            else: ventana_ErrorNumerico(self).show() 
####################### VENTANA FLUJO NORMAL-SECCION CIRCULAR #######################
class FNormalCircular(QMainWindow):

    def __init__(self, parent=None):
        super(FNormalCircular, self).__init__(parent)
        loadUi("FNormalCircular.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        self.Coeficientes.clicked.connect(self.AbrirManning)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuFlujoNormal(self)
        ventana2.show()
        
    def AbrirManning(self):
        ventana=Manning(self)
        ventana.show()
        
    def limpiar(self):
        self.Pendiente.setText("")
        self.Froude.setText("")
        self.Velocidad.setText("")
        self.Tirante.setText("")
        self.Regimen.setText("")
        self.Energia.setText("")
        self.Manning.setText("")
        self.Ancho.setText("")
        self.Caudal.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.Diametro.setText("")
    
    def calculos(self):
        
        D=self.Diametro.text()
        n=self.Manning.text()
        S=self.Pendiente.text()
        Q=self.Caudal.text()
        
        if isfloat(D) and isfloat(n) and isfloat(S) and isfloat(Q):
            g=9.806665
            D=float(self.Diametro.text())
            n=float(self.Manning.text())
            S=float(self.Pendiente.text())
            Q=float(self.Caudal.text())
            r=D/2
            cte=Q*n/S**0.5
            yi=math.pi-0.01
            yf=yi+0.01
            error=0.000000001
            cont=1
            if Q > r:
                yi=math.pi*1.95-0.01
                yf=math.pi*1.95
            while abs(yi-yf)>error:
                yi=yf
                area=D**2*(yi-math.sin(yi))/8
                perimeter=yi*D/2
                fy=area**(5/3)/perimeter**(2/3)-cte
                d_area=D**2*(1-math.cos(yi))/8
                d_perimeter=D/2
                dfy=5*area**(2/3)/perimeter**(2 / 3)*d_area/3-2*area**(5/3)/perimeter**(5 / 3)*d_perimeter/3
                yf=yi-fy/dfy
                cont+= 1
                if cont>40 or area>(math.pi*D**2/4):
                    break
            if area<(math.pi*D**2/4):
                h=D*(1-math.cos(yf/2))/2
                A=D**2*(yi-math.sin(yi))/8
                P=yi*D/2
                T=D*math.sin(yf/2)
                Rh=A/P
                y=A/T
                v=Q/A
                Ep=h+v**2/(2*g)
                Fr=v/(g*y)**0.5
                self.Velocidad.setText(str(round(v,4)))
                self.Tirante.setText(str(round(y,4)))
                self.Energia.setText(str(round(Ep,4)))
                self.Froude.setText(str(round(Fr,4)))
                self.Perimetro.setText(str(round(P,4)))
                self.Area.setText(str(round(A,4)))
                self.Radio.setText(str(round(Rh,4)))
                self.Ancho.setText(str(round(T,4)))

                if Fr<1:
                    self.Regimen.setText('Regimen Subcrítico')
                elif Fr>1:
                    self.Regimen.setText('Regimen Supercrítico')
                elif Fr==1:
                    self.Regimen.setText('Regimen Crítico')
                    
            else: ventana_ErrorResultado(self).show() 
            
        else: ventana_ErrorNumerico(self).show() 

###################################### VENTANA MENU FLUJO CRITICO ######################################

class menuFlujoCritico(QMainWindow):

    def __init__(self, parent=None):
        super(menuFlujoCritico, self).__init__(parent)
        loadUi("Menú_FNormalyCritico.ui", self)

        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #Control de botones
        self.Trapezoidal.clicked.connect(self.abrirTrape)
        self.Circular.clicked.connect(self.abrirCircular)
        self.Atras.clicked.connect(self.AbrirVP)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()


    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def abrirTrape(self):
        self.hide()
        ventana2 = FCriticoTrapezoidal(self)
        ventana2.show()

    def abrirCircular(self):
        self.hide()
        ventana2 = FCriticoCircular(self)
        ventana2.show()

    def AbrirVP(self):
        self.hide()
        ventana2 = ventana_principal(self)
        ventana2.show()

####################### VENTANA FLUJO CRITICO-SECCION TRAPEZOIDAL #######################
class FCriticoTrapezoidal(QMainWindow):

    def __init__(self, parent=None):
        super(FCriticoTrapezoidal, self).__init__(parent)
        loadUi("FCriticoTrapezoidal.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Combobox
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Incognita.addItem('')
        self.Incognita.addItem('Tirante (y)')
        self.Incognita.addItem('Base (b)')
        layout.addWidget(self.Incognita)
        
        self.Incognita.currentTextChanged.connect(self.on_combobox_changed)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def on_combobox_changed(self, value):
        Inc = self.Incognita.currentText()

        if Inc == 'Tirante (y)':
            self.TVariable.setText('Base (b)')
            self.TVariable_2.setText('')
            self.TituloR_incognita.setText('Tirante (y)')
            self.TituloR_incognita_2.setText('Velocidad (v)')
            self.TituloR_incognita_3.setText('Área Hidráulica (A)')
        elif Inc == 'Base (b)':
            self.TVariable.setText('Tirante (y)')
            self.TVariable_2.setText('Área Hidráulica (A)')
            self.TituloR_incognita.setText('Base (b)')
            self.TituloR_incognita_2.setText('Velocidad (v)')
            self.TituloR_incognita_3.setText('')


    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuFlujoCritico(self)
        ventana2.show()
        
    def limpiar(self):
        self.R_incognita.setText("")
        self.Froude.setText("")
        self.Regimen.setText("")
        self.R_incognita2.setText("")
        self.Energia.setText("")
        self.Variable.setText("")
        self.Variable2.setText("")
        self.Caudal.setText("")
        self.Taludk1.setText("")
        self.Taludk2.setText("")
        self.Perimetro.setText("")
        self.R_incognita3.setText("")
        self.Radio.setText("")
        self.Ancho.setText("")
        self.Imagen.clear()
    
    def calculos(self):
        Inc=self.Incognita.currentText()
        
        if Inc=='Tirante (y)':
            Q=self.Caudal.text()
            b=self.Variable.text()
            k1=self.Taludk1.text()
            k2=self.Taludk2.text()
        
            if isfloat(Q) and isfloat(b) and isfloat(k1) and isfloat(k2):
                def newton(f,Df,x0,epsilon=0.0001,max_iter=50):
                    xn = x0
                    for n in range(0,max_iter):
                        fxn = f.subs(y1,xn)
                        if abs(fxn) < epsilon:
                            return xn
                        Dfxn = Df.subs(y1,xn)
                        if Dfxn == 0:
                            return None
                        xn = xn - fxn/Dfxn
                    return None
                g=9.806665
                Q=float(Q)
                b=float(b)
                k1=float(k1)
                k2=float(k2)
                
                if k1!=0 and k2!=0 and b!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    'Ecuaciones Simbólicas'
                    y1=sp.Symbol('y1')
                    Al=b*y1+((k1+k2)/2)*y1**2
                    Tl=b+y1*(k1+k2)
                    fyc=g*(Al**3/Tl)-Q**2
                    diffyc=sp.diff(fyc,y1)
  
                    yc=float(newton(fyc,diffyc,b))

                    'Ecuaciones numéricas'
                    A=b*yc+((k1+k2)/2)*yc**2
                    P=b+yc*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2))
                    T=b+yc*(k1+k2)
                    Rh=A/P
                    v=np.sqrt(A*g/T)
                    Ep=yc+Q**2/(2*g*A**2)
                    Fr=v/(g*A/T)**0.5
            
                    self.R_incognita.setText(str(round(yc,4)))
                    self.R_incognita2.setText(str(round(v,4)))
                    self.Energia.setText(str(round(Ep,4)))
                    self.Froude.setText(str(round(Fr,4)))
                    self.Perimetro.setText(str(round(P,4)))
                    self.R_incognita3.setText(str(round(A,4)))
                    self.Radio.setText(str(round(Rh,4)))
                    self.Ancho.setText(str(round(T,4)))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                        
                elif k1==0 and k2==0 and b!=0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)
                    
                    'Ecuaciones Simbólicas'
                    y1=sp.Symbol('y1')
                    Al=b*y1
                    Tl=b
                    fyc=g*(Al**3/Tl)-Q**2
                    diffyc=sp.diff(fyc,y1)
  
                    yc=float(newton(fyc,diffyc,b))

                    'Ecuaciones numéricas'
                    A=b*yc
                    P=b+2*yc
                    T=b
                    Rh=A/P
                    v=np.sqrt(A*g/T)
                    Ep=yc+Q**2/(2*g*A**2)
                    Fr=v/(g*A/T)**0.5
            
                    self.R_incognita.setText(str(round(yc,4)))
                    self.R_incognita2.setText(str(round(v,4)))
                    self.Energia.setText(str(round(Ep,4)))
                    self.Froude.setText(str(round(Fr,4)))
                    self.Perimetro.setText(str(round(P,4)))
                    self.R_incognita3.setText(str(round(A,4)))
                    self.Radio.setText(str(round(Rh,4)))
                    self.Ancho.setText(str(round(T,4)))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                    
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Alguno de los valores que ingreso no es numérico")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
         
        if Inc=='Base (b)':
            y=self.Variable.text()
            A=self.Variable2.text()
            Q=self.Caudal.text()
            k1=self.Taludk1.text()
            k2=self.Taludk2.text() 
                
            if isfloat(Q) and isfloat(A) and isfloat(k1) and isfloat(k2) and isfloat(y):
                g=9.806665
                A=float(A)
                y=float(y)
                Q=float(Q)
                k1=float(k1)
                k2=float(k2)
                    
                if k1!=0 and k2!=0:
                    qpixmap=QPixmap('Trapezoidal.png')
                    self.Imagen.setPixmap(qpixmap)

                    'Ecuaciones numéricas'
                    b=round((2*A-y**2*(k1+k2))/2*y,4)
                    P=round(b+y*(np.sqrt(1+k1**2)+np.sqrt(1+k2**2)),4)
                    T=round(b+y*(k1+k2),4)
                    Rh=round(A/P,4) 
                    v=round(np.sqrt(A*g/T),4)
                    Ep=round(y+Q**2/(2*g*A**2),4)
                    Fr=round(v/(g*A/T)**0.5,4)
                
                    self.R_incognita.setText(str(b))
                    self.R_incognita2.setText(str(v))
                    self.Energia.setText(str(Ep))
                    self.Froude.setText(str(Fr))
                    self.Perimetro.setText(str(P))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
                
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                            
                elif k1==0 and k2==0:
                    qpixmap=QPixmap('Rectangular.png')
                    self.Imagen.setPixmap(qpixmap)

                    'Ecuaciones numéricas'
                    b=round(2*A,4)
                    P=round(b+2*y,4)
                    T=round(b,4)
                    Rh=round(A/P,4) 
                    v=round(np.sqrt(A*g/T),4)
                    Ep=round(y+Q**2/(2*g*A**2),4)
                    Fr=round(v/(g*A/T)**0.5,4)
                
                    self.R_incognita.setText(str(b))
                    self.R_incognita2.setText(str(v))
                    self.Energia.setText(str(Ep))
                    self.Froude.setText(str(Fr))
                    self.Perimetro.setText(str(P))
                    self.Radio.setText(str(Rh))
                    self.Ancho.setText(str(T))
            
                    if Fr<1:
                        self.Regimen.setText('Regimen Subcrítico')
                    elif Fr>1:
                        self.Regimen.setText('Regimen Supercrítico')
                    elif Fr==1:
                        self.Regimen.setText('Regimen Crítico')
                        
                else: ventana_ErrorNumerico(self).show() 
                
####################### VENTANA FLUJO CRITICO-SECCION CIRCULAR #######################
class FCriticoCircular(QMainWindow):

    def __init__(self, parent=None):
        super(FCriticoCircular, self).__init__(parent)
        loadUi("FCriticoCircular.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuFlujoCritico(self)
        ventana2.show()
    
    def limpiar(self):
        self.Froude.setText("")
        self.Velocidad.setText("")
        self.Tirante.setText("")
        self.Regimen.setText("")
        self.Energia.setText("")
        self.Ancho.setText("")
        self.Caudal.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.Diametro.setText("")
    
    def calculos(self):
        
        D=self.Diametro.text()
        Q=self.Caudal.text()
        
        if isfloat(D) and isfloat(Q):
            g=9.806665
            D=float(self.Diametro.text())
            Q=float(self.Caudal.text())
            r=D/2
            yi=math.pi-0.01
            yf=yi+0.01
            error=0.000000001
            cont=1
            if Q>r:
                yi=math.pi*1.95-0.01
                yf=math.pi*1.95
            while abs(yi-yf)>error:
                yi=yf
                area=D**2*(yi-math.sin(yi))/8
                T=D*math.sin(yi/2)
                fy=g*(area**3/T)-Q**2
                par1=g*D**5*(yi-math.sin(yi))**2
                par2=(6*math.sin(yi/2)*(1-math.cos(yi))-math.cos(yi/2)*(yi-math.sin(yi)))
                dfy=(par1*par2)/(1024*(math.sin(yi/2))**2)
                yf=yi-fy/dfy
                cont+= 1
                if cont > 40 or area > (math.pi*D**2/4):
                    break
            if area<(math.pi*D**2/4):
                A=D**2*(yi-math.sin(yi))/8
                P=yi*D/2
                T=D*math.sin(yf/2)
                Rh=A/P
                y=-D/2*(math.cos(yf/2)-1)
                v=np.sqrt(A*g/T)
                Ep=y+Q**2/(2*g*A**2)
                Fr=v/(g*A/T)**0.5
                self.Velocidad.setText(str(round(v,4)))
                self.Tirante.setText(str(round(y,4)))
                self.Energia.setText(str(round(Ep,4)))
                self.Froude.setText(str(round(Fr,4)))
                self.Perimetro.setText(str(round(P,4)))
                self.Area.setText(str(round(A,4)))
                self.Radio.setText(str(round(Rh,4)))
                self.Ancho.setText(str(round(T,4)))

                if Fr<1:
                    self.Regimen.setText('Regimen Subcrítico')
                elif Fr>1:
                    self.Regimen.setText('Regimen Supercrítico')
                elif Fr==1:
                    self.Regimen.setText('Regimen Crítico')
                    
            else: ventana_ErrorResultado(self).show() 
            
        else: ventana_ErrorNumerico(self).show() 

###################################### VENTANA MENU ENERGIA ESPECIFICA ######################################

class menuEnergiaEspecifica(QMainWindow):

    def __init__(self, parent=None):
        super(menuEnergiaEspecifica, self).__init__(parent)
        loadUi("Menú_Especifica.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Control de botones
        self.Trapezoidal.clicked.connect(self.abrirTrape)
        self.Triangular.clicked.connect(self.abrirTriang)
        self.Circular.clicked.connect(self.abrirCircular)
        self.Parabolica.clicked.connect(self.abrirParabo)
        self.Atras.clicked.connect(self.AbrirVP)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def abrirTrape(self):
        self.hide()
        ventana2 = E_EspecificaTrapezoidal(self)
        ventana2.show()

    def abrirTriang(self):
        self.hide()
        ventana2 = E_EspecificaTriangular(self)
        ventana2.show()

    def abrirParabo(self):
        self.hide()
        ventana2 = E_EspecificaParabolica(self)
        ventana2.show()

    def abrirCircular(self):
        self.hide()
        ventana2 = E_EspecificaCircular(self)
        ventana2.show()

    def AbrirVP(self):
        self.hide()
        ventana2 = ventana_principal(self)
        ventana2.show()


####################### VENTANA ENERGIA ESPECIFICA-SECCION TRAPEZOIDAL #######################
class E_EspecificaTrapezoidal(QMainWindow):

    def __init__(self, parent=None):
        super(E_EspecificaTrapezoidal, self).__init__(parent)
        loadUi("E_EspecificaTrapezoidal.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Sizegrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        self.Coeficientes.clicked.connect(self.AbrirCoriolis)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def AbrirCoriolis(self):
        ventana2 = Coriolis(self)
        ventana2.show()
        
    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuEnergiaEspecifica(self)
        ventana2.show()

    def limpiar(self):
        self.Tirante.setText("")
        self.Froude.setText("")
        self.Regimen.setText("")
        self.Velocidad.setText("")
        self.Energia.setText("")
        self.Base.setText("")
        self.Caudal.setText("")
        self.Taludk1.setText("")
        self.Taludk2.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.Ancho.setText("")
        self.Coriolis.setText("")
        self.Grafica.clear()

    def calculos(self):
        Q = self.Caudal.text()
        b = self.Base.text()
        k1 = self.Taludk1.text()
        k2 = self.Taludk2.text()
        alp = self.Coriolis.text()

        if isfloat(Q) and isfloat(b) and isfloat(k1) and isfloat(k2) and isfloat(alp):
            def newton(f, Df, x0, epsilon=0.0001, max_iter=50):
                xn = x0
                for n in range(0, max_iter):
                    fxn = f.subs(y1, xn)
                    if abs(fxn) < epsilon:
                        return xn
                    Dfxn = Df.subs(y1, xn)
                    if Dfxn == 0:
                        return None
                    xn = xn - fxn / Dfxn
                return None

            g = 9.806665
            Q = float(Q)
            b = float(b)
            k1 = float(k1)
            k2 = float(k2)
            alp = float(alp)

            'Ecuaciones Simbólicas'
            y1 = sp.Symbol('y1')
            Al = b * y1 + ((k1 + k2) / 2) * y1 ** 2
            Tl = b + y1 * (k1 + k2)
            fyc = g * (Al ** 3 / Tl) - Q ** 2
            diffyc = sp.diff(fyc, y1)

            yc = float(newton(fyc, diffyc, b))

            'Ecuaciones numéricas'
            A = b * yc + ((k1 + k2) / 2) * yc ** 2
            P = b + yc * (np.sqrt(1 + k1 ** 2) + np.sqrt(1 + k2 ** 2))
            T = b + yc * (k1 + k2)
            Rh = A / P
            v = np.sqrt(A * g / T)
            Ecri=yc+alp*(Q**2/(2*g*A**2))
            Fr = v / (g * A / T) ** 0.5

            self.Tirante.setText(str(round(yc, 4)))
            self.Velocidad.setText(str(round(v, 4)))
            self.Energia.setText(str(round(Ecri, 4)))
            self.Froude.setText(str(round(Fr, 4)))
            self.Perimetro.setText(str(round(P, 4)))
            self.Area.setText(str(round(A, 4)))
            self.Radio.setText(str(round(Rh, 4)))
            self.Ancho.setText(str(round(T, 4)))

            Inter1 = np.arange(0.001, yc, 0.01)
            Inter2 = np.arange(yc, 10, 0.01)
            Inter2 = np.delete(Inter2, 0)
            InterTC = np.append(Inter1, Inter2)
            A = b * InterTC + ((k1 + k2) / 2) * InterTC ** 2
            XE = InterTC + alp * (Q ** 2 / (2 * g * A ** 2))

            self.Grafica.setXRange(0, 10)
            self.Grafica.setYRange(0, 10)
            self.Grafica.setTitle('Energia especifica')
            self.Grafica.setLabel('bottom', "Energia E(J)")
            self.Grafica.setLabel('left',"Tirante y(m)")
            self.Grafica.showGrid(x=True, y=True)
            self.Grafica.plot(XE, InterTC, pen=pg.mkPen('g', width=1))

            if Fr < 1:
                self.Regimen.setText('Regimen Subcrítico')
            elif Fr > 1:
                self.Regimen.setText('Regimen Supercrítico')
            elif Fr == 1:
                self.Regimen.setText('Regimen Crítico')

        else: ventana_ErrorNumerico(self).show() 


####################### VENTANA ENERGIA ESPECIFICA-SECCION TRIANGULAR #######################
class E_EspecificaTriangular(QMainWindow):

    def __init__(self, parent=None):
        super(E_EspecificaTriangular, self).__init__(parent)
        loadUi("E_EspecificaTriangular.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        self.Coeficientes.clicked.connect(self.AbrirCoriolis)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def AbrirCoriolis(self):
        ventana2 = Coriolis(self)
        ventana2.show()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuEnergiaEspecifica(self)
        ventana2.show()

    def limpiar(self):
        self.Caudal.setText("")
        self.Taludk.setText("")
        self.Tirante.setText("")
        self.Velocidad.setText("")
        self.Energia.setText("")
        self.Froude.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.Ancho.setText("")
        self.Profundidad.setText("")
        self.Regimen.setText("")
        self.Coriolis.setText("")
        self.Grafica.clear()

    def calculos(self):

        Q = self.Caudal.text()
        k = self.Taludk.text()
        alp = self.Coriolis.text()

        if isfloat(k) and isfloat(Q) and isfloat(alp):
            def newton(f, Df, x0, epsilon=0.0001, max_iter=50):
                xn = x0
                for n in range(0, max_iter):
                    fxn = f.subs(y1, xn)
                    if abs(fxn) < epsilon:
                        return xn
                    Dfxn = Df.subs(y1, xn)
                    if Dfxn == 0:
                        return None
                    xn = xn - fxn / Dfxn
                return None

            g = 9.806665
            Q = float(Q)
            k = float(k)
            alp = float(alp)

            'Ecuaciones Simbólicas'
            y1 = sp.Symbol('y1')
            Al = k * y1 ** 2
            Tl = 2 * k * y1
            fyc = g * (Al ** 3 / Tl) - Q ** 2
            diffyc = sp.diff(fyc, y1)
            yc = float(newton(fyc, diffyc, k))

            'Ecuaciones númericas'
            A = k * yc ** 2
            P = 2 * yc * np.sqrt(1 + k ** 2)
            Rh = (k * yc) / (2 * np.sqrt(1 + k ** 2))
            T = 2 * k * yc
            D = 1 / (2 * yc)
            v = np.sqrt(A * g / T)
            Ecri = yc + alp*(Q ** 2 / (2 * g * A ** 2))
            Fr = v / (g * A / T) ** 0.5

            self.Tirante.setText(str(round(yc, 4)))
            self.Velocidad.setText(str(round(v, 4)))
            self.Energia.setText(str(round(Ecri, 4)))
            self.Froude.setText(str(round(Fr, 4)))
            self.Perimetro.setText(str(round(P, 4)))
            self.Area.setText(str(round(A, 4)))
            self.Radio.setText(str(round(Rh, 4)))
            self.Ancho.setText(str(round(T, 4)))
            self.Profundidad.setText(str(round(D, 4)))

            Inter1 = np.arange(0.001, yc, 0.01)
            Inter2 = np.arange(yc, 10, 0.01)
            Inter2 = np.delete(Inter2, 0)
            InterTC = np.append(Inter1, Inter2)
            A = k * InterTC ** 2
            XE = InterTC + alp * (Q ** 2 / (2 * g * A ** 2))

            self.Grafica.setXRange(0, 10)
            self.Grafica.setYRange(0, 10)
            self.Grafica.setTitle('Energia especifica')
            self.Grafica.setLabel('bottom', "Energia E(J)")
            self.Grafica.setLabel('left', "Tirante y(m)")
            self.Grafica.showGrid(x=True, y=True)
            self.Grafica.plot(XE, InterTC, pen=pg.mkPen('g', width=1))

            if Fr < 1:
                self.Regimen.setText('Regimen Subcrítico')
            elif Fr > 1:
                self.Regimen.setText('Regimen Supercrítico')
            elif Fr == 1:
                self.Regimen.setText('Regimen Crítico')
                
        else: ventana_ErrorNumerico(self).show() 


####################### VENTANA ENERGIA ESPECIFICA-SECCION PARABOLICA #######################
class E_EspecificaParabolica(QMainWindow):

    def __init__(self, parent=None):
        super(E_EspecificaParabolica, self).__init__(parent)
        loadUi("E_EspecificaParabolica.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        self.Coeficientes.clicked.connect(self.AbrirCoriolis)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def AbrirCoriolis(self):
        ventana2 = Coriolis(self)
        ventana2.show()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuEnergiaEspecifica(self)
        ventana2.show()

    def limpiar(self):
        self.Froude.setText("")
        self.Velocidad.setText("")
        self.Tirante.setText("")
        self.Regimen.setText("")
        self.Energia.setText("")
        self.Ancho.setText("")
        self.Caudal.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.ConstanteK.setText("")
        self.Coriolis.setText("")
        self.Grafica.clear()

    def calculos(self):

        T = self.Ancho.text()
        Q = self.Caudal.text()
        alp = self.Coriolis.text()

        if isfloat(T) and isfloat(Q) and isfloat(alp):
            g = 9.806665
            T = float(self.Ancho.text())
            Q = float(self.Caudal.text())
            alp = float(self.Coriolis.text())

            yi = 1
            yf = 2
            error = 0.000000001
            cont = 1
            while abs(yi - yf) > error:
                yi = yf
                area = 2 * T * yi / 3
                d_area = 2 * T / 3
                perimeter = 0
                d_perimeter = 0

                if yi / T <= 0.25:
                    perimeter = T + 8 * yi ** 2 / (3 * T)
                    d_perimeter = 16 * yi / (3 * T)
                elif yi / T > 0.25:
                    x = 4 * yi / T
                    dx = 4 / T
                    perimeter = 0.5 * T * ((1 + x ** 2) ** 0.5 + math.log(x + (1 + x ** 2) ** 0.5) / x)
                    d_perimeter = 0.5 * T * (x / (1 + x ** 2) ** 0.5 + 1 / (x * (1 + x ** 2) ** 0.5) - math.log(
                        x + (1 + x ** 2) ** 0.5) / x ** 2) * dx
                    fy = area ** (5 / 3) / perimeter ** (2 / 3)
                    dfy = 5 * area ** (2 / 3) / perimeter ** (2 / 3) * d_area / 3 - 2 * area ** (5 / 3) / perimeter ** (
                                5 / 3) * d_perimeter / 3
                    yf = yi - fy / dfy
                    cont += 1
                    if cont > 40:
                        break
                    # A = 2*T*yf/3
                    P = 0
                    if yi / T <= 0.25:
                        P = T + 8 * yf ** 2 / (3 * T)
                    elif yi / T > 0.25:
                        x = 4 * yf / T
                        P = 0.5 * T * ((1 + x ** 2) ** 0.5 + math.log(x + (1 + x ** 2) ** 0.5) / x)

            E = (Q / 1.1067) ** (2 / 3)
            yc = 3 / 4 * E
            A = 2 * T * yc / 3
            Rh = A / P
            k = (4 * yc) / T ** 2
            Vc = np.sqrt(2 / 3 * g * yc)
            Fr = Vc / (g * A / T) ** 0.5

            self.Velocidad.setText(str(round(Vc, 4)))
            self.Tirante.setText(str(round(yc, 4)))
            self.Energia.setText(str(round(E, 4)))
            self.Froude.setText(str(round(Fr, 4)))
            self.Perimetro.setText(str(round(P, 4)))
            self.Area.setText(str(round(A, 4)))
            self.Radio.setText(str(round(Rh, 4)))
            self.ConstanteK.setText(str(round(k, 4)))

            Inter1 = np.arange(0.001, yc, 0.01)
            Inter2 = np.arange(yc, 10, 0.01)
            Inter2 = np.delete(Inter2, 0)
            InterTC = np.append(Inter1, Inter2)
            A = 2 * T * InterTC / 3
            XE = InterTC + alp * (Q ** 2 / (2 * g * A ** 2))

            self.Grafica.setXRange(0, 10)
            self.Grafica.setYRange(0, 10)
            self.Grafica.setTitle('Energia especifica')
            self.Grafica.setLabel('bottom', "Energia E(J)")
            self.Grafica.setLabel('left', "Tirante y(m)")
            self.Grafica.showGrid(x=True, y=True)
            self.Grafica.plot(XE, InterTC, pen=pg.mkPen('g', width=1))

            if Fr < 1:
                self.Regimen.setText('Regimen Subcrítico')
            elif Fr > 1:
                self.Regimen.setText('Regimen Supercrítico')
            elif Fr == 1:
                self.Regimen.setText('Regimen Crítico')
                
        else: ventana_ErrorNumerico(self).show() 


####################### VENTANA ENERGIA ESPECIFICA-SECCION CIRCULAR #######################
class E_EspecificaCircular(QMainWindow):

    def __init__(self, parent=None):
        super(E_EspecificaCircular, self).__init__(parent)
        loadUi("E_EspecificaCircular.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        self.Coeficientes.clicked.connect(self.AbrirCoriolis)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def AbrirCoriolis(self):
        ventana2 = Coriolis(self)
        ventana2.show()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuEnergiaEspecifica(self)
        ventana2.show()

    def limpiar(self):
        self.Froude.setText("")
        self.Velocidad.setText("")
        self.Tirante.setText("")
        self.Regimen.setText("")
        self.Energia.setText("")
        self.Ancho.setText("")
        self.Caudal.setText("")
        self.Perimetro.setText("")
        self.Area.setText("")
        self.Radio.setText("")
        self.Diametro.setText("")
        self.Coriolis.setText("")
        self.Grafica.clear()

    def calculos(self):

        D = self.Diametro.text()
        Q = self.Caudal.text()
        alp = self.Coriolis.text()

        if isfloat(D) and isfloat(Q):
            g = 9.806665
            D = float(self.Diametro.text())
            Q = float(self.Caudal.text())
            alp = float(self.Coriolis.text())
            r = D / 2
            yi = math.pi - 0.01
            yf = yi + 0.01
            error = 0.000000001
            cont = 1
            if Q > r:
                yi = math.pi * 1.95 - 0.01
                yf = math.pi * 1.95
            while abs(yi - yf) > error:
                yi = yf
                area = D ** 2 * (yi - math.sin(yi)) / 8
                T = D * math.sin(yi / 2)
                fy = g * (area ** 3 / T) - Q ** 2
                par1 = g * D ** 5 * (yi - math.sin(yi)) ** 2
                par2 = (6 * math.sin(yi / 2) * (1 - math.cos(yi)) - math.cos(yi / 2) * (yi - math.sin(yi)))
                dfy = (par1 * par2) / (1024 * (math.sin(yi / 2)) ** 2)
                yf = yi - fy / dfy
                cont += 1
                if cont > 40 or area > (math.pi * D ** 2 / 4):
                    break
            if area < (math.pi * D ** 2 / 4):
                A = D ** 2 * (yi - math.sin(yi)) / 8
                P = yi * D / 2
                T = D * math.sin(yf / 2)
                Rh = A / P
                y = -D / 2 * (math.cos(yf / 2) - 1)
                v = np.sqrt(A * g / T)
                Ep = y + Q ** 2 / (2 * g * A ** 2)
                Fr = v / (g * A / T) ** 0.5
                self.Velocidad.setText(str(round(v, 4)))
                self.Tirante.setText(str(round(y, 4)))
                self.Energia.setText(str(round(Ep, 4)))
                self.Froude.setText(str(round(Fr, 4)))
                self.Perimetro.setText(str(round(P, 4)))
                self.Area.setText(str(round(A, 4)))
                self.Radio.setText(str(round(Rh, 4)))
                self.Ancho.setText(str(round(T, 4)))

                Inter1 = np.arange(0.001, y, 0.01)
                Inter2 = np.arange(y, 10, 0.01)
                Inter2 = np.delete(Inter2, 0)
                InterTC = np.append(Inter1, Inter2)
                A = D ** 2 * (InterTC - np.sin(InterTC)) / 8
                XE = InterTC + alp * (Q ** 2 / (2 * g * A ** 2))

                self.Grafica.setXRange(0, 10)
                self.Grafica.setYRange(0, 10)
                self.Grafica.setTitle('Energia especifica')
                self.Grafica.setLabel('bottom', "Energia E(J)")
                self.Grafica.setLabel('left', "Tirante y(m)")
                self.Grafica.showGrid(x=True, y=True)
                self.Grafica.plot(XE, InterTC, pen=pg.mkPen('g', width=1))

                if Fr < 1:
                    self.Regimen.setText('Regimen Subcrítico')
                elif Fr > 1:
                    self.Regimen.setText('Regimen Supercrítico')
                elif Fr == 1:
                    self.Regimen.setText('Regimen Crítico')
                    
            else: ventana_ErrorResultado(self).show() 
    
        else: ventana_ErrorNumerico(self).show() 

###################################### VENTANA MENU ESTRUCTURAS ######################################

class menuEstructuras(QMainWindow):

    def __init__(self, parent=None):
        super(menuEstructuras, self).__init__(parent)
        loadUi("Menú_Estructuras.ui", self)

        #Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        
        #Control de botones
        self.Vertedores.clicked.connect(self.abrirVertedores)
        self.Orificios.clicked.connect(self.abrirOrificios)
        self.Compuertas.clicked.connect(self.abrirCompuertas)
        self.Atras.clicked.connect(self.AbrirVP)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()


    def sombra_frame(self, frame):
        sombra= QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
        
    def control_bt_minimizar(self):
        self.showMinimized()
        
    def abrirVertedores(self):
        self.hide()
        ventana2 = EstructurasVertedores(self)
        ventana2.show()

    def abrirOrificios(self):
        self.hide()
        ventana2 = EstructurasOrificios(self)
        ventana2.show()

    def abrirCompuertas(self):
        self.hide()
        ventana2 = EstructurasCompuertas(self)
        ventana2.show()

    def AbrirVP(self):
        self.hide()
        ventana2 = ventana_principal(self)
        ventana2.show()

####################### VENTANA ESTRUCTURAS-VERTEDORES #######################
class EstructurasVertedores(QMainWindow):

    def __init__(self, parent=None):
        super(EstructurasVertedores, self).__init__(parent)
        loadUi("Estructuras_Vertedores.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Combobox Incognita
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Incognita.addItem('')
        self.Incognita.addItem('Trapecial')
        self.Incognita.addItem('Rectamgular')
        self.Incognita.addItem('Triangular')
        self.Incognita.addItem('Circular')
        layout.addWidget(self.Incognita)
        
        self.Incognita.currentTextChanged.connect(self.on_combobox_changed)
        
        #Combobox Angulo
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Angulo.addItem('')
        self.Angulo.addItem('90')
        self.Angulo.addItem('60')
        self.Angulo.addItem('45')
        
        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
        
    def on_combobox_changed(self, value):
        Inc=self.Incognita.currentText()
        
        if Inc=='Trapecial':
            qpixmap=QPixmap('Vertedor trapezial.png')
            self.Imagen.setPixmap(qpixmap)
            self.T_Condiciones.setText('Condiciones:')
            self.Condiciones.setText(' * 0.1≤h≤0.6      *  0.5≤b≤2      * 0.2≤w≤1.13       *  B>b')
            self.T_Variable1.setText('Altura del vertedor (w)')
            self.T_Variable2.setText('Ángulo de vértice (θ)')
            self.T_Variable3.setText('Base del canal (B)')
            self.T_Variable4.setText('Base del vertedor (b)')
            self.T_Incognita1.setText('Coeficiente de gasto (C)')
            self.T_Incognita2.setText('Coeficiente de gasto (μ)')
            
        elif Inc=='Rectamgular':
            qpixmap=QPixmap('Vertedor rectangular.png')
            self.Imagen.setPixmap(qpixmap)
            self.T_Condiciones.setText('Condiciones:')
            self.Condiciones.setText(' * 0.1≤h≤0.6      *  0.5≤b≤2      * 0.2≤w≤1.13       *  B>b')
            self.T_Variable1.setText('Altura del vertedor (w)')
            self.T_Variable2.setText('Ángulo de vértice (θ)')
            self.T_Variable3.setText('Base del canal (B)')
            self.T_Variable4.setText('Base del vertedor (b)')
            
            self.T_Incognita1.setText('Coeficiente de gasto (μ)')
            self.T_Incognita2.setText('')
            
        elif Inc=='Triangular':
            qpixmap=QPixmap('Vertedor triangular.png')
            self.Imagen.setPixmap(qpixmap)
            self.T_Condiciones.setText('')
            self.Condiciones.setText('')
            self.T_Variable1.setText('Altura del vertedor (w)')
            self.T_Variable2.setText('Ángulo de vértice (θ)')
            self.T_Variable3.setText('')
            self.T_Variable4.setText('')
            self.Variable3.setText('')
            self.Variable4.setText('')
            
            self.T_Incognita1.setText('Coeficiente de gasto (C)')
            self.T_Incognita2.setText('')
            
        elif Inc=='Circular':
            qpixmap=QPixmap('Vertedor circular.png')
            self.Imagen.setPixmap(qpixmap)
            self.T_Condiciones.setText('')
            self.Condiciones.setText('')
            self.T_Variable1.setText('Diametro (D)')
            self.T_Variable2.setText('')
            self.T_Variable3.setText('')
            self.T_Variable4.setText('')
            self.Variable3.setText('')
            self.Variable4.setText('')
            self.Angulo.clear()
            
            self.T_Incognita1.setText('Coeficiente de gasto (μ)')
            self.T_Incognita2.setText('Coeficiente de gasto (ϕ)')
            
    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuEstructuras(self)
        ventana2.show()
        
    def limpiar(self):
        self.h.setText("")
        self.Variable1.setText("")
        self.Variable3.setText("")
        self.Variable4.setText("")
        self.Caudal.setText("")
        self.Incognita1.setText("")
        self.Incognita2.setText("")
        self.Imagen.clear()
        self.Angulo.clear()
    
    def calculos(self):
        
        Inc=self.Incognita.currentText()
        
        if Inc=='Trapecial':
            h=self.h.text()
            w=self.Variable1.text()
            B=self.Variable3.text()
            b=self.Variable4.text()
        
            if isfloat(h) and isfloat(w) and isfloat(B) and isfloat(b):
            
                g=9.806665
                h=float(self.h.text())
                w=float(self.Variable1.text())
                B=float(self.Variable3.text())
                b=float(self.Variable4.text())
                theta=float(self.Angulo.currentText())
                
                if 0.1<=h<=0.6 and 0.5<=b<=2 and 0.2<=w<=1.13 and B>b:
                    mu=(0.6075-0.045*((B-b)/B)+0.0041/h)*(1+0.55*(b/B)**2*(h/(h+w))**2)
                    
                    CoT=1.32*(np.tan(theta/2))/h**0.03
                    Q=CoT*h**(5/2)+2/3*np.sqrt(2*g)*mu*b*h**(3/2)
                    
                    self.Caudal.setText(str(round(Q,4)))
                    self.Incognita1.setText(str(round(CoT,4)))   
                    self.Incognita2.setText(str(round(mu,4)))
                    
                else: ventana_ErrorB(self).show()
                    
            else: ventana_ErrorNumerico(self).show()
                
        elif Inc=='Rectamgular':
            h=self.h.text()
            w=self.Variable1.text()
            B=self.Variable3.text()
            b=self.Variable4.text()
        
            if isfloat(h) and isfloat(w) and isfloat(B) and isfloat(b):
            
                g=9.806665
                h=float(self.h.text())
                w=float(self.Variable1.text())
                B=float(self.Variable3.text())
                b=float(self.Variable4.text())
                theta=float(self.Angulo.currentText())
                
                if 0.1<=h<=0.6 and 0.5<=b<=2 and 0.2<=w<=1.13 and B>b:
                    mu=(0.6075-0.045*((B-b)/B)+0.0041/h)*(1+0.55*(b/B)**2*(h/(h+w))**2)
                    
                    Co=1.1951-0.3902*(theta/180)
                    mu1=mu*Co
                    Q=2/3*np.sqrt(2*g)*mu1*b*h**(3/2)
                    
                    self.Caudal.setText(str(round(Q,4)))
                    self.Incognita1.setText(str(round(mu,4)))
                    
                else: ventana_ErrorB(self).show()
                    
            else: ventana_ErrorNumerico(self).show() 
            
        elif Inc=='Triangular':
            h=self.h.text()
            w=self.Variable1.text()
        
            if isfloat(h) and isfloat(w):
            
                g=9.806665
                h=float(self.h.text())
                w=float(self.Variable1.text())
                theta=float(self.Angulo.currentText())
                
                Co=1.32*(np.tan(theta/2))/h**0.03

                Q=Co*h**(5/2)
                    
                self.Caudal.setText(str(round(Q,4)))
                self.Incognita1.setText(str(round(Co,4)))
                    
            else: ventana_ErrorNumerico(self).show() 
            
        elif Inc=='Circular':
            h=self.h.text()
            D=self.Variable1.text()
        
            if isfloat(h) and isfloat(D):
                
                g=9.806665
                h=float(self.h.text())
                D=float(self.Variable1.text())
                
                phi=10.12*(h/D)**1.975-2.66*(h/D)**3.78
                mu=0.555+D/(110*h)+(0.041*h)/D
                Q=phi*mu*D**(5/2)
                             
                self.Caudal.setText(str(round(Q,4)))
                self.Incognita1.setText(str(round(mu,4)))
                self.Incognita2.setText(str(round(phi,4)))
                    
            else: ventana_ErrorNumerico(self).show()  
            
####################### VENTANA ESTRUCTURAS-ORIFICIOS #######################
class EstructurasOrificios(QMainWindow):

    def __init__(self, parent=None):
        super(EstructurasOrificios, self).__init__(parent)
        loadUi("Estructuras_Orificios.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #Combobox Cd
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.Cd.addItem('')
        self.Cd.addItem('0.60')
        self.Cd.addItem('0.82')
        self.Cd.addItem('0.97')
        
        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
            
    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuEstructuras(self)
        ventana2.show()
        
    def limpiar(self):
        self.h.setText("")
        self.Area.setText("")
        self.CaudalMe.setText("")
        self.CaudalLi.setText("")
        self.Cd.clear()
    
    def calculos(self):
        
        h=self.h.text()
        A=self.Area.text()

        
        if isfloat(h) and isfloat(A):
            
            g=9.806665
            h=float(self.h.text())
            A=float(self.Area.text())
            Cd=float(self.Cd.currentText())  
            
            Q=Cd*A*np.sqrt(2*g*h)
                    
            self.CaudalMe.setText(str(round(Q,4)))
            self.CaudalLi.setText(str(round(Q*1000,4)))   

        else: ventana_ErrorNumerico(self).show()

####################### VENTANA ESTRUCTURAS-COMPUERTAS #######################
class EstructurasCompuertas(QMainWindow):

    def __init__(self, parent=None):
        super(EstructurasCompuertas, self).__init__(parent)
        loadUi("Estructuras_Compuertas.ui", self)

        # Sombra de los Widgets
        self.sombra_frame(self.frame_superior)

        # Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        # Control Botones
        self.Atras.clicked.connect(self.AbrirMenu)
        self.Limpiar.clicked.connect(self.limpiar)
        self.Calcular.clicked.connect(self.calculos)
        
        # mover ventana
        self.frame_superior.mouseMoveEvent=self.mover_ventana
        
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
            
    def control_bt_minimizar(self):
        self.showMinimized()

    def AbrirMenu(self):
        self.hide()
        ventana2 = menuEstructuras(self)
        ventana2.show()
        
    def limpiar(self):
        self.Base.setText("")
        self.Apertura.setText("")
        self.Tirantey1.setText("")
        self.Tirantey3.setText("")
        self.Caudal.setText("")
        self.Cc.setText("")
        self.Cd.setText("")
        self.Cv.setText("")
    
    def calculos(self):
        
        b=self.Base.text()
        a=self.Apertura.text()
        y1=self.Tirantey1.text()
        y3=self.Tirantey3.text()
        
        if isfloat(b) and isfloat(a) and isfloat(y1) and isfloat(y3):
            
            g=9.806665
            b=float(self.Base.text())
            a=float(self.Apertura.text())
            y1=float(self.Tirantey1.text())
            y3=float(self.Tirantey3.text())
            
            if y3<y1:
               Cc=0.510+0.1*np.sqrt(23.04-(-4.69)**2)
               Cd=Cc/(np.sqrt(1+Cc*a/y1))
               Cv=Cd/Cc
               Q=Cd*b*a*np.sqrt(2*g*y1)
                    
               self.Caudal.setText(str(round(Q,4)))
               self.Cc.setText(str(round(Cc,4))) 
               self.Cd.setText(str(round(Cd,4)))
               self.Cv.setText(str(round(Cv,4)))
               
            else: ventana_Errory3(self).show() 
        else: ventana_ErrorNumerico(self).show()                
if __name__== "__main__":
    app = QApplication(sys.argv)
    GUI= ventana_principal()
    GUI.show()
    sys.exit(app.exec_())
