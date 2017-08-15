import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import os
from os import listdir

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):

        # Show  image
        self.pic = QLabel(self)
        #self.pic.setGeometry(10, 10, 800, 800)
        self.pic.setPixmap(QPixmap("image1.jpg"))

        # Show button
        btn = QPushButton('Next', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.fun)
        btn.move(50, 50)


        self.setGeometry(300, 300, 2000, 1500)
        self.setWindowTitle('Tooltips')
        self.show()

    # Connect button to image updating
    def fun(self):
        self.pic.setPixmap(QPixmap("image2.jpg"))

def main():

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
