import numpy as np
import cv2 as cv

img = cv.imread('pics/light.jpg', cv.IMREAD_GRAYSCALE)

img_out = cv.equalizeHist(img)

cv.imwrite('output-pics/HistEQ_Before.png', img)
cv.imwrite('output-pics/HistEQ_After.png', img_out)