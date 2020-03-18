import numpy as np 
import cv2 
import matplotlib.pyplot as plt


# print("Getting started")

#### here's how to load images
bkgrn_img = cv2.imread('Day4/Images/b.jpg', 0)
q_img = cv2.imread('Day4/Images/1.jpg', 0)
# this reads in the image as a grayscale image

blur_q = cv2.GaussianBlur(q_img,(5,5),1)
blur_b = cv2.GaussianBlur(bkgrn_img,(5,5),1)

# cast these to floating point values so we can work
# with real numbers
blur_q = blur_q.astype(np.float32)
blur_b = blur_b.astype(np.float32)
# at this point, we want to work with real numbers

# We want to take two images: 1. bkgrnd 2. query image
# we want to take the query image and kill the background

sub_img = blur_q - blur_b

plt.imshow(sub_img, cmap='gray')
plt.show()
