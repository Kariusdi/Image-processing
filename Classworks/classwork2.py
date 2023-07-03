import cv2
import numpy as np
from DrawingFeatures import circle

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

if __name__ == '__main__':
    # Create a blank image
    image_size = (400, 400)
    image = cv2.imread('pics/CircleObjects.png', 0)
    # image = np.zeros((image_size[0], image_size[1], 3), dtype=np.uint8)

    # Set the parameters for the circle
    center = (image_size[1] // 2, image_size[0] // 2)
    radius = 100
    color = 255  # Green color in BGR format

    # Get the eight main points on the circle
    circle_points = get_circle_points(center[0], center[1], radius)

    # image = circle.Draw_bresenhamCircle(center[0], center[1], radius)

    # Draw the points on the image
    for point in circle_points:
        x = int(point[0])
        y = int(point[1])
        cen = (x, y)
        cv2.circle(image, cen, 100, color, 1)

    # Display the image
    cv2.imshow("Circle Points", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()