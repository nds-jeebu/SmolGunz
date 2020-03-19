# from the glob library import 1 method called 'glob'
from glob import glob

# hint part 1
image_dir = '/Users/Muhammad/Desktop/SmolGunz/Day5/Images/'
# this does NOT load in order of number or alphabetic
image_names = glob(image_dir + '*.jpg')

# hint part 2

# for i in range(5):
# 	...


for name in image_names:
	print(name)
#print(image_names)
# import glob
# glob.glob()