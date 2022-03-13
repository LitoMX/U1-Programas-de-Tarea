import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N1_Presentacion.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_Presentacion.clicked.connect(self.ejecutarPresentacion)
    # Área de los Slots
    def ejecutarPresentacion(self):
        presentacion = """
        Universidad Autónoma de Tamaulipas
    Facultad de Ingeniería “Arturo Narro Siller” 

Equipo 1:
  * Guillu Perez Cristian Jesus
  * Juarez Navarro Francisco Javier
  * Piñeiro Santiago Alma Elisa
  * Rodriguez Silguero Luis Francisco
  * Sanchez Perez Miguel Angel
 
Carrera: Ing. En Sistemas Computacionales
 
                  “Programas Python”
 
  Materia: Programación de Interfaces y Puertos
 
    Docente: Garcia Ruiz Alejandro Humberto 
 
                          Grupo: “G”
"""
        m = QtWidgets.QMessageBox()
        m.setText(presentacion)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
