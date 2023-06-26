import cv2 as cv
import numpy as np

def pixelVal(pix, r1, s1, r2, s2):
    if(0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif(r1 < pix and pix <= r2):
        return ((s2-s1)/(r2-r1)) * (pix - r1) + s1
    else:
        return ((255-s2)/(255-r2)) * (pix-r2) + s2
    

img = cv.imread('pics/me.jpg')
r1 = 70
s1 = 0
r2 = 140
s2 = 255

pixelVal_vec = np.vectorize(pixelVal)
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

img_out = np.array(contrast_stretched, dtype = 'uint8')

cv.imwrite('output-pics/contrast-demo.png', img_out)