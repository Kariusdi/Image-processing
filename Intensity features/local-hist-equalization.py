import cv2 as cv
import numpy as np

# Load the image
og_image = cv.imread('pics/demo.png', cv.IMREAD_COLOR)

# Define the block size and stride length
block_size = (320, 320)  # Size of each block
stride = (160, 160)  # Stride length for overlapping blocks

# Convert the image to a NumPy array
image_array = np.array(og_image)

# Calculate the number of blocks in each dimension
blocks_per_row = (image_array.shape[1] - block_size[1]) // stride[1] + 1
blocks_per_col = (image_array.shape[0] - block_size[0]) // stride[0] + 1

# Create an empty list to store the blocks
blocks = []
count = 0
# Iterate over the image and extract blocks
for row in range(blocks_per_col):
    for col in range(blocks_per_row):
        block = image_array[row * stride[0]:row * stride[0] + block_size[0],
                           col * stride[1]:col * stride[1] + block_size[1]]
        blocks.append(block)
        # Save the block as a separate image
        cv.imwrite(f'dividepics/input/Inblock{count}.jpg', block)
        count += 1



for img in range(len(blocks)):
    imgblock_in = cv.imread('dividepics/input/Inblock{}.jpg'.format(img), 0)
    mean = np.mean(imgblock_in) / 125
    print(mean)
    gamma = 1

    if (mean < gamma):
        gamma = 2
    else:
        gamma = 0.5

    print(gamma)

    gamma_corrected = (imgblock_in / 255)**gamma

    gamma_corrected = gamma_corrected * 255

    imgblock_out = np.array(gamma_corrected, dtype = 'uint8')

    # cv.imshow('Power-law', imgblock_out)
    # cv.imwrite('dividepics/input/Inblock{}.jpg'.format(img), imgblock_in)
    cv.imwrite('dividepics/output/Outblock{}.jpg'.format(img), imgblock_out)

# Create an empty canvas to assemble the output image
canvas_height = (blocks_per_col - 1) * stride[0] + block_size[0]
canvas_width = (blocks_per_row - 1) * stride[1] + block_size[1]
assembled_image = np.zeros((canvas_height, canvas_width), dtype=np.uint8)

# Assemble the output image from the overlapping blocks
for idx, block in enumerate(blocks):
    imgblock_out = cv.imread('dividepics/output/Outblock{}.jpg'.format(idx), cv.IMREAD_GRAYSCALE)
    row = idx // blocks_per_row
    col = idx % blocks_per_row
    start_row = row * stride[0]
    end_row = start_row + block_size[0]
    start_col = col * stride[1]
    end_col = start_col + block_size[1]
    assembled_image[start_row:end_row, start_col:end_col] = imgblock_out

# Save the assembled image
cv.imwrite('dividepics/output/assembled_image.jpg', assembled_image)



