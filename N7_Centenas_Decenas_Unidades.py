import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N7_Centenas_Decenas_Unidades.ui"   # Nombre del archivo aqui
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

        centenas = int(numero/100)
        decenas= int((numero-centenas*100)/10)
        unidades= numero-(centenas*100+decenas*10)
        self.txtNumero.setText("")
        print(centenas)
        print(decenas)
        print(unidades)
        n = QtWidgets.QMessageBox()
        n.setText(f"Centenas: {int(centenas)}\n"
                  f"Decenas : {int(decenas)}\n"
                  f"Unidades: {int(unidades)}")
        n.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())