import random
import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt



class Fort(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.flag = False
        self.push.clicked.connect(self.click)

    def click(self):
        self.flag = True
        self.update()
    def paintEvent(self, event):
        sp = []
        if self.flag:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 8, Qt.DashLine))
            f = random.randint(500, 800)
            t = random.randint(850, 1150)
            painter.drawEllipse(40, 40, f, f)
            painter.drawEllipse(700, 40, t, t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Fort()
    ex.show()
    sys.exit(app.exec_())

