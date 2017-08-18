
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# In[2]:

get_ipython().magic('matplotlib inline')


# In[3]:

img=mpimg.imread('trial pic.jpg')


# In[4]:

imgplot = plt.imshow(img)


# In[5]:

img3 = np.dot(img, img2)


# In[48]:

imgplot = plt.imshow(img3)


# In[49]:

img4 = np.divide(img3, img)


# In[50]:

imgplot = plt.imshow(img4)


# In[7]:

img[200, 10]


# In[52]:

np.amax(img)


# In[53]:

from os import listdir
from os.path import isfile, join
from os import walk


# In[54]:

mypath='/export/mlrg/lmann03/Notebook Tutorials/RoadSide'


# In[55]:

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

for filenames in f:
    print filenames
    break


# In[6]:

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = mpimg.imread( join(mypath,onlyfiles[n]))
  imgplot = plt.imshow(images[n])
  plt.show()
#   print(images[n])


# In[7]:

print(len(images))


# In[8]:

print(images[1])


# In[9]:

img0 = images[0]
im2 = images[2]


# In[10]:

imgplot = plt.imshow(img0)


# In[11]:

some_digit_image = img0.reshape(224, 224)
plt.imshow(some_digit_image, cmap = plt.cm.binary, interpolation="nearest")
plt.axis("off")
plt.show()


# In[ ]:

data:image/png;base64,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

