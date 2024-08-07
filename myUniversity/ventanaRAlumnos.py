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

class Ui_FormAlumnos(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000,600)
        Form.setStyleSheet("background-color:#FFA600")

        AppVLayout = QVBoxLayout()
        AppVLayout.setContentsMargins(0,0,0,0)

        self.botones = QHBoxLayout()
        self.botones.setContentsMargins(0,0,0,0)
        
        self.formGroupBox = QGroupBox("Agregar Alumno") 
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
        self.degreeComboBox.addItems(["M","F"]) 
        self.nameLineEdit = QLineEdit()
        self.nameLineEdit.setFont(QFont('Arial', 10))
        self.nameLineEdit.setStyleSheet("background-color:white") 
        self.nameLineEdit2 = QLineEdit()
        self.nameLineEdit2.setFont(QFont('Arial', 10))
        self.nameLineEdit2.setStyleSheet("background-color:white") 
        self.nameLineEdit3 = QLineEdit()
        self.nameLineEdit3.setFont(QFont('Arial', 10))
        self.nameLineEdit3.setStyleSheet("background-color:white") 
        self.nameLineEdit4 = QLineEdit()
        self.nameLineEdit4.setFont(QFont('Arial', 10))
        self.nameLineEdit4.setStyleSheet("background-color:white") 
        self.nameLineEdit5 = QLineEdit()
        self.nameLineEdit5.setFont(QFont('Arial', 10))
        self.nameLineEdit5.setStyleSheet("background-color:white") 

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
        print("Codigo_Alumno : {0}".format(self.nameLineEdit.text())) 
        print("Nombre : {0}".format(self.nameLineEdit2.text())) 
        print("Genero : {0}".format(self.degreeComboBox.currentText()))
        print("Edad : {0}".format(self.ageSpinBar.text())) 
        print("Correo : {0}".format(self.nameLineEdit3.text())) 
        print("Semestre : {0}".format(self.ageSpinBar2.text()))
        print("ID_Coordinador : {0}".format(self.nameLineEdit4.text())) 
        print("Clave_Carrera : {0}".format(self.nameLineEdit5.text())) 
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="password",
                                        host="localhost",
                                        port="5432",
                                        database="Universidad")
            cursor = connection.cursor()

            postgres_insert_query = """ INSERT INTO "Alumno"(codigo_alumno, nombre, genero, edad, correo, semestre,
            id_coordinador1, clave_carrera2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (self.nameLineEdit.text(), self.nameLineEdit2.text(), self.degreeComboBox.currentText(),
            self.ageSpinBar.text(), self.nameLineEdit3.text(), self.ageSpinBar2.text(), self.nameLineEdit4.text(),
            self.nameLineEdit5.text())
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into Alumno table")

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

        self.label = QLabel("Codigo_Alumno") 
        self.label.setFont(QFont('Arial', 10))
        self.label2 = QLabel("Nombre") 
        self.label2.setFont(QFont('Arial', 10))
        self.label3 = QLabel("Genero") 
        self.label3.setFont(QFont('Arial', 10))
        self.label4 = QLabel("Edad") 
        self.label4.setFont(QFont('Arial', 10))
        self.label5 = QLabel("Correo") 
        self.label5.setFont(QFont('Arial', 10))
        self.label6 = QLabel("Semestre") 
        self.label6.setFont(QFont('Arial', 10))
        self.label7 = QLabel("ID_Coordinador") 
        self.label7.setFont(QFont('Arial', 10))
        self.label8 = QLabel("Clave_Carrera") 
        self.label8.setFont(QFont('Arial', 10))

        layout.addRow(self.label, self.nameLineEdit)
        layout.addRow(self.label2, self.nameLineEdit2) 
        layout.addRow(self.label3, self.degreeComboBox) 
        layout.addRow(self.label4, self.ageSpinBar) 
        layout.addRow(self.label5, self.nameLineEdit3)  
        layout.addRow(self.label6, self.ageSpinBar2) 
        layout.addRow(self.label7, self.nameLineEdit4) 
        layout.addRow(self.label8, self.nameLineEdit5) 
        self.formGroupBox.setLayout(layout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Agregar Alumno"))