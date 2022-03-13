import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N2_Calculo_IMC.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_calcular.clicked.connect(self.ejecutar_calculo)

    # Área de los Slots
    def ejecutar_calculo(self):
        peso = float(self.txt_peso.text())
        estatura =float(self.txt_estatura.text())
        imc = peso/(estatura**2)
        imc = round(imc,2)
        self.calcular(imc)

    def calcular(self,res):
        m = QtWidgets.QMessageBox()
        m.setText("Tu IMC es de : "+str(res))
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

