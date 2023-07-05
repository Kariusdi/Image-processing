import cv2
import numpy as np
from DrawingFeatures import circle

def DrawCircle_WhitePixel(ogImg , filterImg, radius):
    height, width = filterImg.shape[:2]
    for row in range(0, height, 3):
        for col in range(0, width, 3):
            pixel_value = filterImg[row, col]
            if pixel_value == 255:
                print(col, row)
                circle.Draw_bresenhamCircle(ogImg , col, row, radius)

if __name__ == '__main__':              
    img = cv2.imread('pics/CircleObjects.png', 0)

    # Reduce image's noise
    Imgmeanfilter = cv2.medianBlur(img, 15)
    thresh = cv2.threshold(Imgmeanfilter, 175, 255, cv2.THRESH_BINARY)[1]
    Circleedge = cv2.Canny(thresh, 200, 255)

    DrawCircle_WhitePixel(img, Circleedge, 60)

    cv2.imwrite("pics/CircleCenter.png", img)
    cv2.imshow("Filtered", Circleedge)
    cv2.imshow("Result", img)
    cv2.waitKey(0)
