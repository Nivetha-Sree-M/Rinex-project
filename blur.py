import cv2

#reading image
img = cv2.imread('image1.jpg')

#resizing
img = cv2.resize(img,(300,300))

#bluring of image
blured=cv2.blur(img,(5,5))

#displaying image
cv2.imshow('normal',img)
cv2.imshow('blured',blured)
cv2.waitKey()
cv2.destroAllWindows()
