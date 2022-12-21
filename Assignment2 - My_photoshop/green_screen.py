"""
File: green_screen.py
Name: James Chung
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the figure image
    :return: SimpleImage, the image synthesis
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            # Mark every pixel
            pixel_me = figure_img.get_pixel(x, y)
            pixel_bg = background_img.get_pixel(x, y)
            # Set a threshold
            bigger = max(pixel_me.red, pixel_me.blue)
            # Set a condition
            if pixel_me.green > bigger*2:
                # Replace the green background
                pixel_me.red = pixel_bg.red
                pixel_me.green = pixel_bg.green
                pixel_me.blue = pixel_bg.blue
    return figure_img


def main():
    """
    This program combines a background and a figure picture together
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    space_ship.show()
    figure.show()
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
