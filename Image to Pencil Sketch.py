# IMAGE TO PENCIL SKETCH

import cv2

# Enter the image file name that is to be converted into pencil sketch
image_name = input().strip()
image = cv2.imread(image_name)
name,ext = image_name.split('.')
cv2.imshow(name, image)
cv2.waitKey(0)

# Convert the image into gray image format
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_image)
cv2.imshow(name+" Gray", gray_image)
cv2.waitKey(0)

# Convert the gray image format into inverted image format
inverted_image = 255 - gray_image
print(inverted_image)
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
print(blurred)
inverted_blurred = 255 - blurred
print(inverted_blurred)

# Converting the gray image, inverted image into Sketch
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)
cv2.imshow(name+" Original Image", image)
cv2.imshow(name + " Sketch", pencil_sketch)
