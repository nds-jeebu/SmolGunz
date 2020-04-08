# from the glob library import 1 method called 'glob'
from glob import glob
import numpy as np 
import cv2 
import matplotlib.pyplot as plt
# hint part 1
image_dir = '/Users/Edward/Desktop/SmolGunz/Day5/Images/'
# this does NOT load in order of number or alphabetic
image_names = glob(image_dir + '*.jpg')

# hint part 2

# for i in range(5):
# 	...
for i in image_names:
	print(i)
	img = cv2.imread(i,0)
	plt.imshow(img,cmap='gray')
	plt.show()


for name in image_names:
	print(name)
#print(image_names)
# import glob
# glob.glob()