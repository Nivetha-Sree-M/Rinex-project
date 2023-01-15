import numpy as np
import cv2 as cv

#read image from source
img = cv.imread('image.png',0)
img = cv.medianBlur(img,5)

#grayscale
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
#gradient method
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    
 # draw the outer circle((image, center_coordinates, color, thickness))
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    
# draw the center of the circle
#((image, center_coordinates, radius, color, thickness))
    
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
#displaying image
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()
