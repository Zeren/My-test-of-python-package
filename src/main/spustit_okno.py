from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel
from PySide2 import QtCore
import sys, os
from .Main_window import Ui_MainWindow
import time
import numpy as np

class Measurement_window(QMainWindow):
    def __init__(self):
        super(Measurement_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.blokovaci_funkce)

        self.novy_thread = worker()
        self.novy_thread.merena_data.connect(self.navracena_data_po_dokonceni_funkce_v_threadu)
        self.ui.pushButton_2.clicked.connect(self.neblokovaci_funkce)

    def blokovaci_funkce(self):
        # Ted to na 3 sekundy zaseknu
        self.ui.textEdit.append('Ted na 10 sekund zaseknu program')
        time.sleep(3)
        self.ui.textEdit.append('Program pokracuje')

    def neblokovaci_funkce(self): # nastavi a spusti workera, ktery nazablolokuje program
        if self.ui.radioButton_1.isChecked():
            self.novy_thread.set_freq_range(9e3, 100e3, 11)
        elif self.ui.radioButton_2.isChecked():
            self.novy_thread.set_freq_range(100e3, 1e6, 11)
        elif self.ui.radioButton_3.isChecked():
            self.novy_thread.set_freq_range(1e6, 30e6, 11)
        elif self.ui.radioButton_4.isChecked():
            self.novy_thread.set_freq_range(30e6, 1e9, 11)
        self.novy_thread.start()
        self.ui.textEdit.append('Nezablokoval program, ale spustil thread')
        self.ui.textEdit.append('Po dokonceni vypise "data":')

    def navracena_data_po_dokonceni_funkce_v_threadu(self, data):
        np.set_printoptions(precision=3)
        self.ui.textEdit.append(str(data))

class worker(QtCore.QThread):
    merena_data = QtCore.Signal(np.ndarray) # Toto je signal ktery to vrati s daty

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.freq = np.array([])

    def set_freq_range(self, start, stop, points):
        self.freq = np.linspace(start, stop, points)

    def run(self):
        time.sleep(3)
        measurement = np.random.rand(self.freq.size)
        self.merena_data.emit(measurement)

def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    window = Measurement_window()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
