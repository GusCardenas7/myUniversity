from ctypes import alignment
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QApplication,QMainWindow,QFrame,QWidget, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize,Qt
from cv2 import QT_PUSH_BUTTON
from MisWidgets import BarraDeConfiguracion, BarraDeNavegacion
from Estilos import DynamicFrameQSize,GetFrameBackGroundStyle, GetWidgetBackGroundColor
from ventanaRAlumnos import Ui_FormAlumnos
from ventanaBAlumnos import Ui_FormBAlumnos
from ventanaMAlumnos import Ui_FormMAlumnos
from ventanaEAlumnos import Ui_FormEAlumnos
from ventanaRProfesores import Ui_FormProfesores
from ventanaBProfesores import Ui_FormBProfesores
from ventanaMProfesores import Ui_FormMProfesores
from ventanaEProfesores import Ui_FormEProfesores
from ventanaRCoordinadores import Ui_FormCoordinadores
from ventanaBCoordinadores import Ui_FormBCoordinadores
from ventanaMCoordinadores import Ui_FormMCoordinadores
from ventanaECoordinadores import Ui_FormECoordinadores
from ventanaRSalones import Ui_FormSalones
from ventanaBSalones import Ui_FormBSalones
from ventanaMSalones import Ui_FormMSalones
from ventanaESalones import Ui_FormESalones
from ventanaRMaterias import Ui_FormMaterias
from ventanaBMaterias import Ui_FormBMaterias
from ventanaMMaterias import Ui_FormMMaterias
from ventanaEMaterias import Ui_FormEMaterias
from ventanaRCarreras import Ui_FormCarreras
from ventanaBCarreras import Ui_FormBCarreras
from ventanaMCarreras import Ui_FormMCarreras
from ventanaECarreras import Ui_FormECarreras
from ventanaMOCarreras import Ui_FormMOCarreras
from ventanaRGrupos import Ui_FormGrupos
from ventanaBGrupos import Ui_FormBGrupos
from ventanaMGrupos import Ui_FormMGrupos
from ventanaEGrupos import Ui_FormEGrupos
import sys

ui = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setFixedSize(1200,800)
        self.MainWidget.setStyleSheet("background-color:#4F99FF")
        
        AppVLayout = QVBoxLayout()
        AppVLayout.setContentsMargins(0,0,0,0)
        self.NavBar = BarraDeNavegacion()
        self.ConfigBar = BarraDeConfiguracion()

        self.NavBar.navAlumnos.clicked.connect(lambda:self.navigateTo("Alumn"))
        self.NavBar.navProfesores.clicked.connect(lambda:self.navigateTo("Prof"))
        self.NavBar.navCoordinadores.clicked.connect(lambda:self.navigateTo("Coor"))
        self.NavBar.navCarreras.clicked.connect(lambda:self.navigateTo("Car"))
        self.NavBar.navSalones.clicked.connect(lambda:self.navigateTo("Sal"))
        self.NavBar.navMaterias.clicked.connect(lambda:self.navigateTo("Mat"))
        self.NavBar.navGrupos.clicked.connect(lambda:self.navigateTo("Gru"))

        self.ConfigBar.navSalir.clicked.connect(lambda:app.quit())

        self.frmAlumnos = QFrame()
        self.frmAlumnos.setContentsMargins(0,0,0,0)
        self.frmAlumnos.setFixedSize(DynamicFrameQSize)
        self.frmAlumnos.setStyleSheet(GetFrameBackGroundStyle("#FFA600"))
        self.frmAlumnosHlayout = QHBoxLayout()
        self.frmAlumnosHlayout2 = QHBoxLayout()
        self.frmAlumnosVlayout = QVBoxLayout()
        self.frmAlumnos.label = QLabel()
        self.frmAlumnos.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.frmAlumnos.pixmap = QPixmap("img/alumnos.png")
        self.frmAlumnos.pixmap2 = self.frmAlumnos.pixmap.scaled(500, 400)
        self.frmAlumnos.label.setPixmap(self.frmAlumnos.pixmap2)
        self.frmAlumnos.label2 = QLabel()
        self.frmAlumnos.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.frmAlumnos.pixmap3 = QPixmap("img/menuAlumnos.png")
        self.frmAlumnos.pixmap4 = self.frmAlumnos.pixmap3.scaled(500, 400)
        self.frmAlumnos.label2.setPixmap(self.frmAlumnos.pixmap4)
        self.frmAlumnos.botonAgregar = QPushButton("Agregar")
        self.frmAlumnos.botonAgregar.setFixedSize(150, 50)
        self.frmAlumnos.botonAgregar.clicked.connect(lambda:self.ventanaRegistroAlumnos())
        self.frmAlumnos.botonAgregar.setStyleSheet("background-color:#0087FF;")
        self.frmAlumnos.botonBuscar = QPushButton("Buscar")
        self.frmAlumnos.botonBuscar.setFixedSize(150, 50)
        self.frmAlumnos.botonBuscar.setStyleSheet("background-color:#0087FF;")
        self.frmAlumnos.botonBuscar.clicked.connect(lambda:self.ventanaBuscarAlumnos())
        self.frmAlumnos.botonMostrar = QPushButton("Mostrar")
        self.frmAlumnos.botonMostrar.setFixedSize(150, 50)
        self.frmAlumnos.botonMostrar.setStyleSheet("background-color:#0087FF;")
        self.frmAlumnos.botonMostrar.clicked.connect(lambda:self.ventanaMostrarAlumnos())
        self.frmAlumnos.botonEliminar = QPushButton("Eliminar")
        self.frmAlumnos.botonEliminar.setFixedSize(150, 50)
        self.frmAlumnos.botonEliminar.setStyleSheet("background-color:#0087FF;")
        self.frmAlumnos.botonEliminar.clicked.connect(lambda:self.ventanaEliminarAlumnos())
        self.frmAlumnosHlayout.addWidget(self.frmAlumnos.label2)
        self.frmAlumnosHlayout.addWidget(self.frmAlumnos.label)
        self.frmAlumnosVlayout.addLayout(self.frmAlumnosHlayout)
        self.frmAlumnosHlayout2.addWidget(self.frmAlumnos.botonAgregar,Qt.AlignmentFlag.AlignCenter)
        self.frmAlumnosHlayout2.addWidget(self.frmAlumnos.botonBuscar,Qt.AlignmentFlag.AlignCenter)
        self.frmAlumnosHlayout2.addWidget(self.frmAlumnos.botonMostrar,Qt.AlignmentFlag.AlignCenter)
        self.frmAlumnosHlayout2.addWidget(self.frmAlumnos.botonEliminar,Qt.AlignmentFlag.AlignCenter)
        self.frmAlumnosVlayout.addLayout(self.frmAlumnosHlayout2)
        self.frmAlumnos.setLayout(self.frmAlumnosVlayout)


        self.frmProfesores = QFrame()
        self.frmProfesores.setContentsMargins(0,0,0,0)
        self.frmProfesores.setFixedSize(DynamicFrameQSize)
        self.frmProfesores.setStyleSheet(GetFrameBackGroundStyle("#00FF00"))
        self.frmProfesores.setVisible(False)
        self.frmProfesoresHlayout = QHBoxLayout()
        self.frmProfesoresHlayout2 = QHBoxLayout()
        self.frmProfesoresVlayout = QVBoxLayout()
        self.frmProfesores.label = QLabel()
        self.frmProfesores.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.frmProfesores.pixmap = QPixmap("img/profesores.png")
        self.frmProfesores.pixmap2 = self.frmProfesores.pixmap.scaled(500, 400)
        self.frmProfesores.label.setPixmap(self.frmProfesores.pixmap2)
        self.frmProfesores.label2 = QLabel()
        self.frmProfesores.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.frmProfesores.pixmap3 = QPixmap("img/menuProfesores.png")
        self.frmProfesores.pixmap4 = self.frmProfesores.pixmap3.scaled(500, 400)
        self.frmProfesores.label2.setPixmap(self.frmProfesores.pixmap4)
        self.frmProfesores.botonAgregar = QPushButton("Agregar")
        self.frmProfesores.botonAgregar.setFixedSize(150, 50)
        self.frmProfesores.botonAgregar.setStyleSheet("background-color:#0087FF;")
        self.frmProfesores.botonAgregar.clicked.connect(lambda:self.ventanaRegistroProfesores())
        self.frmProfesores.botonBuscar = QPushButton("Buscar")
        self.frmProfesores.botonBuscar.setFixedSize(150, 50)
        self.frmProfesores.botonBuscar.setStyleSheet("background-color:#0087FF;")
        self.frmProfesores.botonBuscar.clicked.connect(lambda:self.ventanaBuscarProfesores())
        self.frmProfesores.botonMostrar = QPushButton("Mostrar")
        self.frmProfesores.botonMostrar.setFixedSize(150, 50)
        self.frmProfesores.botonMostrar.setStyleSheet("background-color:#0087FF;")
        self.frmProfesores.botonMostrar.clicked.connect(lambda:self.ventanaMostrarProfesores())
        self.frmProfesores.botonEliminar = QPushButton("Eliminar")
        self.frmProfesores.botonEliminar.setFixedSize(150, 50)
        self.frmProfesores.botonEliminar.setStyleSheet("background-color:#0087FF;")
        self.frmProfesores.botonEliminar.clicked.connect(lambda:self.ventanaEliminarProfesores())
        self.frmProfesoresHlayout.addWidget(self.frmProfesores.label2)
        self.frmProfesoresHlayout.addWidget(self.frmProfesores.label)
        self.frmProfesoresVlayout.addLayout(self.frmProfesoresHlayout)
        self.frmProfesoresHlayout2.addWidget(self.frmProfesores.botonAgregar,Qt.AlignmentFlag.AlignCenter)
        self.frmProfesoresHlayout2.addWidget(self.frmProfesores.botonBuscar,Qt.AlignmentFlag.AlignCenter)
        self.frmProfesoresHlayout2.addWidget(self.frmProfesores.botonMostrar,Qt.AlignmentFlag.AlignCenter)
        self.frmProfesoresHlayout2.addWidget(self.frmProfesores.botonEliminar,Qt.AlignmentFlag.AlignCenter)
        self.frmProfesoresVlayout.addLayout(self.frmProfesoresHlayout2)
        self.frmProfesores.setLayout(self.frmProfesoresVlayout)

        self.frmCoordinadores = QFrame()
        self.frmCoordinadores.setContentsMargins(0,0,0,0)
        self.frmCoordinadores.setFixedSize(DynamicFrameQSize)
        self.frmCoordinadores.setStyleSheet(GetFrameBackGroundStyle("#FF00FE"))
        self.frmCoordinadores.setVisible(False)
        self.frmCoordinadoresHlayout = QHBoxLayout()
        self.frmCoordinadoresHlayout2 = QHBoxLayout()
        self.frmCoordinadoresVlayout = QVBoxLayout()
        self.frmCoordinadores.label = QLabel()
        self.frmCoordinadores.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.frmCoordinadores.pixmap = QPixmap("img/coordinadores.png")
        self.frmCoordinadores.pixmap2 = self.frmCoordinadores.pixmap.scaled(500, 400)
        self.frmCoordinadores.label.setPixmap(self.frmCoordinadores.pixmap2)
        self.frmCoordinadores.label2 = QLabel()
        self.frmCoordinadores.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.frmCoordinadores.pixmap3 = QPixmap("img/menuCoordinadores.png")
        self.frmCoordinadores.pixmap4 = self.frmCoordinadores.pixmap3.scaled(500, 400)
        self.frmCoordinadores.label2.setPixmap(self.frmCoordinadores.pixmap4)
        self.frmCoordinadores.botonAgregar = QPushButton("Agregar")
        self.frmCoordinadores.botonAgregar.setFixedSize(150, 50)
        self.frmCoordinadores.botonAgregar.setStyleSheet("background-color:#0087FF;")
        self.frmCoordinadores.botonAgregar.clicked.connect(lambda:self.ventanaRegistroCoordinadores())
        self.frmCoordinadores.botonBuscar = QPushButton("Buscar")
        self.frmCoordinadores.botonBuscar.setFixedSize(150, 50)
        self.frmCoordinadores.botonBuscar.setStyleSheet("background-color:#0087FF;")
        self.frmCoordinadores.botonBuscar.clicked.connect(lambda:self.ventanaBuscarCoordinadores())
        self.frmCoordinadores.botonMostrar = QPushButton("Mostrar")
        self.frmCoordinadores.botonMostrar.setFixedSize(150, 50)
        self.frmCoordinadores.botonMostrar.setStyleSheet("background-color:#0087FF;")
        self.frmCoordinadores.botonMostrar.clicked.connect(lambda:self.ventanaMostrarCoordinadores())
        self.frmCoordinadores.botonEliminar = QPushButton("Eliminar")
        self.frmCoordinadores.botonEliminar.setFixedSize(150, 50)
        self.frmCoordinadores.botonEliminar.setStyleSheet("background-color:#0087FF;")
        self.frmCoordinadores.botonEliminar.clicked.connect(lambda:self.ventanaEliminarCoordinadores())
        self.frmCoordinadoresHlayout.addWidget(self.frmCoordinadores.label2)
        self.frmCoordinadoresHlayout.addWidget(self.frmCoordinadores.label)
        self.frmCoordinadoresVlayout.addLayout(self.frmCoordinadoresHlayout)
        self.frmCoordinadoresHlayout2.addWidget(self.frmCoordinadores.botonAgregar,Qt.AlignmentFlag.AlignCenter)
        self.frmCoordinadoresHlayout2.addWidget(self.frmCoordinadores.botonBuscar,Qt.AlignmentFlag.AlignCenter)
        self.frmCoordinadoresHlayout2.addWidget(self.frmCoordinadores.botonMostrar,Qt.AlignmentFlag.AlignCenter)
        self.frmCoordinadoresHlayout2.addWidget(self.frmCoordinadores.botonEliminar,Qt.AlignmentFlag.AlignCenter)
        self.frmCoordinadoresVlayout.addLayout(self.frmCoordinadoresHlayout2)
        self.frmCoordinadores.setLayout(self.frmCoordinadoresVlayout)

        self.frmCarreras = QFrame()
        self.frmCarreras.setContentsMargins(0,0,0,0)
        self.frmCarreras.setFixedSize(DynamicFrameQSize)
        self.frmCarreras.setStyleSheet(GetFrameBackGroundStyle("#800080"))
        self.frmCarreras.setVisible(False)
        self.frmCarrerasHlayout = QHBoxLayout()
        self.frmCarrerasHlayout2 = QHBoxLayout()
        self.frmCarrerasVlayout = QVBoxLayout()
        self.frmCarreras.label = QLabel()
        self.frmCarreras.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.frmCarreras.pixmap = QPixmap("img/carreras.png")
        self.frmCarreras.pixmap2 = self.frmCarreras.pixmap.scaled(500, 400)
        self.frmCarreras.label.setPixmap(self.frmCarreras.pixmap2)
        self.frmCarreras.label2 = QLabel()
        self.frmCarreras.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.frmCarreras.pixmap3 = QPixmap("img/menuCarreras.png")
        self.frmCarreras.pixmap4 = self.frmCarreras.pixmap3.scaled(500, 400)
        self.frmCarreras.label2.setPixmap(self.frmCarreras.pixmap4)
        self.frmCarreras.botonAgregar = QPushButton("Agregar")
        self.frmCarreras.botonAgregar.setFixedSize(150, 50)
        self.frmCarreras.botonAgregar.setStyleSheet("background-color:#0087FF;")
        self.frmCarreras.botonAgregar.clicked.connect(lambda:self.ventanaRegistroCarreras())
        self.frmCarreras.botonBuscar = QPushButton("Buscar")
        self.frmCarreras.botonBuscar.setFixedSize(150, 50)
        self.frmCarreras.botonBuscar.setStyleSheet("background-color:#0087FF;")
        self.frmCarreras.botonBuscar.clicked.connect(lambda:self.ventanaBuscarCarreras())
        self.frmCarreras.botonMostrar = QPushButton("Mostrar")
        self.frmCarreras.botonMostrar.setFixedSize(150, 50)
        self.frmCarreras.botonMostrar.setStyleSheet("background-color:#0087FF;")
        self.frmCarreras.botonMostrar.clicked.connect(lambda:self.ventanaMostrarCarreras())
        self.frmCarreras.botonEliminar = QPushButton("Eliminar")
        self.frmCarreras.botonEliminar.setFixedSize(150, 50)
        self.frmCarreras.botonEliminar.setStyleSheet("background-color:#0087FF;")
        self.frmCarreras.botonEliminar.clicked.connect(lambda:self.ventanaEliminarCarreras())
        self.frmCarreras.botonModificar = QPushButton("Modificar")
        self.frmCarreras.botonModificar.setFixedSize(150, 50)
        self.frmCarreras.botonModificar.setStyleSheet("background-color:#0087FF;")
        self.frmCarreras.botonModificar.clicked.connect(lambda:self.ventanaModificarCarreras())
        self.frmCarrerasHlayout.addWidget(self.frmCarreras.label2)
        self.frmCarrerasHlayout.addWidget(self.frmCarreras.label)
        self.frmCarrerasVlayout.addLayout(self.frmCarrerasHlayout)
        self.frmCarrerasHlayout2.addWidget(self.frmCarreras.botonAgregar,Qt.AlignmentFlag.AlignCenter)
        self.frmCarrerasHlayout2.addWidget(self.frmCarreras.botonBuscar,Qt.AlignmentFlag.AlignCenter)
        self.frmCarrerasHlayout2.addWidget(self.frmCarreras.botonMostrar,Qt.AlignmentFlag.AlignCenter)
        self.frmCarrerasHlayout2.addWidget(self.frmCarreras.botonEliminar,Qt.AlignmentFlag.AlignCenter)
        self.frmCarrerasHlayout2.addWidget(self.frmCarreras.botonModificar,Qt.AlignmentFlag.AlignCenter)
        self.frmCarrerasVlayout.addLayout(self.frmCarrerasHlayout2)
        self.frmCarreras.setLayout(self.frmCarrerasVlayout)

        self.frmSalones = QFrame()
        self.frmSalones.setContentsMargins(0,0,0,0)
        self.frmSalones.setFixedSize(DynamicFrameQSize)
        self.frmSalones.setStyleSheet(GetFrameBackGroundStyle("#FFFF00"))
        self.frmSalones.setVisible(False)
        self.frmSalonesHlayout = QHBoxLayout()
        self.frmSalonesHlayout2 = QHBoxLayout()
        self.frmSalonesVlayout = QVBoxLayout()
        self.frmSalones.label = QLabel()
        self.frmSalones.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.frmSalones.pixmap = QPixmap("img/salones.png")
        self.frmSalones.pixmap2 = self.frmSalones.pixmap.scaled(500, 400)
        self.frmSalones.label.setPixmap(self.frmSalones.pixmap2)
        self.frmSalones.label2 = QLabel()
        self.frmSalones.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.frmSalones.pixmap3 = QPixmap("img/menuSalones.png")
        self.frmSalones.pixmap4 = self.frmSalones.pixmap3.scaled(500, 400)
        self.frmSalones.label2.setPixmap(self.frmSalones.pixmap4)
        self.frmSalones.botonAgregar = QPushButton("Agregar")
        self.frmSalones.botonAgregar.setFixedSize(150, 50)
        self.frmSalones.botonAgregar.setStyleSheet("background-color:#0087FF;")
        self.frmSalones.botonAgregar.clicked.connect(lambda:self.ventanaRegistroSalones())
        self.frmSalones.botonBuscar = QPushButton("Buscar")
        self.frmSalones.botonBuscar.setFixedSize(150, 50)
        self.frmSalones.botonBuscar.setStyleSheet("background-color:#0087FF;")
        self.frmSalones.botonBuscar.clicked.connect(lambda:self.ventanaBuscarSalones())
        self.frmSalones.botonMostrar = QPushButton("Mostrar")
        self.frmSalones.botonMostrar.setFixedSize(150, 50)
        self.frmSalones.botonMostrar.setStyleSheet("background-color:#0087FF;")
        self.frmSalones.botonMostrar.clicked.connect(lambda:self.ventanaMostrarSalones())
        self.frmSalones.botonEliminar = QPushButton("Eliminar")
        self.frmSalones.botonEliminar.setFixedSize(150, 50)
        self.frmSalones.botonEliminar.setStyleSheet("background-color:#0087FF;")
        self.frmSalones.botonEliminar.clicked.connect(lambda:self.ventanaEliminarSalones())
        self.frmSalonesHlayout.addWidget(self.frmSalones.label2)
        self.frmSalonesHlayout.addWidget(self.frmSalones.label)
        self.frmSalonesVlayout.addLayout(self.frmSalonesHlayout)
        self.frmSalonesHlayout2.addWidget(self.frmSalones.botonAgregar,Qt.AlignmentFlag.AlignCenter)
        self.frmSalonesHlayout2.addWidget(self.frmSalones.botonBuscar,Qt.AlignmentFlag.AlignCenter)
        self.frmSalonesHlayout2.addWidget(self.frmSalones.botonMostrar,Qt.AlignmentFlag.AlignCenter)
        self.frmSalonesHlayout2.addWidget(self.frmSalones.botonEliminar,Qt.AlignmentFlag.AlignCenter)
        self.frmSalonesVlayout.addLayout(self.frmSalonesHlayout2)
        self.frmSalones.setLayout(self.frmSalonesVlayout)
        
        self.frmMaterias = QFrame()
        self.frmMaterias.setContentsMargins(0,0,0,0)
        self.frmMaterias.setFixedSize(DynamicFrameQSize)
        self.frmMaterias.setStyleSheet(GetFrameBackGroundStyle("#FF0000"))
        self.frmMaterias.setVisible(False)
        self.frmMateriasHlayout = QHBoxLayout()
        self.frmMateriasHlayout2 = QHBoxLayout()
        self.frmMateriasVlayout = QVBoxLayout()
        self.frmMaterias.label = QLabel()
        self.frmMaterias.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.frmMaterias.pixmap = QPixmap("img/materias.png")
        self.frmMaterias.pixmap2 = self.frmMaterias.pixmap.scaled(500, 400)
        self.frmMaterias.label.setPixmap(self.frmMaterias.pixmap2)
        self.frmMaterias.label2 = QLabel()
        self.frmMaterias.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.frmMaterias.pixmap3 = QPixmap("img/menuMaterias.png")
        self.frmMaterias.pixmap4 = self.frmMaterias.pixmap3.scaled(500, 400)
        self.frmMaterias.label2.setPixmap(self.frmMaterias.pixmap4)
        self.frmMaterias.botonAgregar = QPushButton("Agregar")
        self.frmMaterias.botonAgregar.setFixedSize(150, 50)
        self.frmMaterias.botonAgregar.setStyleSheet("background-color:#0087FF;")
        self.frmMaterias.botonAgregar.clicked.connect(lambda:self.ventanaRegistroMaterias())
        self.frmMaterias.botonBuscar = QPushButton("Buscar")
        self.frmMaterias.botonBuscar.setFixedSize(150, 50)
        self.frmMaterias.botonBuscar.setStyleSheet("background-color:#0087FF;")
        self.frmMaterias.botonBuscar.clicked.connect(lambda:self.ventanaBuscarMaterias())
        self.frmMaterias.botonMostrar = QPushButton("Mostrar")
        self.frmMaterias.botonMostrar.setFixedSize(150, 50)
        self.frmMaterias.botonMostrar.setStyleSheet("background-color:#0087FF;")
        self.frmMaterias.botonMostrar.clicked.connect(lambda:self.ventanaMostrarMaterias())
        self.frmMaterias.botonEliminar = QPushButton("Eliminar")
        self.frmMaterias.botonEliminar.setFixedSize(150, 50)
        self.frmMaterias.botonEliminar.setStyleSheet("background-color:#0087FF;")
        self.frmMaterias.botonEliminar.clicked.connect(lambda:self.ventanaEliminarMaterias())
        self.frmMaterias.botonModificar = QPushButton("Modificar")
        self.frmMaterias.botonModificar.setFixedSize(150, 50)
        self.frmMaterias.botonModificar.setStyleSheet("background-color:#0087FF;")
        self.frmMateriasHlayout.addWidget(self.frmMaterias.label2)
        self.frmMateriasHlayout.addWidget(self.frmMaterias.label)
        self.frmMateriasVlayout.addLayout(self.frmMateriasHlayout)
        self.frmMateriasHlayout2.addWidget(self.frmMaterias.botonAgregar,Qt.AlignmentFlag.AlignCenter)
        self.frmMateriasHlayout2.addWidget(self.frmMaterias.botonBuscar,Qt.AlignmentFlag.AlignCenter)
        self.frmMateriasHlayout2.addWidget(self.frmMaterias.botonMostrar,Qt.AlignmentFlag.AlignCenter)
        self.frmMateriasHlayout2.addWidget(self.frmMaterias.botonEliminar,Qt.AlignmentFlag.AlignCenter)
        self.frmMateriasHlayout2.addWidget(self.frmMaterias.botonModificar,Qt.AlignmentFlag.AlignCenter)
        self.frmMateriasVlayout.addLayout(self.frmMateriasHlayout2)
        self.frmMaterias.setLayout(self.frmMateriasVlayout)

        self.frmGrupos = QFrame()
        self.frmGrupos.setContentsMargins(0,0,0,0)
        self.frmGrupos.setFixedSize(DynamicFrameQSize)
        self.frmGrupos.setStyleSheet(GetFrameBackGroundStyle("#C0C0C0"))
        self.frmGrupos.setVisible(False)
        self.frmGruposHlayout = QHBoxLayout()
        self.frmGruposHlayout2 = QHBoxLayout()
        self.frmGruposVlayout = QVBoxLayout()
        self.frmGrupos.label = QLabel()
        self.frmGrupos.label.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.frmGrupos.pixmap = QPixmap("img/grupos.png")
        self.frmGrupos.pixmap2 = self.frmGrupos.pixmap.scaled(500, 400)
        self.frmGrupos.label.setPixmap(self.frmGrupos.pixmap2)
        self.frmGrupos.label2 = QLabel()
        self.frmGrupos.label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.frmGrupos.pixmap3 = QPixmap("img/menuGrupos.png")
        self.frmGrupos.pixmap4 = self.frmGrupos.pixmap3.scaled(500, 400)
        self.frmGrupos.label2.setPixmap(self.frmGrupos.pixmap4)
        self.frmGrupos.botonAgregar = QPushButton("Agregar")
        self.frmGrupos.botonAgregar.setFixedSize(150, 50)
        self.frmGrupos.botonAgregar.setStyleSheet("background-color:#0087FF;")
        self.frmGrupos.botonAgregar.clicked.connect(lambda:self.ventanaRegistroGrupos())
        self.frmGrupos.botonBuscar = QPushButton("Buscar")
        self.frmGrupos.botonBuscar.setFixedSize(150, 50)
        self.frmGrupos.botonBuscar.setStyleSheet("background-color:#0087FF;")
        self.frmGrupos.botonBuscar.clicked.connect(lambda:self.ventanaBuscarGrupos())
        self.frmGrupos.botonMostrar = QPushButton("Mostrar")
        self.frmGrupos.botonMostrar.setFixedSize(150, 50)
        self.frmGrupos.botonMostrar.setStyleSheet("background-color:#0087FF;")
        self.frmGrupos.botonMostrar.clicked.connect(lambda:self.ventanaMostrarGrupos())
        self.frmGrupos.botonEliminar = QPushButton("Eliminar")
        self.frmGrupos.botonEliminar.setFixedSize(150, 50)
        self.frmGrupos.botonEliminar.setStyleSheet("background-color:#0087FF;")
        self.frmGrupos.botonEliminar.clicked.connect(lambda:self.ventanaEliminarGrupos())
        self.frmGruposHlayout.addWidget(self.frmGrupos.label2)
        self.frmGruposHlayout.addWidget(self.frmGrupos.label)
        self.frmGruposVlayout.addLayout(self.frmGruposHlayout)
        self.frmGruposHlayout2.addWidget(self.frmGrupos.botonAgregar,Qt.AlignmentFlag.AlignCenter)
        self.frmGruposHlayout2.addWidget(self.frmGrupos.botonBuscar,Qt.AlignmentFlag.AlignCenter)
        self.frmGruposHlayout2.addWidget(self.frmGrupos.botonMostrar,Qt.AlignmentFlag.AlignCenter)
        self.frmGruposHlayout2.addWidget(self.frmGrupos.botonEliminar,Qt.AlignmentFlag.AlignCenter)
        self.frmGruposVlayout.addLayout(self.frmGruposHlayout2)
        self.frmGrupos.setLayout(self.frmGruposVlayout)

        AppVLayout.addWidget(self.NavBar,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.frmAlumnos,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.frmProfesores,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.frmCoordinadores,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.frmCarreras,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.frmSalones,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.frmMaterias,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.frmGrupos,QtCore.Qt.AlignmentFlag.AlignTop)
        AppVLayout.addWidget(self.ConfigBar,QtCore.Qt.AlignmentFlag.AlignBottom)

        self.MainWidget.setLayout(AppVLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def navigateTo(self,frameName:str):
        if(frameName=="Alumn"):
            self.setAllInvisible()
            self.frmAlumnos.setVisible(True)
        elif(frameName=="Prof"):
            self.setAllInvisible()
            self.frmProfesores.setVisible(True)
        elif(frameName=="Coor"):
            self.setAllInvisible()
            self.frmCoordinadores.setVisible(True)
        elif(frameName=="Car"):
            self.setAllInvisible()
            self.frmCarreras.setVisible(True)
        elif(frameName=="Sal"):
            self.setAllInvisible()
            self.frmSalones.setVisible(True)
        elif(frameName=="Mat"):
            self.setAllInvisible()
            self.frmMaterias.setVisible(True)
        elif(frameName=="Gru"):
            self.setAllInvisible()
            self.frmGrupos.setVisible(True)

    def setAllInvisible(self):
        self.frmAlumnos.setVisible(False)
        self.frmProfesores.setVisible(False)
        self.frmCoordinadores.setVisible(False)
        self.frmCarreras.setVisible(False)
        self.frmSalones.setVisible(False)
        self.frmMaterias.setVisible(False)
        self.frmGrupos.setVisible(False)

    def ventanaRegistroAlumnos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormAlumnos()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaBuscarAlumnos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormBAlumnos()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaMostrarAlumnos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMAlumnos()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaEliminarAlumnos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormEAlumnos()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaRegistroProfesores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormProfesores()
        self.ui2.setupUi(self.form)
        self.form.show()

    def ventanaBuscarProfesores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormBProfesores()
        self.ui2.setupUi(self.form)
        self.form.show()

    def ventanaMostrarProfesores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMProfesores()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaEliminarProfesores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormEProfesores()
        self.ui2.setupUi(self.form)
        self.form.show()

    def ventanaRegistroCoordinadores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormCoordinadores()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaBuscarCoordinadores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormBCoordinadores()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaMostrarCoordinadores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMCoordinadores()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaEliminarCoordinadores(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormECoordinadores()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaRegistroCarreras(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormCarreras()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaBuscarCarreras(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormBCarreras()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaMostrarCarreras(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMCarreras()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaEliminarCarreras(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormECarreras()
        self.ui2.setupUi(self.form)
        self.form.show()

    def ventanaModificarCarreras(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMOCarreras()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaRegistroSalones(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormSalones()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaBuscarSalones(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormBSalones()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaMostrarSalones(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMSalones()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaEliminarSalones(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormESalones()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaRegistroMaterias(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMaterias()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaBuscarMaterias(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormBMaterias()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaMostrarMaterias(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMMaterias()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaEliminarMaterias(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormEMaterias()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaRegistroGrupos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormGrupos()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaBuscarGrupos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormBGrupos()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaMostrarGrupos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormMGrupos()
        self.ui2.setupUi(self.form)
        self.form.show()
    
    def ventanaEliminarGrupos(self):
        self.form = QWidget() 
        self.ui2 = Ui_FormEGrupos()
        self.ui2.setupUi(self.form)
        self.form.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "myUniversity - Menu Principal"))

if __name__ == "__main__":
    try:
        print("CARGANDO GUI")
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        
    except Exception as ex:
        print("Excepcion en metodo cargarGUI() -> " + str(ex))