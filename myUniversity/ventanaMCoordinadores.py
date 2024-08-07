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

class Ui_FormMCoordinadores(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000,600)
        Form.setStyleSheet("background-color:#FF00FE")

        AppVLayout = QVBoxLayout()
        AppVLayout.setContentsMargins(0,0,0,0)

        self.botones = QHBoxLayout()
        self.botones.setContentsMargins(0,0,0,0)
        
        self.formGroupBox = QGroupBox("Mostrar Coordinadores") 
        self.formGroupBox.setFont(QFont('Arial', 20))
        self.formGroupBox.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.botonMostrar = QPushButton("Mostrar Coordinadores")
        self.botonMostrar.setFixedSize(170, 50)
        self.botonMostrar.setStyleSheet("background-color:#4F99FF;")
        self.botonMostrar.clicked.connect(lambda:self.getInfo(Form))
        self.botonCancelar = QPushButton("Cancelar")
        self.botonCancelar.setFixedSize(150, 50)
        self.botonCancelar.setStyleSheet("background-color:#4F99FF;")
        self.botonCancelar.clicked.connect(lambda:Form.close())

        self.botones.addWidget(self.botonMostrar,QtCore.Qt.AlignmentFlag.AlignCenter)
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

            consulta = """SELECT * FROM "Coordinador" """
 
            cursor.execute(consulta)

            column_names = [desc[0] for desc in cursor.description]
            print("\n|----------------------------------------------------------------------------------------------------------------------------|")
            print("|", end="")
            for i in column_names:
                print(i, end="")
                print("   |   ", end="")
            
            print("\n|----------------------------------------------------------------------------------------------------------------------------|")

            # Con fetchall traemos todas las filas
            alumnos = cursor.fetchall()

            # Recorrer e imprimir
            for alumno in alumnos:
                print("|", end="")
                print(alumno)

            print("|----------------------------------------------------------------------------------------------------------------------------|\n")

        except (Exception, psycopg2.Error) as error:
            print("Ocurrió un error al consultar: ", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mostrar Coordinadores"))