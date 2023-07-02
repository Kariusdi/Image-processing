import cv2
import numpy as np

def drawingSolidCircle(h, k, radius):

    circle = np.zeros((400, 400), dtype=np.uint8)

    for y in range(0, 400):
        for x in range(0, 400):

            line_lenght = (x - h)**2 + (y - k)**2
            
            if line_lenght <= (radius**2):
                circle[y, x] = 255

    cv2.imshow("Circle", circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
a = int(input("Please enter a point of center(x) : "))
b = int(input("Please enter a point of center(y) : "))
r = int(input("Please enter radius : "))
drawingSolidCircle(a, b, r)
