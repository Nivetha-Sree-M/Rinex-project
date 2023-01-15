import numpy as np
import cv2 as cv

#reading image from source
input_image = cv.imread('b.jpg')
blue, green, red = cv.split(input_image)

#black background and splitting of image to different color channel
blue_channel = np.zeros(input_image.shape, input_image.dtype)
green_channel = np.zeros(input_image.shape, input_image.dtype)
red_channel = np.zeros(input_image.shape, input_image.dtype)

#matching each color channel to a 3D dimension:
    
cv.mixChannels([blue, green, red], [blue_channel], [0,0]) #Blue
cv.mixChannels([blue, green, red], [green_channel], [1,1]) #green
cv.mixChannels([blue, green, red], [red_channel], [2,2]) #red

# Displaying the three obtained images
cv.imshow('Blue Channel', blue_channel)
cv.imshow('Green Channel', green_channel)
cv.imshow('Red Channel', red_channel)

cv.waitKey(0)
cv.destroyAllWindows()
