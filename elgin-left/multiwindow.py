import sys
#from PyQt4 import QtGui
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import os


def fun(window):
    window.b2.setPixmap(QPixmap('image2.jpg'))

def window():
   app = QtWidgets.QApplication(sys.argv)

   #Create first window
   w = QtWidgets.QWidget()
   b = QtWidgets.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(5, 200, 1003, 752)
   w.setWindowTitle('PyQt')
   w.show()

   #Create second window
   w2 = QtWidgets.QWidget()
   b2 = QtWidgets.QLabel(w2)
   pixmap = QPixmap('image1.jpg')
   b2.setPixmap(pixmap)
   w2.setGeometry(1100, 200, 1003, 752)
   w2. setWindowTitle('PyQt 2!')
   w2.show()

   #Create third window
   w3 = QtWidgets.QWidget()
   b3 = QtWidgets.QLabel(w3)
   b3.setText("Hello Third Window!")
   w3.setGeometry(2195, 200, 1003, 752)
   w3.setWindowTitle('PyQt 3!')
   w3.show()

   #Create bottom bar for button
   w4 = QtWidgets.QWidget()
   b4 = QtWidgets.QPushButton(w4)
   c4 = QtWidgets.QLabel(w4)
   c4.setText("The images are in the following order: original image, full mask, overlayed mask.")
   b4.setText("Next")
   b4.clicked.connect(fun)
   # c4.setWordWrap(True)
   w4.setGeometry(300, 900, 700, 100)
   c4. move(50, 5)
   b4.move(300, 40)
   w4.setWindowTitle('PyQt 4!')
   w4.show()

   sys.exit(app.exec_())


if __name__ == '__main__':
   window()
