import cv2

#reading the image
img = cv2.imread('im.png')

#resizing image
img = cv2.resize(img,(1000,1000))

#grayscale
img = cv2.imread('im.png',0)

#thresholding
var,t = cv2.threshold(img, 100, 100, cv2.THRESH_BINARY)

#displaying the image
cv2.imshow('normal',img)
cv2.imshow('threshold',t)
cv2.waitKey()
cv2.destroyAllWindows()
