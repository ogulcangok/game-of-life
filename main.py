from field import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from threading import Thread
import time
import sys

class Window(QMainWindow):
	BLOCK_SIZE = 10
	def __init__(self, ioclass):
		super().__init__()
		self.field = ioclass
		self.home()
		self.start()
		self.running = True

	def home(self):
		width = self.field.colsize * self.BLOCK_SIZE
		height = self.field.rowsize * self.BLOCK_SIZE
		# x y height width
		self.setGeometry(50, 50, width, height)
		self.setWindowTitle('Game of Life Simulator')
		self.show()

	def stop(self):
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

def ticker(field, window):
	print('Thread init complete')
	while True:
		time.sleep(0.5)
		if window.running:
			field.tick()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	field = Field(50, 50)

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
	sys.exit(app.exec_())