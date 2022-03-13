import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N6_Discriminante_Matriz_2X2.ui"   # Nombre del archivo aqui
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
        m00 = int(self.txtMatriz00.text())
        m01 = int(self.txtMatriz01.text())
        m10 = int(self.txtMatriz10.text())
        m11 = int(self.txtMatriz11.text())
        self.txtMatriz00.setText("")
        self.txtMatriz01.setText("")
        self.txtMatriz10.setText("")
        self.txtMatriz11.setText("")
        Determinante = (m00*m11)-(m10*m01)

        n = QtWidgets.QMessageBox()
        n.setText(f"La determinante de la matriz es: {Determinante}")
        n.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())