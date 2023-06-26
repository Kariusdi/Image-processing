import cv2 as cv
import numpy as np

image = cv.imread('pics/me.jpg', cv.IMREAD_GRAYSCALE)

c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(1 + image))

log_image = np.array(log_image, dtype = 'uint8')

cv.imwrite('output-pics/log-out.png', log_image)