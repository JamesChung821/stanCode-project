"""
File: shrink.py
Name: James Chung
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file location of original image
    :return img: SimpleImage, the small image
    """
    img = SimpleImage(filename)
    # Create a half blank window
    shrink = SimpleImage.blank(img.width//2, img.height//2)
    # Shrink 4 pixels in original image to 1 pixel in small image
    # Compress the selection range
    for y in range(img.height//2):
        for x in range(img.width//2):
            # The pixel at the upper left site and Select 4 pixels in original image each time
            pixel = img.get_pixel(x*2, y*2)
            # Print 1 pixel each time in small image
            shrink_pixel = shrink.get_pixel(x, y)
            # The other 3 pixels coordination
            pixel_10 = img.get_pixel(x*2+1, y*2)
            pixel_01 = img.get_pixel(x*2, y*2+1)
            pixel_11 = img.get_pixel(x*2+1, y*2+1)
            # Average the RGB, which can retain the original information
            shrink_pixel.red = (pixel.red + pixel_10.red + pixel_01.red + pixel_11.red) / 4
            shrink_pixel.green = (pixel.green + pixel_10.green + pixel_01.green + pixel_11.green) / 4
            shrink_pixel.blue = (pixel.blue + pixel_10.blue + pixel_01.blue + pixel_11.blue) / 4
    return shrink


def main():
    """
    This program shrinks the image to a half of it
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
