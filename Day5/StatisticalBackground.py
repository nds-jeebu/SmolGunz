### import numpy and opencv
import numpy as np 
import cv2 
import matplotlib.pyplot as plt
### 1. read in all of the images into a list
image_dir = '/Users/Edward/Desktop/SmolGunz/Day5/Images/'
image = cv2.imread(image_dir+'1.jpg', 0)

plt.imshow(image,cmap='gray')
plt.show()
### Hint: a list is declared like a = [img1, img2, ...]
### Hint: to add stuff to a list called l use l.append(stuff)

