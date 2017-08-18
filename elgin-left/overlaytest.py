from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage
import sys
from resizeimage import resizeimage

def PILimageToQImage(pilimage):
    """converts a PIL image to QImage, by Sebastian Stetter"""
    imageq = ImageQt(pilimage) #convert PIL image to a PIL.ImageQt object
    qimage = QImage(imageq) #cast PIL.ImageQt object to QImage object -that´s the trick!!!
    return qimage

if __name__ == "__main__":
    #Testcode
    app = QApplication(sys.argv)

    image = Image.open('/export/mlrg/lmann03/Desktop/scrnshot.png')
    print(image.size)

#     background = Image.open('EN20160520L039-26_mask.jpg')
#     overlay = Image.open('EN20160520L039-45_mask.jpg')
#
#     new_image = Image.blend(background, overlay, 0.3)
# # new_image.show()
#
#     quim = ImageQt(new_image)
#     pix = QPixmap.fromImage(quim)
#     lbl = QLabel()
#     lbl.setPixmap(pix)
#     lbl.show()

    sys.exit(app.exec_())
