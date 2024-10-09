# MINIPROJECT 2 (CREATING CHECKERBOARD USING OPEN CV)

import cv2  # Import the OpenCV library for image processing
import numpy as np  # Import NumPy for numerical operations

# Create a black image of size 400x400 pixels with 3 color channels (RGB)
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Loop through the rows of the image with a step size of 100 pixels
for i in range(0, 400, 100):
    # Loop through the columns of the image with a step size of 100 pixels
    for j in range(0, 400, 100):
        # Fill a square (50x50 pixels) at the position (i, j) with white color (255, 255, 255)
        img[i:i + 50, j:j + 50] = 255, 255, 255

# Loop through the rows of the image with a step size of 100 pixels
for i in range(0, 400, 100):
    # Loop through the columns of the image with a step size of 100 pixels
    for j in range(0, 400, 100):
        # Fill the adjacent square (50x50 pixels) at the position (i + 50, j + 50) with white color
        img[i + 50:i + 100, j + 50:j + 100] = 255, 255, 255

# Save the image to a file
cv2.imwrite('checkerboard_output.png', img)  # Save the output image

# Optionally, display the image in a window
cv2.imshow('Checkerboard', img)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()






