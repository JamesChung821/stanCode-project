"""
File: blur.py
Name: James Chung
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred image
    """
    # Create a new blank
    blur_img = SimpleImage.blank(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):
            # Mark every pixel
            pixel = img.get_pixel(x, y)
            # The centre coordination of the pixel which you would like to blur
            blur_pixel = blur_img.get_pixel(x, y)
            # Other 8 pixel coordination
            # pixel_10 = img.get_pixel(x-1, y-1)
            # pixel_20 = img.get_pixel(x, y-1)
            # pixel_30 = img.get_pixel(x+1, y-1)
            # pixel_11 = img.get_pixel(x-1, y)
            # pixel_31 = img.get_pixel(x+1, y)
            # pixel_12 = img.get_pixel(x-1, y+1)
            # pixel_22 = img.get_pixel(x, y+1)
            # pixel_32 = img.get_pixel(x+1, y+1)
            # The left edge condition of the image
            if x == 0 and y != 0 and y != img.height-1:
                pixel_20 = img.get_pixel(x, y - 1)
                pixel_30 = img.get_pixel(x + 1, y - 1)
                pixel_31 = img.get_pixel(x + 1, y)
                pixel_22 = img.get_pixel(x, y + 1)
                pixel_32 = img.get_pixel(x + 1, y + 1)
                blur_pixel.red = (pixel_20.red + pixel_30.red + pixel.red +
                             pixel_31.red + pixel_22.red + pixel_32.red) // 6
                blur_pixel.green = (pixel_20.green + pixel_30.green + pixel.green +
                               pixel_31.green + pixel_22.green + pixel_32.green) // 6
                blur_pixel.blue = (pixel_20.blue + pixel_30.blue + pixel.blue +
                              pixel_31.blue + pixel_22.blue + pixel_32.blue) // 6
            # The upper edge condition of the image
            elif y == 0 and x != 0 and x != img.width-1:
                pixel_11 = img.get_pixel(x - 1, y)
                pixel_31 = img.get_pixel(x + 1, y)
                pixel_12 = img.get_pixel(x - 1, y + 1)
                pixel_22 = img.get_pixel(x, y + 1)
                pixel_32 = img.get_pixel(x + 1, y + 1)
                blur_pixel.red = (pixel_11.red + pixel.red +
                             pixel_31.red + pixel_12.red + pixel_22.red + pixel_32.red) // 6
                blur_pixel.green = (pixel_11.green + pixel.green +
                               pixel_31.green + pixel_12.green + pixel_22.green + pixel_32.green) // 6
                blur_pixel.blue = (pixel_11.blue + pixel.blue +
                              pixel_31.blue + pixel_12.blue + pixel_22.blue + pixel_32.blue) // 6
            # The right edge condition of the image
            elif x == img.width-1 and y != 0 and y != img.height-1:
                pixel_10 = img.get_pixel(x - 1, y - 1)
                pixel_20 = img.get_pixel(x, y - 1)
                pixel_11 = img.get_pixel(x - 1, y)
                pixel_12 = img.get_pixel(x - 1, y + 1)
                pixel_22 = img.get_pixel(x, y + 1)
                blur_pixel.red = (pixel_10.red + pixel_20.red+ pixel_11.red + pixel.red +
                             pixel_12.red + pixel_22.red) // 6
                blur_pixel.green = (pixel_10.green + pixel_20.green + pixel_11.green + pixel.green +
                               pixel_12.green + pixel_22.green) // 6
                blur_pixel.blue = (pixel_10.blue + pixel_20.blue + pixel_11.blue + pixel.blue +
                              pixel_12.blue + pixel_22.blue) // 6
            # The bottom edge condition of the image
            elif y == img.height-1 and x != 0 and x != img.width-1:
                pixel_10 = img.get_pixel(x - 1, y - 1)
                pixel_20 = img.get_pixel(x, y - 1)
                pixel_30 = img.get_pixel(x + 1, y - 1)
                pixel_11 = img.get_pixel(x - 1, y)
                pixel_31 = img.get_pixel(x + 1, y)
                blur_pixel.red = (pixel_10.red + pixel_20.red + pixel_30.red + pixel_11.red + pixel.red +
                             pixel_31.red) // 6
                blur_pixel.green = (pixel_10.green + pixel_20.green + pixel_30.green + pixel_11.green + pixel.green +
                               pixel_31.green) // 6
                blur_pixel.blue = (pixel_10.blue + pixel_20.blue + pixel_30.blue + pixel_11.blue + pixel.blue +
                              pixel_31.blue) // 6
            # The (0, 0) site
            elif x == 0 and y == 0:
                pixel_31 = img.get_pixel(x + 1, y)
                pixel_22 = img.get_pixel(x, y + 1)
                pixel_32 = img.get_pixel(x + 1, y + 1)
                blur_pixel.red = (pixel.red +
                             pixel_31.red + pixel_22.red + pixel_32.red) // 4
                blur_pixel.green = (pixel.green +
                               pixel_31.green + pixel_22.green + pixel_32.green) // 4
                blur_pixel.blue = (pixel.blue +
                              pixel_31.blue + pixel_22.blue + pixel_32.blue) // 4
            # The (len(image_width), 0) site
            elif x == img.width-1 and y == 0:
                pixel_11 = img.get_pixel(x - 1, y)
                pixel_12 = img.get_pixel(x - 1, y + 1)
                pixel_22 = img.get_pixel(x, y + 1)
                blur_pixel.red = (pixel_11.red + pixel.red +
                             pixel_12.red + pixel_22.red) // 4
                blur_pixel.green = (pixel_11.green + pixel.green +
                               pixel_12.green + pixel_22.green) // 4
                blur_pixel.blue = (pixel_11.blue + pixel.blue +
                              pixel_12.blue + pixel_22.blue) // 4
            # The (len(image_width), len(image_height)) site
            elif x == img.width-1 and y == img.height-1:
                pixel_10 = img.get_pixel(x - 1, y - 1)
                pixel_20 = img.get_pixel(x, y - 1)
                pixel_11 = img.get_pixel(x - 1, y)
                blur_pixel.red = (pixel_10.red + pixel_20.red+ pixel_11.red + pixel.red
                             ) // 4
                blur_pixel.green = (pixel_10.green + pixel_20.green + pixel_11.green + pixel.green
                               ) // 4
                blur_pixel.blue = (pixel_10.blue + pixel_20.blue + pixel_11.blue + pixel.blue
                              ) // 4
            # The (0, len(image_height)) site
            elif x == 0 and y == img.height-1:
                pixel_20 = img.get_pixel(x, y - 1)
                pixel_30 = img.get_pixel(x + 1, y - 1)
                pixel_31 = img.get_pixel(x + 1, y)
                blur_pixel.red = (pixel_20.red + pixel_30.red+ pixel.red +
                             pixel_31.red) // 4
                blur_pixel.green = (pixel_20.green + pixel_30.green + pixel.green +
                               pixel_31.green) // 4
                blur_pixel.blue = (pixel_20.blue + pixel_30.blue + pixel.blue +
                              pixel_31.blue) // 4
            # All the other pixel sites
            else:
                pixel_10 = img.get_pixel(x - 1, y - 1)
                pixel_20 = img.get_pixel(x, y - 1)
                pixel_30 = img.get_pixel(x + 1, y - 1)
                pixel_11 = img.get_pixel(x - 1, y)
                pixel_31 = img.get_pixel(x + 1, y)
                pixel_12 = img.get_pixel(x - 1, y + 1)
                pixel_22 = img.get_pixel(x, y + 1)
                pixel_32 = img.get_pixel(x + 1, y + 1)
                blur_pixel.red = (pixel_10.red + pixel_20.red + pixel_30.red + pixel_11.red + pixel.red +
                             pixel_31.red + pixel_12.red + pixel_22.red + pixel_32.red) // 9
                blur_pixel.green = (pixel_10.green + pixel_20.green + pixel_30.green + pixel_11.green + pixel.green +
                             pixel_31.green + pixel_12.green + pixel_22.green + pixel_32.green) // 9
                blur_pixel.blue = (pixel_10.blue + pixel_20.blue + pixel_30.blue + pixel_11.blue + pixel.blue +
                             pixel_31.blue + pixel_12.blue + pixel_22.blue + pixel_32.blue) // 9
    return blur_img


def main():
    """
    This program blurs the image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
