import sys
import random

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(self.size())
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = random.randint(1, self.height() // 2)
            x, y = random.randint(r, self.width() - r), random.randint(r, self.height() - r)
            qp.drawEllipse(QPoint(x, y), r, r)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
