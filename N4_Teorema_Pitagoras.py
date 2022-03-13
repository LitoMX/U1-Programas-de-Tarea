import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "N4_Teorema_Pitagoras.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.teorema)

    def teorema(self):
        m = QtWidgets.QMessageBox()

        if self.txt_a.text() == "" and self.txt_b.text() == "" or self.txt_a.text() == "" and self.txt_c.text() == "" \
                or self.txt_b.text() == "" and self.txt_c.text() == "":
            m.setText("Faltan Ingresar Valores")
            m.exec()

        #Calcular lado a
        elif self.txt_a.text() == "":
            try:
                b = float(self.txt_b.text())
                c = float(self.txt_c.text())

                a = math.sqrt(pow(c, 2) - pow(b, 2))

                m.setText("a = "+str(a))
                m.exec()

            except (ValueError,TypeError,IndexError):
                m.setText("Valores Incorrectos")
                m.exec()

        # Calcular lado b
        elif self.txt_b.text() == "":
            try:
                a = int(self.txt_a.text())
                c = int(self.txt_c.text())

                b = math.sqrt(pow(c, 2) - pow(a, 2))

                m.setText("b = " + str(b))
                m.exec()

            except (ValueError,TypeError,IndexError):
                m.setText("Valores Incorrectos")
                m.exec()

        # Calcular lado c
        elif self.txt_c.text() == "":
            try:
                a = int(self.txt_a.text())
                b = int(self.txt_b.text())

                c = math.sqrt(pow(a,2) + pow(b,2))

                m.setText("c = " + str(c))
                m.exec()

            except (ValueError,TypeError,IndexError):
                m.setText("Valores Incorrectos")
                m.exec()

        else:
            m.setText("No Hay Incognitas ")
            m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
