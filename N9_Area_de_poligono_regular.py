import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N9_Area_de_poligono_regular.ui"   # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los signals
        self.btnCalcular.clicked.connect(self.calcular)

    # Area de los Stats
    def calcular(self):
        Nlados = float(self.txtNlados.text())
        Lado = float(self.txtLado.text())
        Apotema =float(self.txtApotema.text())
        self.txtNlados.setText("")
        self.txtLado.setText("")
        self.txtApotema.setText("")
        area = (Nlados*Lado*Apotema)/2
        n = QtWidgets.QMessageBox()
        n.setText(f"El area del poligono es:: {round(area,2)} ")
        n.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())