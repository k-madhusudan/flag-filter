from skimage import data
import skimage
import os
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import img_as_float
from skimage import color
# Saffron : 255, 153, 51
#cam = data.camera()
#print type(cam)
#print cam.shape
#filename = os.path.join("/home/madhusudan/Programming/Python-For-Life/independence-day-filter","lena.png")
filename = os.path.join (input(),input())
lena = io.imread(filename)

#rgblena = rgb2gray(lena)
lenaimg = img_as_float(lena)

yello_mult = [1,1,0]
red_mult = [1,0,0]
#green_mult = [19.0/255,100.0/255,8.0/255]
lenacolor= color.gray2rgb(lenaimg)
#io.imshow(lena,plugin=None)

lenacolor[0: lenacolor.shape[0]/2] = lenacolor[0: lenacolor.shape[0]/2] * yello_mult
lenacolor[(lenacolor.shape[0]/2)*1: (lenacolor.shape[0]/2)*2] = lenacolor[(lenacolor.shape[0]/2)*1: (lenacolor.shape[0]/2)*2] * red_mult
#lenacolor[(lenacolor.shape[0]/3)*2: (lenacolor.shape[0]/3)*3] = lenacolor[(lenacolor.shape[0]/3)*2: (lenacolor.shape[0]/3)*3] * green_mult

io.imshow(lenacolor, plugin=None)
io.show()
#print rgblena.min(), rgblena.max()
#plt.imshow(lena)
#plt.show()