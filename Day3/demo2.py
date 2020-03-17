import numpy as np

def norm(list_1):
	return np.linalg.norm(list_1)

a = [3,4]
print('result 1:', norm(a))
print('result 2:', np.linalg.norm(a))


#####################################
#####################################
# control flow

# 1. loops <- allow u to do the same stuff over and over
# 2. logic <- allows u to specify when to run a line of code

def divide(x, y):
	if not(y == 0):
		c = x/y
	else:
		c = -1
	return c

def multiply(x, y):
	c = x*y
	return c
# write this without using *, use a for loop
# assuming y is a whole number > 0
def hardcore_multiply(x, y):
	c = 0
	print('c when we start:', c)
	for i in range(y):
		c = c + x
		print('c during iteration', i + 1, ':', c)
	return c

##########################################
#print(divide(1,2))
#print(divide(1, 0))
#print(multiply(3,6))
#print(hardcore_multiply(3,6))
#hardcore_multiply(3,6)

# number_of_times_to_loop = 10 # pyhton starts at 0!!
# for i in range(number_of_times_to_loop):
# 	print(i)

# modular arithmatic 
# a = 8 % 2
# a = 9 % 2
# a = 8 % 3
# print(a)
# problem: print all even numbers up to 100
for i in range(101):
	c = i % 2
	if c == 0:
		print(i)
	# when should i print i
	# things of the form 2k are even things 2k+1 are odd
	# divisible by 2!!! turns out there is a operation for that


