from field import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from threading import Thread
import time
import sys


class Window(QMainWindow):
    BLOCK_SIZE = 10

    # ioclass = Field type object.
    def __init__(self, ioclass):
        """ Args:ioclass (Field): Main cell matrix which that the window process"""
        super().__init__()
        self.field = ioclass
        width = self.field.rowsize * self.BLOCK_SIZE
        height = self.field.colsize * self.BLOCK_SIZE
        # x y height width
        self.setGeometry(50, 50, width, height)
        self.setWindowTitle('Game of Life Simulator')
        self.show()
        self.start()
        self.running = True

    def stop(self):
        """ This function is called only when program closes. """
        self.running = False

    def start(self):
        self.running = True

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)

        for row in self.field.field:
            for cell in row:
                self.paint_block(qp, cell)

        qp.end()

        self.update()

    def mousePressEvent(self, QMouseEvent):
        pos = QMouseEvent.pos()

        block_x = pos.x() // self.BLOCK_SIZE
        block_y = pos.y() // self.BLOCK_SIZE

        print(block_x, block_y)

        self.field.field[block_y][block_x].on()

    def keyPressEvent(self, e):
        # Pause the simulation if space key has hit
        if e.key() == Qt.Key_Space:
            if field.running:
                field.stop()
            else:
                field.start()

    def paint_block(self, qp, cell):
        color = QColor(0, 0, 0)
        if cell.alive:
            color = QColor(255, 255, 255)
        else:
            color = QColor(0, 0, 0)

        qp.setPen(color)
        qp.setBrush(color)
        qp.drawRect(
            cell.x * self.BLOCK_SIZE,
            cell.y * self.BLOCK_SIZE,
            self.BLOCK_SIZE,
            self.BLOCK_SIZE
        )


# Thread timer function
def ticker(field, window):
    print('Thread init complete.')
    while window.running:
        time.sleep(0.25)
        if field.running:
            field.tick()
    print('Thread terminated.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    field = Field(100, 50)

    field.field[10][10].on()
    field.field[9][11].on()
    field.field[8][11].on()
    field.field[9][12].on()
    field.field[8][10].on()

    window = Window(field)
    thread = Thread(target=ticker, args=[field, window])
    print('Thread created')
    thread.start()
    print('Thread running')
    ret = app.exec_()
    window.running = False
    sys.exit(ret)
