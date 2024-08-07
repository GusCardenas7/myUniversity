from ctypes import alignment
from pickle import TRUE
from tkinter import CENTER
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QApplication, QLineEdit,QLabel, QGroupBox, QFrame, QComboBox, QDialogButtonBox, QSpinBox, QFormLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize,Qt
from Estilos import DynamicFrameQSize,GetFrameBackGroundStyle, GetWidgetBackGroundColor
import sys
import psycopg2

class Ui_FormSalones(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000,600)
        Form.setStyleSheet("background-color:#FFFF00")

        AppVLayout = QVBoxLayout()
        AppVLayout.setContentsMargins(0,0,0,0)

        self.botones = QHBoxLayout()
        self.botones.setContentsMargins(0,0,0,0)
        
        self.formGroupBox = QGroupBox("Agregar Salon") 
        self.formGroupBox.setFont(QFont('Arial', 20))
        self.formGroupBox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.ageSpinBar = QSpinBox() 
        self.ageSpinBar.setFont(QFont('Arial', 10))
        self.ageSpinBar.setStyleSheet("background-color:white")
        self.ageSpinBar2 = QSpinBox() 
        self.ageSpinBar2.setFont(QFont('Arial', 10))
        self.ageSpinBar2.setStyleSheet("background-color:white")
        self.degreeComboBox = QComboBox() 
        self.degreeComboBox.setFont(QFont('Arial', 10))
        self.degreeComboBox.setStyleSheet("background-color:white")
        self.degreeComboBox.addItems(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]) 
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setFont(QFont('Arial', 10))
        self.nameLineEdit.setStyleSheet("background-color:white") 
        self.nameLineEdit2 = QLineEdit()
        self.nameLineEdit2.setFont(QFont('Arial', 10))
        self.nameLineEdit2.setStyleSheet("background-color:white") 

        self.createForm() 

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedSize(150, 50)
        self.botonRegistrar.setStyleSheet("background-color:#4F99FF;")
        self.botonRegistrar.clicked.connect(lambda:self.getInfo(Form))
        self.botonCancelar = QPushButton("Cancelar")
        self.botonCancelar.setFixedSize(150, 50)
        self.botonCancelar.setStyleSheet("background-color:#4F99FF;")
        self.botonCancelar.clicked.connect(lambda:Form.close())

        self.botones.addWidget(self.botonRegistrar,QtCore.Qt.AlignmentFlag.AlignCenter)
        self.botones.addWidget(self.botonCancelar,QtCore.Qt.AlignmentFlag.AlignCenter)

        AppVLayout.addWidget(self.formGroupBox,QtCore.Qt.AlignmentFlag.AlignCenter)
        AppVLayout.addLayout(self.botones, QtCore.Qt.AlignmentFlag.AlignCenter)

        Form.setLayout(AppVLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def getInfo(self, Form): 
        print("ID_Salon : {0}".format(self.nameLineEdit.text())) 
        print("Numero : {0}".format(self.ageSpinBar.text())) 
        print("Capacidad : {0}".format(self.ageSpinBar2.text()))
        print("Edificio : {0}".format(self.degreeComboBox.currentText())) 
        print("Codigo_Profesor : {0}".format(self.nameLineEdit2.text()))
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="password",
                                        host="localhost",
                                        port="5432",
                                        database="Universidad")
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO "Salon"(id_salon, numero, capacidad, edificio, codigo_profesor2) VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = (self.nameLineEdit.text(), self.ageSpinBar.text(), self.ageSpinBar2.text(),
            self.degreeComboBox.currentText(), self.nameLineEdit2.text())
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into Salon table")

        except (Exception, psycopg2.Error) as error:
            print("Ocurrió un error al consultar: ", error)

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        Form.close()
    
    def createForm(self): 
        layout = QFormLayout()

        self.label = QLabel("ID_Salon") 
        self.label.setFont(QFont('Arial', 10))
        self.label2 = QLabel("Numero") 
        self.label2.setFont(QFont('Arial', 10))
        self.label3 = QLabel("Capacidad") 
        self.label3.setFont(QFont('Arial', 10))
        self.label4 = QLabel("Edificio") 
        self.label4.setFont(QFont('Arial', 10))
        self.label5 = QLabel("Codigo_Profesor") 
        self.label5.setFont(QFont('Arial', 10))

        layout.addRow(self.label, self.nameLineEdit)
        layout.addRow(self.label2, self.ageSpinBar) 
        layout.addRow(self.label3, self.ageSpinBar2) 
        layout.addRow(self.label4, self.degreeComboBox) 
        layout.addRow(self.label5, self.nameLineEdit2) 
        self.formGroupBox.setLayout(layout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Agregar Salon"))