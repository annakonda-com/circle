import sys
import random

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QApplication
from UI import Ui_Form
from random import choice


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            r = choice(range(0, 256))
            g = choice(range(0, 256))
            b = choice(range(0, 256))
            qp.setBrush(QColor(r, g, b))
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
