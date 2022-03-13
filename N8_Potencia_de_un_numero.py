import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N8_Potencia_de_un_numero.ui"   # Nombre del archivo aqui
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
        numero = int(self.txtNumero.text())
        exponente = int(self.txtExponente.text())
        self.txtNumero.setText("")
        self.txtExponente.setText("")
        potencia=numero**exponente
        n = QtWidgets.QMessageBox()
        n.setText(f"La potencia es: {potencia} ")
        n.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())