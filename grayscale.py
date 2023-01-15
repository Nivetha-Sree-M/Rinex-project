import cv2
img = cv2.imread('image1.jpg')#reading the image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#conversion into grayscale
cv2.imshow('NORMAL IMAGE',img) #displays the original image
cv2.imshow('GRAY SCALE IMAGE',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
