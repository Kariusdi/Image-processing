import cv2
import numpy as np
import math

def Draw_SolidCircle(inputimg, h, k, radius):

    image = inputimg

    for y in range(0, 400):
        for x in range(0, 400):

            line_lenght = (x - h)**2 + (y - k)**2
            
            if line_lenght <= (radius**2):
                image[y, x] = 255

    return image

def get_circle_points(x, y, r):
    points = []
    
    points.append((x, y + r))
    points.append((x, y - r))
    points.append((x + r, y))
    points.append((x - r, y))
    
    diagonal_distance = r / np.sqrt(2)
    points.append((x + diagonal_distance, y + diagonal_distance))
    points.append((x - diagonal_distance, y + diagonal_distance))
    points.append((x + diagonal_distance, y - diagonal_distance))
    points.append((x - diagonal_distance, y - diagonal_distance))
    
    return points

def Draw_bresenhamCircle(inputimg, h, k, r):

    image = inputimg
    # Set the center and radius of the circle
    center = (h, k)
    radius = r
    # Set the color of the circle
    color = 175
    
    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:
        # Bresenham's circle drawing algorithm
        # Plot circle points in all octants
        image[center[1] + y, center[0] + x] = color
        image[center[1] + x, center[0] + y] = color
        image[center[1] - x, center[0] + y] = color
        image[center[1] - y, center[0] + x] = color
        image[center[1] - y, center[0] - x] = color
        image[center[1] - x, center[0] - y] = color
        image[center[1] + x, center[0] - y] = color
        image[center[1] + y, center[0] - x] = color

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y = y - 1

        x = x + 1

    return image


if __name__ == '__main__':    
    a = int(input("Please enter a point of center(x) : "))
    b = int(input("Please enter a point of center(y) : "))
    r = int(input("Please enter radius : "))
    image = np.zeros((400, 400, 3), dtype=np.uint8)
    Draw_bresenhamCircle(image, a, b, r)
