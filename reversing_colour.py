import cv2

#reading the image
img = cv2.imread('im.png')

#resizing image
img = cv2.resize(img,(700,700))

#reversing the color of the images
i_img =cv2.bitwise_not(img)

#displaying the image
cv2.imshow('normal',img)
cv2.imshow('inverted',i_img)
cv2.waitKey()
cv2.destroyAllWindows()

