from easygui import *
import sys
from PIL import Image
import numpy as np
import os
from os import listdir
from os.path import isfile, join
from os import walk

dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)

original_images_path = os.path.join(dir_path, 'original')
full_masks_path = os.path.join(dir_path, 'full-masks')

#print(original_images_path)
#print(full_masks_path)

#Print filenames in Original Images folder
f = []
for (dirpath, dirnames, filenames) in walk(original_images_path):
	f.extend(filenames)
for filenames in f:
	print(filenames)

#Display images in easygui
onlyfiles = [ f for f in listdir(original_images_path) if isfile(join(original_images_path, f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
	#images[n] = mpimg.imread( join(orginal_images_path,onlyfiles[n]))
#imgplot = plt.imshow(images[n])
#plt.show()

	image = images[n]

pic = os.path.join(full_masks_path, 'EN20160520L039-26_mask.jpg')
message = "Hello"
reply = buttonbox(message, image=pic)

# # A nice welcome message
# ret_val = msgbox("Hello, World!")
# if ret_val is None: # User closed msgbox
#     sys.exit(0)
#
# image = "new.png"
# msg = "Do you like this picture?"
# choices = ["Yes","No","No opinion"]
# reply = buttonbox(msg, image=image, choices=choices)
