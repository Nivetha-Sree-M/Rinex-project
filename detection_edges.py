import cv2

#reading the image
img = cv2.imread('image.png')

#resizing image
img = cv2.resize(img,(700,700))

#detection of edges
i_edge = cv2.Canny(img, 100, 100)

#displaying the image
cv2.imshow('normal',img)
cv2.imshow('edge',i_edge)
cv2.waitKey()
cv2.destroyAllWindows()
