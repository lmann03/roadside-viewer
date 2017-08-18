import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import os
from os import listdir

dir_path = os.path.dirname(os.path.realpath(__file__))
original_images_path = os.path.join(dir_path, 'original')
full_mask_path = os.path.join(dir_path, 'full-masks')

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
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(0,0)
        button.clicked.connect(self.on_click)

        # # Create widget
        label = QLabel(self)
        pixmap = QPixmap(os.path.join(full_mask_path, 'EN20160520L039-26_mask.jpg'))
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
