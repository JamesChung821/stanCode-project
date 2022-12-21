"""
File: fire.py
Name: James Chung
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage

# This constant is to help distinguish the fire disaster.
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file image location
    :return: SimpleImage, the gray image with fire mark noted by red dots
    """
    # Open the file
    fire_disaster = SimpleImage(filename)
    for pixel in fire_disaster:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        # Mark the fire place
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        # Plot grayscale in safe place
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return fire_disaster


def main():
    """
    This program detects the fire disaster in the forest.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
