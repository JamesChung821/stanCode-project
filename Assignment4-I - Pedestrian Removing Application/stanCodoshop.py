"""
Assignment4 - I
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

YOUR DESCRIPTION HERE
This program is designed to remove the image which user would not like.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    red_avg = red
    green_avg = green
    blue_avg = blue
    color_distance = math.sqrt((red_avg - pixel.red)*(red_avg - pixel.red) +
                               (green_avg - pixel.green)*(green_avg - pixel.green) +
                               (blue_avg - pixel.blue)*(blue_avg - pixel.blue))
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0
    for i in range(len(pixels)):
        # Sum all RGB pixels
        total_red += pixels[i].red
        total_green += pixels[i].green
        total_blue += pixels[i].blue
    return [int(total_red/len(pixels)), int(total_green/len(pixels)), int(total_blue/len(pixels))]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb_avg = get_average(pixels)
    note = 0
    # Set the first distance to be compared
    minimum = get_pixel_dist(pixels[0], rgb_avg[0], rgb_avg[1], rgb_avg[2])
    for i in range(len(pixels)):
        distance = get_pixel_dist(pixels[i], rgb_avg[0], rgb_avg[1], rgb_avg[2])
        if distance <= minimum:
            minimum = distance
            # Record the shortest distance
            note = i
    return pixels[note]


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
    # Set an empty list
    pixel_list = []
    for j in range (result.height):
        for i in range (result.width):
            # The number of images
            for n in range(len(images)):
                # Create a pixel list including the same pixel position of each image
                pixel_list += [images[n].get_pixel(i, j)]
            # Select the best pixel
            best_pixel = get_best_pixel(pixel_list)
            # Set new pixel coordination
            result_pixel = result.get_pixel(i, j)
            # Change pixel
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
            # You should empty the list!
            pixel_list = []
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # Milestone 1
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))
    # Milestone 2
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    # Milestone 3
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)
    ######## YOUR CODE ENDS HERE ###########
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
    for filename in os.listdir(dir): # a directory ?
        if filename.endswith('.jpg'): # file ending type
            filenames.append(os.path.join(dir, filename))
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
