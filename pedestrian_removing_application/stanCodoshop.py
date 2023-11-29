"""
File: stanCodoshop.py
Name: 許景涵
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # pixel_red, pixel_green, pixel_blue = pixel.red, pixel.green, pixel.blue

    # Use this formula to calculate the color distance of a pixel from the avg_point
    dist = math.sqrt((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # Initialize variables to calculate the sum of RGB
    # sum_red, sum_green, sum_blue = 0, 0, 0
    # 助教優化寫法，在講義P.51
    sum_red = sum(pixel.red for pixel in pixels)
    sum_green = sum(pixel.green for pixel in pixels)
    sum_blue = sum(pixel.blue for pixel in pixels)

    # Iterate through each pixel in the list
    # for pixel in pixels:
    #    sum_red += pixel.red
    #    sum_green += pixel.green
    #    sum_blue += pixel.blue

    # Calculate the average RGB values
    num_pixels = len(pixels)
    # red_avg = sum_red // num_pixels
    # green_avg = sum_green // num_pixels
    # blue_avg = sum_blue // num_pixels

    # Return the average RGB values as a list
    # return [red_avg, green_avg, blue_avg]
    return [sum_red // num_pixels, sum_green // num_pixels, sum_blue // num_pixels]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # Get the average RGB values by the get_average function
    rgb_avg = get_average(pixels)
    red_avg, green_avg, blue_avg = rgb_avg

    # Initialize variables to keep track of the best pixel and the smallest distance
    # best_pixel = None
    # best_distance = float('inf')  # 無窮大的浮點數
    dist_list = []

    # Iterate through each pixel in the list
    for pixel in pixels:
        # Calculate the color distance by the get_pixel_dist function
        distance = get_pixel_dist(pixel, red_avg, green_avg, blue_avg)
        dist_list.append((distance, pixel))

        # Update the best pixel if the current pixel has a smaller distance
        # if distance < best_distance:
        #    best_pixel = pixel
        #    best_distance = distance
    # return best_pixel
    return min(dist_list, key=lambda t: t[0])[1]  # 鎖定 0 號位置 distance，比較 distance 的大小，返回 distance 最小的 pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    # Iterate through each position (x, y) in the images
    for x in range(width):
        for y in range(height):
            # Get the pixels (x, y) from all images
            pixels_position = [image.get_pixel(x, y) for image in images]

            # Use the get_best_pixel function to get the best pixel for the current position
            best_pixel = get_best_pixel(pixels_position)

            # Set the best pixel (x, y) on the result image
            result.set_pixel(x, y, best_pixel)
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):  # os.listdir: 列出所有資料夾但無順序性
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))  # dir/filename 用 / join兩者，變成路徑
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
