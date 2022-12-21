"""
File: mirror_lake.py
Name: James Chung
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file image location.
    :return: SimpleImage, the original image with it's mirror image.
    """
    # Open the file
    lake = SimpleImage(filename)
    # Create a new blank
    double = SimpleImage.blank(lake.width, lake.height*2)
    for y in range(lake.height):
        for x in range(lake.width):
            # Mark every pixel
            pixel = lake.get_pixel(x,y)
            # Define upper pixel
            new_upper_pixel = double.get_pixel(x, y)
            # Define below pixel 4-1-y(0) == 3
            new_below_pixel = double.get_pixel(x, double.height-1-y)
            # Replace the pixel
            new_upper_pixel.red = pixel.red
            new_upper_pixel.green = pixel.green
            new_upper_pixel.blue = pixel.blue
            new_below_pixel.red = pixel.red
            new_below_pixel.green = pixel.green
            new_below_pixel.blue = pixel.blue
    return double


def main():
    """
    This programs is to mirror image vertically.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
