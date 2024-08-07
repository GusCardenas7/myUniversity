from ctypes import alignment
from pickle import TRUE
from tkinter import CENTER
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QApplication, QLineEdit,QLabel, QGroupBox, QMessageBox, QComboBox, QDialogButtonBox, QSpinBox, QFormLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize,Qt
from Estilos import DynamicFrameQSize,GetFrameBackGroundStyle, GetWidgetBackGroundColor
import sys
import psycopg2

class Ui_FormClaveCarrera(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000,300)
        Form.setStyleSheet("background-color:#800080")

        AppVLayout = QVBoxLayout()
        AppVLayout.setContentsMargins(0,0,0,0)

        self.botones = QHBoxLayout()
        self.botones.setContentsMargins(0,0,0,0)
        
        self.formGroupBox = QGroupBox("Modificar Clave Carrera") 
        self.formGroupBox.setFixedSize(1000, 300)
        self.formGroupBox.setFont(QFont('Arial', 20))
        self.formGroupBox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.botonModificar = QPushButton("Modificar")
        self.botonModificar.setFixedSize(150, 50)
        self.botonModificar.setStyleSheet("background-color:#4F99FF;")
        self.botonModificar.clicked.connect(lambda:self.getInfo(Form))
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setFont(QFont('Arial', 10))
        self.nameLineEdit.setStyleSheet("background-color:white")
        self.nameLineEdit2 = QLineEdit()
        self.nameLineEdit2.setFont(QFont('Arial', 10))
        self.nameLineEdit2.setStyleSheet("background-color:white")  

        self.createForm() 

        self.botonCancelar = QPushButton("Cancelar")
        self.botonCancelar.setFixedSize(150, 50)
        self.botonCancelar.setStyleSheet("background-color:#4F99FF;")
        self.botonCancelar.clicked.connect(lambda:Form.close())

        self.botones.addWidget(self.botonModificar,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.botones.addWidget(self.botonCancelar,QtCore.Qt.AlignmentFlag.AlignCenter)

        AppVLayout.addWidget(self.formGroupBox,QtCore.Qt.AlignmentFlag.AlignCenter)
        AppVLayout.addLayout(self.botones, QtCore.Qt.AlignmentFlag.AlignCenter)

        Form.setLayout(AppVLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def getInfo(self, Form): 
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="password",
                                        host="localhost",
                                        port="5432",
                                        database="Universidad")
            cursor = connection.cursor()

            consulta = """UPDATE "Carrera" SET clave_carrera = %s WHERE clave_carrera = %s;"""
            cursor.execute(consulta, (self.nameLineEdit2.text(), self.nameLineEdit.text()))

            # No olvidemos hacer commit cuando hacemos un cambio a la BD
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Ocurrió un error al eliminar: ", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        Form.close()
    
    def createForm(self): 
        layout = QFormLayout()

        self.label = QLabel("Introduzca la clave de la carrera a modificar") 
        self.label.setFont(QFont('Arial', 10))
        self.label2 = QLabel("Introduzca la nueva clave de la carrera") 
        self.label2.setFont(QFont('Arial', 10))

        layout.addRow(self.label, self.nameLineEdit)
        layout.addRow(self.label2, self.nameLineEdit2)
        self.formGroupBox.setLayout(layout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Modificar Clave Carrera"))