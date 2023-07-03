import numpy as np
import cv2 as cv

img = np.zeros([200, 300], dtype = np.uint8)

for y in range(50,100):
    for x in range(50,100):
        img[y,x] = 255

cv.imshow('Drawing', img)

cv.waitKey(0)

cv.destroyAllWindows()