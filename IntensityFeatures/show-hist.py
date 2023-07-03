import numpy as np
import cv2 as cv

import matplotlib.pyplot as plt

img = cv.imread('pics/dark.jpg', cv.IMREAD_GRAYSCALE)

# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_out = cv.equalizeHist(img)

histogram = cv.calcHist([img_out], [0], None, [256], [0, 256])

plt.plot(histogram)
plt.show()