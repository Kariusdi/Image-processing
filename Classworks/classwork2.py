import cv2
import numpy as np
from DrawingFeatures import circle


def check_pixel_values(image, radius):
    height, width = image.shape[:2]
    used_pixels = np.zeros((height, width), dtype=np.uint8)
    for row in range(height):
        for col in range(width):
            pixel_value = image[row, col]
            if pixel_value == 255 and used_pixels[row, col] == 0 :
                print(col, row)
                circle.Draw_bresenhamCircle(image , col, row, radius)
                
                # Set this pixel to be used
                used_pixels[row-radius:row+radius//2, col-radius:col+radius//2] = 255

if __name__ == '__main__':              
    # read image
    img = cv2.imread('pics/CircleObjects.png', 0)

    # Reduce image's noise
    Imgmeanfilter = cv2.medianBlur(img, 5)
    thresh = cv2.threshold(Imgmeanfilter, 175, 255, cv2.THRESH_BINARY)[1]

    # Check white pixel for drawing
    check_pixel_values(thresh, 60)

    # write result to disk
    cv2.imwrite("pics/CircleCenter.png", thresh)
    # display it
    cv2.imshow("IMAGE", img)
    cv2.imshow("THRESH", thresh)
    cv2.waitKey(0)
