import cv2 as cv
import numpy as np

img_in = cv.imread('pics/dark.jpg', cv.IMREAD_GRAYSCALE)

gamma = 0.5 #if it's dark decrease gamma, but is it's bright increase gamma
gamma_corrected = (img_in / 255)**gamma

gamma_corrected = gamma_corrected * 255

img_out = np.array(gamma_corrected, dtype = 'uint8')

cv.imshow('Power-law', img_out)

cv.imwrite('output-pics/demoIn.png', img_in)
cv.imwrite('output-pics/demoOut.png', img_out)