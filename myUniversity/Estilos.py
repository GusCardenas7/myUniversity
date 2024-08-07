from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtCore import QSize

DynamicFrameQSize = QSize(1200,600)

def GetWidgetBackGroundColor(rgb:str):
    pallet = None
    try:
        color = QColor(rgb)
        wdg = QWidget()
        pallet = wdg.palette()
        pallet.setColor(QPalette.Window,color)
    except Exception as ex:
        print("Excepcion en metodo GetWidgetBackGroundColor()" + str(ex))
    return pallet

def GetFrameBackGroundStyle(rgb:str):
    return "QFrame { background-color:"+rgb+";}"
        

    
    
