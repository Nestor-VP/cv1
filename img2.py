import cv2 as cv

img = cv.imread("images/7.1.03.tiff",1)

cv.imshow("img",img)
key = cv.waitKey(0)

if key== ord('q'):
    cv.destroyWindow('img')
elif key == ord('s'):
    cv.imwrite('images/img1.jpg',img)
    cv.destroyWindow('img')