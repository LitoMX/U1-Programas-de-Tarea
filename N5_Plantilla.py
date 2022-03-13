import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N5_Plantilla.ui"   # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Area de los signals
        self.btn_Calcular.clicked.connect(self.calcular)

    # Area de los Stats
    def calcular(self):
        ax = int(self.txt_Ax.text())
        ay = int(self.txt_Ay.text())
        bx = int(self.txt_Bx.text())
        by = int(self.txt_By.text())
        dAB = math.sqrt((bx - ax)**2 + (by - ay)**2)
        n = QtWidgets.QMessageBox()
        n.setText(f"La distancia entre los puntos A y B es de: {dAB}")
        n.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


