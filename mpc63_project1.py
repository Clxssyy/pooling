# Big Data Programming Project 1
# Author: Michael Connolly
import sys
import numpy as np


# @param: .pgm filename
# @return: a tuple (header, image array) # image array - numpy array
def pgmFileRead(fileName):
    img_header = []   # Placeholder 
    img = np.array([])   # Placeholder

    with open(fileName, 'r') as file:
        while img_header[-1:] != ['255']:   # Read until the end of the header
            line = file.readline().strip()
            if not line.startswith('#'):   # Skip any comments
                img_header.append(line)

        width, height = map(int, img_header[1].split())

        pixelValues = []   # Placeholder

        for line in file:
            pixelValues.extend(map(int, line.split()))

        img = np.array(pixelValues).reshape(height, width)

    return img_header, img


# @param: image array; image header; name of the processed image
# return: NaN
def image_save(output_header, image_array, file_name):
    height, width = image_array.shape   # Get the dimensions of the new pooled image

    # Update the header with the correct dimensions (should be the same if using oil painting)
    output_header[1] = f"{width} {height}"

    with open(file_name, 'w') as file:
        file.write('\n'.join(output_header) + '\n')   # Write the header
        for row in image_array:
            file.write(' '.join(map(str, row)) + '\n')   # Write the pixel values


# @param: image array, pool size
# @return: pooled array
def max_pooling(input_array, pool_size):
    height, width = input_array.shape
    pooled_height = height // pool_size
    pooled_width = width // pool_size

    if (height % pool_size != 0):
        pooled_height += 1
    if (width % pool_size != 0):
        pooled_width += 1

    pooled_array = np.zeros((pooled_height, pooled_width), dtype=int)


    for i in range(pooled_height):
        for j in range(pooled_width):
            start_row = i * pool_size
            end_row = min((i + 1) * pool_size, height)
            start_col = j * pool_size
            end_col = min((j + 1) * pool_size, width)
            pooled_array[i, j] = np.max(input_array[start_row:end_row, start_col:end_col])

    return pooled_array


# @param: image array, pool size
# @return: oil painted image array
def oil_painting(input_array, pool_size):
    height, width = input_array.shape
    oil_array = np.zeros((height, width), dtype=int)

    for i in range(height):
        for j in range(width):
            start_row = i
            end_row = min(height, i + pool_size)
            start_col = j
            end_col = min(width, j + pool_size)
            oil_array[i, j] = np.median(input_array[start_row:end_row, start_col:end_col])

    return oil_array


def main():
    imgFileName, poolSize, part = sys.argv[1:]
    poolSize = int(poolSize)
    selectedImg = imgFileName.split('.')[0]

    # Commented out to allow for any image name (for diff.py testing)
    # if selectedImg != 'bug' and selectedImg != 'flower':
    #     print("Invalid image name. Use 'bug.pgm' or 'flower.pgm'.")
    #     return

    # Read the PGM file
    header, img = pgmFileRead(imgFileName)

    if part == '1':
        img = max_pooling(img, poolSize)
        process = 'pooled'
    elif part == '2':
        img = oil_painting(img, poolSize)
        process = 'oil_painted'
    else:
        print("Invalid part number. Use '1' or '2'.")
        return

    # Save the image
    outputFileName = f"{selectedImg}_{process}_{poolSize}.pgm"
    image_save(header, img, outputFileName)


if __name__ == '__main__':
    main()
