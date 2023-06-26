import numpy as np
import cv2 as cv

imgA = cv.imread('pics/meandyou.jpg', cv.IMREAD_GRAYSCALE)
imgB = cv.imread('pics/me.jpg', cv.IMREAD_GRAYSCALE)

histB = cv.calcHist([imgB], [0], None, [256], [0, 256])

imgAtoB = cv.equalizeHist(imgA, histB)

cv.imwrite('output-pics/imgA.png', imgA)
cv.imwrite('output-pics/imgB.png', imgB)
cv.imwrite('output-pics/imgAtoB.png', imgAtoB)