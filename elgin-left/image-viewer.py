import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QIcon, QPixmap, QScreen
from PIL.ImageQt import ImageQt
from PIL import Image
import os
from os import listdir, walk
from os.path import isfile, join
from resizeimage import resizeimage

class App():
    def __init__(self):

        # sizeObject = QDesktopWidget().screenGeometry()
        # print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))


        self.current_image_index = 0
        print(self.current_image_index)
        QWidget().__init__()
        try:
            self.folder = sys.argv[1]
        except IndexError:
            print('You must specify the full path to a folder.\n')
            sys.exit(1)

        self.original_path = os.path.join(self.folder, 'original')
        self.full_masks_path = os.path.join(self.folder, 'full-masks')

        #Create array of images in 'original' folder
        self.original_images = []
        for (dirpath, dirnames, original_filenames) in walk(self.original_path):
            self.original_images.extend(original_filenames)
        self.sortedoriginal = sorted(self.original_images)
        print(len(self.sortedoriginal))

        #Create array of images in 'full-masks' folder
        self.full_masks_images = []
        for (dirpath, dirnames, mask_filenames) in walk(self.full_masks_path):
            self.full_masks_images.extend(mask_filenames)
        self.sortedmasks = sorted(self.full_masks_images)
        print(len(self.sortedmasks))


        #Full mask window
        self.w2 = QWidget()
        self.b2 = QLabel(self.w2)
        self.current_mask = QPixmap(os.path.join(self.full_masks_path, self.sortedmasks[self.current_image_index]))
        self.maskim = Image.open(os.path.join(self.full_masks_path, self.sortedmasks[self.current_image_index]))
        self.b2.setPixmap(self.current_mask)
        self.w2.setGeometry(1100, 200, 1003, 752)
        self.w2.setWindowTitle("Full mask: " + self.sortedmasks[self.current_image_index])
        self.w2.show()

        #Original image window
        self.w = QWidget()
        self.b = QLabel(self.w)
        self.current_original_image = QPixmap(os.path.join(self.original_path, self.sortedoriginal[self.current_image_index]))
        self.origim = Image.open(os.path.join(self.original_path, self.sortedoriginal[self.current_image_index]))
        self.origimresized = resizeimage.resize_cover(self.origim, [1003, 752])
        self.b.setPixmap(self.current_original_image.scaledToWidth(1003))
        self.w.setGeometry(5, 200, 1003, 752)
        self.w.setWindowTitle("Original image: " + self.sortedoriginal[self.current_image_index])
        self.w.show()

        #Overlayed image window
        self.w3 = QWidget()
        self.b3 = QLabel(self.w3)

        self.overlayed_image = Image.blend(self.origimresized, self.maskim, 0.3)
        self.qim = ImageQt(self.overlayed_image)
        self.pix = QPixmap.fromImage(self.qim)
        self.b3.setPixmap(self.pix)

        self.w3.setGeometry(2195, 200, 1003, 752)
        self.w3.setWindowTitle('Overlayed Image: ' + self.sortedoriginal[self.current_image_index])
        self.w3.show()

        #Next button window
        self.btnwin = QWidget()
        self.btntext = QLabel(self.btnwin)
        self.btntext.setText("The images are in the following order: original image, full mask, overlayed mask.")
        self.btn = QPushButton(self.btnwin)
        self.btn.setText("Next")
        self.btn.clicked.connect(self.handle_btn)
        self.btnwin.setGeometry(700, 1000, 700, 100)
        self.btntext.move(50, 5)
        self.btn.move(300, 40)
        self.btnwin.setWindowTitle('PyQt 4')
        self.btnwin.show()

        self.load_new_image(self.sortedoriginal)

    def load_new_image(self, folder):
        print(folder)


    # def resize_image()


    def handle_btn(self):
        if self.current_image_index + 1 < len(self.sortedoriginal):
            self.current_image_index = self.current_image_index + 1

            #Set new original image
            self.current_original_image = QPixmap(os.path.join(self.original_path, self.sortedoriginal[self.current_image_index]))
            self.origim = Image.open(os.path.join(self.original_path, self.sortedoriginal[self.current_image_index]))
            self.origimresized = resizeimage.resize_cover(self.origim, [1003, 752])
            self.b.setPixmap(self.current_original_image)
            self.b.setPixmap(self.current_original_image.scaledToWidth(1003))
            self.w.setWindowTitle("Original image: " + self.sortedoriginal[self.current_image_index])

            #set new mask image
            self.current_mask = QPixmap(os.path.join(self.full_masks_path, self.sortedmasks[self.current_image_index]))
            self.maskim = Image.open(os.path.join(self.full_masks_path, self.sortedmasks[self.current_image_index]))
            self.b2.setPixmap(self.current_mask)
            self.w2.setWindowTitle("Full mask: " + self.sortedmasks[self.current_image_index])

            #set new overlay image
            self.overlayed_image = Image.blend(self.origimresized, self.maskim, 0.3)
            self.qim = ImageQt(self.overlayed_image)
            self.pix = QPixmap.fromImage(self.qim)
            self.b3.setPixmap(self.pix)
            self.w3.setWindowTitle('Overlayed Image: ' + self.sortedoriginal[self.current_image_index])
            self.w3.show()
        else:
            print("No more images in directory!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
