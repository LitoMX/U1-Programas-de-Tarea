import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N10_Ecuacion_lineal_ax+b.ui"   # Nombre del archivo aqui
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
        A = float(self.txtA.text())
        X = float(self.txtX.text())
        B =float(self.txtB.text())
        self.txtA.setText("")
        self.txtX.setText("")
        self.txtB.setText("")
        res=A*X+B
        n = QtWidgets.QMessageBox()
        n.setText(f"El resultado es:: {res} ")
        n.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())