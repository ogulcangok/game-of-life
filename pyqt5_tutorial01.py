# -*- coding: utf-8 -*-
"""
gathered from http://zetcode.com/gui/pyqt5/firstprograms/
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 250)
    w.move(1200, 20)
    w.setWindowTitle('Start Simple')
    w.show()

    sys.exit(app.exec_())