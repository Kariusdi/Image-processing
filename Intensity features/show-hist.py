import numpy as np
import cv2 as cv

import matplotlib.pyplot as plt

img = cv.imread('pics/light.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

histogram = cv.calcHist([img_gray], [0], None, [256], [0, 256])

plt.plot(histogram)
plt.show()