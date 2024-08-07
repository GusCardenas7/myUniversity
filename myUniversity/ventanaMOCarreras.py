from ctypes import alignment
from pickle import TRUE
from tkinter import CENTER
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QApplication, QLineEdit,QLabel, QGroupBox, QMessageBox, QComboBox, QDialogButtonBox, QSpinBox, QFormLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize,Qt
from Estilos import DynamicFrameQSize,GetFrameBackGroundStyle, GetWidgetBackGroundColor
from ctypes import alignment
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QApplication,QMainWindow,QFrame,QWidget, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize,Qt
from cv2 import QT_PUSH_BUTTON
from MisWidgets import BarraDeConfiguracion, BarraDeNavegacion
from Estilos import DynamicFrameQSize,GetFrameBackGroundStyle, GetWidgetBackGroundColor
import sys
import psycopg2
from ventanaClaveCarrera import Ui_FormClaveCarrera

class Ui_FormMOCarreras(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000,600)
        Form.setStyleSheet("background-color:#800080")

        AppVLayout = QVBoxLayout()
        AppVLayout.setContentsMargins(0,0,0,0)

        self.botones = QHBoxLayout()
        self.botones.setContentsMargins(0,0,0,0)
        
        self.formGroupBox = QGroupBox("Modificar Carrera") 
        self.formGroupBox.setFixedSize(1000, 300)
        self.formGroupBox.setFont(QFont('Arial', 20))
        self.formGroupBox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.botonClave = QPushButton("Clave Carrera")
        self.botonClave.setFixedSize(150, 50)
        self.botonClave.setStyleSheet("background-color:#4F99FF;")
        self.botonClave.clicked.connect(lambda:self.ventanaModificarClave())
        self.botonDuracion = QPushButton("Duracion")
        self.botonDuracion.setFixedSize(150, 50)
        self.botonDuracion.setStyleSheet("background-color:#4F99FF;")
        self.botonDuracion.clicked.connect(lambda:self.getInfo(Form))
        self.botonNombre = QPushButton("Nombre")
        self.botonNombre.setFixedSize(150, 50)
        self.botonNombre.setStyleSheet("background-color:#4F99FF;")
        self.botonNombre.clicked.connect(lambda:self.getInfo(Form))
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setFont(QFont('Arial', 10))
        self.nameLineEdit.setStyleSheet("background-color:white") 

        self.botonCancelar = QPushButton("Cancelar")
        self.botonCancelar.setFixedSize(150, 50)
        self.botonCancelar.setStyleSheet("background-color:#4F99FF;")
        self.botonCancelar.clicked.connect(lambda:Form.close())

        self.botones.addWidget(self.botonClave,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.botones.addWidget(self.botonDuracion,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.botones.addWidget(self.botonNombre,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.botones.addWidget(self.botonCancelar,QtCore.Qt.AlignmentFlag.AlignCenter)

        AppVLayout.addWidget(self.formGroupBox,QtCore.Qt.AlignmentFlag.AlignCenter)
        AppVLayout.addLayout(self.botones, QtCore.Qt.AlignmentFlag.AlignCenter)

        Form.setLayout(AppVLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def getInfo(self, Form): 
        Form.close()

    def ventanaModificarClave(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormClaveCarrera()
        self.ui2.setupUi(self.form)
        self.form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificar Carrera"))