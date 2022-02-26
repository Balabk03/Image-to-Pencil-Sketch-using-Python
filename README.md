# Image-to-Pencil-Sketch-using-Python
In Python, an image is just a two-dimensional array of integers. So one can do a couple of matrix manipulations using various python modules in order to get some very interesting effects. In order to convert the normal image to a sketch, we will change its original RGB values and assign its RGB values similar to grey, in this way a sketch of the input image will be generated. 

The program converts the image into a pencil sketch.
Steps for the conversion:
		The main library used is *cv2*
		Then we will import cv2 inside our code, after that, we will use some of the following functions: 
				1. imread()- This function will load the image i.e in the specified folder. 
				2. cvtColor()- This function takes color as an argument and then changes the source image color into that color.
				3. GaussianBlur()- This function is used to modify the image by sharpening the edges of the image, smoothen the image, and will minimize the blurring property.
		Finally the converted image is shown using imshow() function.
