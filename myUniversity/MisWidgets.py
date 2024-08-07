from PyQt5.QtWidgets import QFrame,QWidget,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtCore import QSize,Qt
from Estilos import GetFrameBackGroundStyle, GetWidgetBackGroundColor

class BarraDeNavegacion(QWidget):
    def __init__(self):
        QWidget.__init__(self,parent=None)
        self.setStyleSheet("background-color:black;")
        self.mainHlayout = QHBoxLayout()
        self.setFixedSize(1200,100)

        self.navAlumnos = QPushButton("Alumnos")
        self.navAlumnos.setFixedSize(QSize(150,50))
        self.navAlumnos.setStyleSheet("background-color:#FCFF59;")
        self.navProfesores = QPushButton("Profesores")
        self.navProfesores.setFixedSize(150,50)
        self.navProfesores.setStyleSheet("background-color:#FCFF59;")
        self.navCoordinadores = QPushButton("Coordinador")
        self.navCoordinadores.setFixedSize(QSize(150,50))
        self.navCoordinadores.setStyleSheet("background-color:#FCFF59;")
        self.navCarreras = QPushButton("Carrera")
        self.navCarreras.setFixedSize(QSize(150,50))
        self.navCarreras.setStyleSheet("background-color:#FCFF59;")
        self.navSalones = QPushButton("Salon")
        self.navSalones.setFixedSize(QSize(150,50))
        self.navSalones.setStyleSheet("background-color:#FCFF59;")
        self.navMaterias = QPushButton("Materia")
        self.navMaterias.setFixedSize(QSize(150,50))
        self.navMaterias.setStyleSheet("background-color:#FCFF59;")
        self.navGrupos = QPushButton("Grupo")
        self.navGrupos.setFixedSize(QSize(150,50))
        self.navGrupos.setStyleSheet("background-color:#FCFF59;")
        
        self.mainHlayout.addWidget(self.navAlumnos,Qt.AlignmentFlag.AlignCenter)
        self.mainHlayout.addWidget(self.navProfesores,Qt.AlignmentFlag.AlignCenter)
        self.mainHlayout.addWidget(self.navCoordinadores,Qt.AlignmentFlag.AlignCenter)
        self.mainHlayout.addWidget(self.navCarreras,Qt.AlignmentFlag.AlignCenter)
        self.mainHlayout.addWidget(self.navSalones,Qt.AlignmentFlag.AlignCenter)
        self.mainHlayout.addWidget(self.navMaterias,Qt.AlignmentFlag.AlignCenter)
        self.mainHlayout.addWidget(self.navGrupos,Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.mainHlayout)
        

class BarraDeConfiguracion(QWidget):
    def __init__(self):
        QWidget.__init__(self,parent=None)
        self.mainHlayout = QHBoxLayout()
        self.setFixedSize(1200,100)

        self.navSalir = QPushButton("Salir")
        self.navSalir.setFixedSize(QSize(150,50))
        self.navSalir.setStyleSheet("background-color:red;")

        self.mainHlayout.addWidget(self.navSalir,Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.mainHlayout)
        
