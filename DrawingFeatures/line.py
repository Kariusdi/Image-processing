import cv2
import numpy as np

def Draw_Line(startX, startY, endX, endY):
    line = np.zeros((100, 100), dtype=np.uint8)

    Setx = []
    Sety = []
    if(startX > endX and startY < endY): # 45deg(/) -> right to left (bottom to top)
        for x in range(startX, endX-1, -1):
            Setx.append(x)
        for y in range(startY, endY+1, 1):
            Sety.append(y)
    elif(startX < endX and startY > endY): # 45deg(/) -> left to right (top to bottom)
        for x in range(startX, endX+1, 1):
            Setx.append(x)
        for y in range(startY, endY-1, -1):
            Sety.append(y)
    elif(startX < endX and startY == endY): # 90deg(|) -> top to bottom
        for x in range(startX, endX+1, 1):
            Setx.append(x)
            Sety.append(startY)
    elif(startX > endX and startY == endY): # 90deg(|) -> bottom to top
        for x in range(startX, endX-1, -1):
            Setx.append(x)
            Sety.append(startY)
    elif(startX == endX and startY < endY): # 180deg(-) -> right to left
        for y in range(startY, endY+1, 1):
            Setx.append(startX)
            Sety.append(y)
    elif(startX == endX and startY > endY): # 180deg(-) -> left to right
        for y in range(startY, endY-1, -1):
            Setx.append(startX)
            Sety.append(y)
    else: # 135deg(\)
        if(startX < endX and startY < endY): # 135deg -> right to left (top to bottom)
            for x in range(startX, endX+1, 1):
                Setx.append(x)
            for y in range(startY, endY+1, 1):
                Sety.append(y)
        else: # 135deg -> left to right (bottom to top)
            for x in range(startX, endX-1, -1):
                Setx.append(x)
            for y in range(startY, endY-1, -1):
                Sety.append(y)

    for x, y in zip(Setx, Sety):
        line[x, y] = 255


    cv.imshow("Line", line)
    # cv.imwrite('Drawing-features\line.png', line)
    cv.imwrite('pics/line.png', line)
    cv.waitKey(2000)
    cv.destroyAllWindows()
    # print(line)
    return line

import numpy as np
import cv2 as cv

def Draw_bresenhamLine(startX, startY, endX, endY):
    line = np.zeros((100, 100), dtype=np.uint8)
    points = []

    # Bresenham's line drawing algorithm
    dx = abs(endX - startX)
    dy = abs(endY - startY)
    sx = 1 if startX < endX else -1
    sy = 1 if startY < endY else -1
    err = dx - dy

    while True:
        points.append((startX, startY))

        if (startX, startY) == (endX, endY):
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            startX += sx
        if e2 < dx:
            err += dx
            startY += sy

    for x, y in points:
        line[x, y] = 255

    cv.imshow("Line", line)
    cv.imwrite('pics/line.png', line)
    cv.waitKey(2000)
    cv.destroyAllWindows()

    return line


if __name__ == '__main__':
    StartEnd_x = [70, 10]
    StartEnd_y = [40, 10]
    line = Draw_Line(StartEnd_x[0], StartEnd_y[0], StartEnd_x[1], StartEnd_y[1])
    line = Draw_bresenhamLine(StartEnd_x[0], StartEnd_y[0], StartEnd_x[1], StartEnd_y[1])