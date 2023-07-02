import cv2
import numpy as np

def bresenhamLine(x1, y1, x2, y2):
    line = np.zeros((500, 500), dtype=np.uint8)
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)
 
    y = y1
    for x in range(x1, x2+1):
 
        print("(", x, ",", y, ")\n")
        line[x, y] = 255
 
        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new
 
        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y+1
            slope_error_new = slope_error_new - 2 * (x2 - x1)
            

    cv2.imshow("Line", line)
    cv2.imwrite('pics/line.png', line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Line45deg(startX, startY, endX, endY):
    line = np.zeros((500, 500), dtype=np.uint8)

    Setx = []
    Sety = []
    if(startX > endX and startY < endY):
        for x in range(startX, endX-1, -1):
            Setx.append(x)
        for y in range(startY, endY+1, 1):
            Sety.append(y)
    elif(startX < endX and startY > endY):
        for x in range(startX, endX+1, 1):
            Setx.append(x)
        for y in range(startY, endY-1, -1):
            Sety.append(y)
    else:
        if(startX < endX and startY < endY):
            for x in range(startX, endX+1, 1):
                Setx.append(x)
            for y in range(startY, endY+1, 1):
                Sety.append(y)
        else:
            for x in range(startX, endX-1, -1):
                Setx.append(x)
            for y in range(startY, endY-1, -1):
                Sety.append(y)

    for x, y in zip(Setx, Sety):
        line[x, y] = 255


    cv2.imshow("Line", line)
    # cv2.imwrite('Drawing-features\line.png', line)
    cv2.imwrite('pics/line.png', line)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    x = [100, 460]
    y = [370, 150]
    # bresenhamLine(x[0], y[0], x[1], y[1])
    Line45deg(x[0], y[0], x[1], y[1])