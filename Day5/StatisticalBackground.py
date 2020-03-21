### import numpy and opencv
import numpy as np 
import cv2 
import matplotlib.pyplot as plt
### 1. read in all of the images into a list
image_dir = '/Users/Edward/Desktop/SmolGunz/Day5/Images/'
image = cv2.imread(image_dir+'1.jpg', 0)




### Hint: a list is declared like a = [img1, img2, ...]

a=[image_dir+'1.jpg',image_dir+'2.jpg',image_dir+'3.jpg',image_dir+'4.jpg',image_dir+'5.jpg',image_dir+'6.jpg',image_dir+'7.jpg',image_dir+'8.jpg',image_dir+'9.jpg',image_dir+'10.jpg',image_dir+'11.jpg']

for i in a
	plt.imshow(image,cmap='gray')
	plt.show()

### Hint: to add stuff to a list called l use l.append(stuff)

