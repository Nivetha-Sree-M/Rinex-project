import cv2

#reading the image
img = cv2.imread('im.png')

#resizing image
img = cv2.resize(img,(700,700))

#rotating the image upside-down
rotate = cv2.flip(img,0)

#displaying the image
cv2.imshow('normal',img)
cv2.imshow('rotated',rotate)
cv2.waitKey()
cv2.destroyAllWindows()
