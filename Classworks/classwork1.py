import cv2 as cv
import numpy as np
from DrawingFeatures import line as Aline

def motionblur(line):

    kernel_size = 15000
    image = cv.imread('pics/meandyou.jpg', 0)
    kernel = np.zeros((kernel_size, kernel_size))
    kernel = line
    kernel = kernel / kernel_size

    motion_blur = cv.filter2D(image, -1, kernel)

    cv.imshow('Original Image', image)
    cv.imshow('Motion Blurred Image', motion_blur)
    cv.waitKey(5000)
    cv.destroyAllWindows()



if __name__ == '__main__':
    StartEnd_x = [70, 20]
    StartEnd_y = [10, 10]
    line = Aline.Draw_Line(StartEnd_x[0], StartEnd_y[0], StartEnd_x[1], StartEnd_y[1])
    # line = Draw_bresenhamLine(StartEnd_x[0], StartEnd_y[0], StartEnd_x[1], StartEnd_y[1])
    motionblur(line)