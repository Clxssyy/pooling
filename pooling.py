# Big Data Programming Project 1
# Author: your name
import sys
import numpy as np


# @param: .pgm filename
# @return: a tuple (header, image array) # image array - numpy array
def pgmFileRead(fileName):
    img_header = []   # a place holder
    img = np.array([])   # a place holder

    return img_header, img


# @param: image array; image header; name of the processed image
# return: NaN
def image_save(output_header, image_array, fileName):
    return None


# @param: image array, pool size
# @return: pooled array
def max_pooling(input_array, pool_size):
    pooled_array = np.array([])   # a place holder

    return pooled_array


# @param: image array, pool size
# @return: oil painted image array
def oil_painting(input_array, pool_size):
    oil_array = np.array([])  # a place holder

    return oil_array


def main():
    imgFileName, poolSize, part = sys.argv[1:]


if __name__ == '__main__':
    main()
