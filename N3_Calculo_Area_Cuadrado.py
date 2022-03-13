import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N3_Calculo_Area_Cuadrado.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btnCalculo.clicked.connect(self.ejecalculo)

    # Área de los Slots
    def ejecalculo(self):
        lado = float(self.txtLado.text())
        ar= lado**2
        self.calculo(ar)

    def calculo(self,res):
        m = QtWidgets.QMessageBox()
        m.setText("El area es igual a: "+str(res))
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

