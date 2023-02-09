import cv2 as cv

img = cv.imread('images/4.1.04.tiff',1)

cv.imshow('img1',img)
cv.waitKey(0)
cv.destroyAllWindows('img1')