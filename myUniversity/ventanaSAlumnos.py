from ctypes import alignment
from pickle import TRUE
from tkinter import CENTER
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QTextEdit, QLineEdit,QLabel, QGroupBox, QFrame, QComboBox, QDialogButtonBox, QSpinBox, QFormLayout, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize,Qt
from Estilos import DynamicFrameQSize,GetFrameBackGroundStyle, GetWidgetBackGroundColor
from CommonQuery import CommonQuery
import sys
import psycopg2

class Ui_FormSAlumnos(object):
    
    CQ = CommonQuery("postgres","password","Universidad","localhost","5432")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000,600)
        Form.setStyleSheet("background-color:#FFFF00")

        AppVLayout = QVBoxLayout()
        AppVLayout.setContentsMargins(0,0,0,0)

        self.botones = QHBoxLayout()
        self.botones.setContentsMargins(0,0,0,0)
        
        self.formGroupBox = QGroupBox("Agregar Alumno") 
        self.formGroupBox.setFont(QFont('Arial', 20))
        self.formGroupBox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        
        self.cmbAlumnos = QComboBox() 
        self.cmbAlumnos.setFont(QFont('Arial', 10))
        self.cmbAlumnos.setStyleSheet("background-color:white")

        self.cmbSalones = QComboBox() 
        self.cmbSalones.setFont(QFont('Arial', 10))
        self.cmbSalones.setStyleSheet("background-color:white")
        
        self.createForm() 

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedSize(150, 50)
        self.botonRegistrar.setStyleSheet("background-color:#4F99FF;")
        self.botonRegistrar.clicked.connect(lambda:self.insert())
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
        self.cargarSalones()
        self.cargarAlumnos()
        QtCore.QMetaObject.connectSlotsByName(Form)

    
    def cargarSalones(self):
        query = """SELECT id_salon,id_salon FROM "Salon" """
        salones = self.CQ.getDictFromQuery(query)
        for sal in salones:
            id = str(sal[0])
            text = (sal[1])
            self.cmbSalones.addItem(text,id)

    def cargarAlumnos(self):
        query = """SELECT codigo_alumno,nombre FROM "Alumno" """
        alumnos = self.CQ.getDictFromQuery(query)
        for sal in alumnos:
            id = str(sal[0])
            text = str(sal[1])
            self.cmbAlumnos.addItem(text,id)
    
    def insert(self):
        try:
            nombreAlumno = self.cmbAlumnos.currentText()
            codigoAlunmo = self.cmbAlumnos.currentData()

            idSalon = self.cmbSalones.currentText()
            valueSalon = self.cmbSalones.currentData()

            insertQuery =  """ INSERT INTO "Asiste"(id_salon2,codigo_alumno1) VALUES( '"""+ idSalon +"""',"""+ codigoAlunmo +") """
            self.CQ.executeQuery(insertQuery)

            self.txtConsole.setText("INSERTADO CORRECTAMENTE")
        except Exception as ex:
            self.txtConsole.setText("Error al insertar -> " + str(ex))

    def createForm(self): 
        layout = QFormLayout()

        self.label = QLabel("ID_Salon") 
        self.label.setFont(QFont('Arial', 10))
        self.label2 = QLabel("Codigo_Alumno") 
        self.label2.setFont(QFont('Arial', 10))
        self.txtConsole =  QTextEdit()
        self.txtConsole.setFixedSize(800,100)

        layout.setContentsMargins(0,0,0,0)
        layout.addRow(self.label, self.cmbSalones)
        layout.addRow(self.label2, self.cmbAlumnos)
        layout.addWidget(self.txtConsole)
        
        self.formGroupBox.setLayout(layout)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Agregar Alumno"))