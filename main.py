import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
import random

class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 200)
        self.circle_diameter = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor("yellow"))
        painter.drawEllipse(self.rect().center(), self.circle_diameter, self.circle_diameter)

    def setCircleDiameter(self, diameter):
        self.circle_diameter = diameter
        self.update()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("кружочек")
        self.circle_widget = CircleWidget()
        self.button = QPushButton("Создать кружочек")
        self.button.clicked.connect(self.createCircle)
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.circle_widget)
        layout.addWidget(self.button)
        self.setCentralWidget(central_widget)

    def createCircle(self):
        diameter = random.randint(20, 100)
        self.circle_widget.setCircleDiameter(diameter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
