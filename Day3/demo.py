### chunk 1 : importing all library 
import numpy as np
import cv2

### chunk 2 : all functions (shit we make)
def add(x, y):
	return x + y

def print_add(x, y):
	print(x + y)
	# this don't return nothing!!!!

def multiply(x,y):
	c = x * y
	return(c)
	#return None
	# no return


### chunk 3 : main body


print('hi edward!') # this is function

# object
# method

#cow.makenoise()

print([1,2,3,4]) # printing list <-- built in to python
vector = np.array([1,2,3,4]) # an example of a method

print(np.linalg.norm(vector)) # this is a method!!

print_add(3,5)

print(add(1, 2))

print(multiply(2,3))