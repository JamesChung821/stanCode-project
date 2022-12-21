"""
File: best_photoshop_award.py
Name: James Chung
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage


# Green screen test
# def synthesis(me, background):
#     """
#     :param me: SimpleImage, myself picture
#     :param background: SimpleImage, background image
#     :return: SimpleImage, synthesis image
#     """
#     for y in range(background.height):
#         for x in range(background.width):
#             pixel_me = me.get_pixel(x, y)
#             pixel_background = background.get_pixel(x, y)
#             avg = (pixel_me.red + pixel_me.green + pixel_me.blue) // 3
#             total = pixel_me.red + pixel_me.green + pixel_me.blue
#             if pixel_me.green > avg*1.14 and total > 150:
#                 pixel_me.red = pixel_background.red
#                 pixel_me.green = pixel_background.green
#                 pixel_me.blue = pixel_background.blue
#     return me


def synthesis_different_size(me, background, bonus, bonus1, bonus2, word, word1):
    """
    :param me: SimpleImage, myself picture
    :param background: SimpleImage, background image
    :return: SimpleImage, synthesis image
    """
    # James Chung
    # Create a new blank
    new_image = SimpleImage.blank(background.width, background.height)
    for y in range(me.height):
        for x in range(me.width):
            # Define the pixel at the new blank
            new_pixel = new_image.get_pixel(x+200, y+165)
            # Mark the pixel at myself image
            pixel_me = me.get_pixel(x, y)
            # Set conditions
            avg = (pixel_me.red + pixel_me.green + pixel_me.blue) // 3
            total = pixel_me.red + pixel_me.green + pixel_me.blue
            if pixel_me.green > avg * 1.14 and total > 150:
                new_pixel.red = 255
                new_pixel.green = 255
                new_pixel.blue = 255
            else:
                new_pixel.red = pixel_me.red
                new_pixel.green = pixel_me.green
                new_pixel.blue = pixel_me.blue
    # Nature energy cover letter
    for n in range(bonus.height):
        for m in range(bonus.width):
            new_pixel = new_image.get_pixel(m+12, n+225)
            pixel_bonus = bonus.get_pixel(m, n)
            new_pixel.red = pixel_bonus.red
            new_pixel.green = pixel_bonus.green
            new_pixel.blue = pixel_bonus.blue
    # Stanford logo
    for p in range(bonus1.height):
        for o in range(bonus1.width):
            new_pixel = new_image.get_pixel(o+420, p+10)
            pixel_bonus1 = bonus1.get_pixel(o, p)
            total = pixel_bonus1.red + pixel_bonus1.green + pixel_bonus1.blue
            if total > 80:
                new_pixel.red = pixel_bonus1.red
                new_pixel.green = pixel_bonus1.green
                new_pixel.blue = pixel_bonus1.blue
    # MIT logo
    for w in range(bonus2.height):
        for v in range(bonus2.width):
            new_pixel = new_image.get_pixel(v, w+10)
            pixel_bonus2 = bonus2.get_pixel(v, w)
            total = pixel_bonus2.red + pixel_bonus2.green + pixel_bonus2.blue
            if total < 730:
                new_pixel.red = pixel_bonus2.red
                new_pixel.green = pixel_bonus2.green
                new_pixel.blue = pixel_bonus2.blue
    # Background
    for j in range(new_image.height):
        for i in range(new_image.width):
            pixel_background = background.get_pixel(i, j)
            new_pixel = new_image.get_pixel(i, j)
            if new_pixel.red == 255:
                new_pixel.red = pixel_background.red
                new_pixel.green = pixel_background.green
                new_pixel.blue = pixel_background.blue
    # Artificial intelligence
    for t in range(word.height):
        for s in range(word.width):
            new_pixel = new_image.get_pixel(s+10, t+395)
            pixel_word = word.get_pixel(s, t)
            new_pixel.red = pixel_word.red
            new_pixel.green = pixel_word.green
            new_pixel.blue = pixel_word.blue
    # StanCode will change the world
    for f in range(word1.height):
        for e in range(word1.width):
            new_pixel = new_image.get_pixel(e+330, f+255)
            pixel_word1 = word1.get_pixel(e, f)
            total = pixel_word1.red + pixel_word1.green + pixel_word1.blue
            if total > 60:
                new_pixel.red = pixel_word1.red
                new_pixel.green = pixel_word1.green
                new_pixel.blue = pixel_word1.blue
    return new_image


def shrink(filename):
    """
    :param filename: SimpleImage, the original image
    :return img: SimpleImage, the small image
    """
    # Create a half blank window
    shrink = SimpleImage.blank(filename.width//2, filename.height//2)
    # Shrink 4 pixels in original image to 1 pixel in small image
    # Compress the selection range
    for y in range(filename.height//2):
        for x in range(filename.width//2):
            # The pixel at the upper left site and Select 4 pixels in original image each time
            pixel = filename.get_pixel(x*2, y*2)
            # Print 1 pixel each time in small image
            shrink_pixel = shrink.get_pixel(x, y)
            # The other 3 pixels coordination
            pixel_10 = filename.get_pixel(x*2+1, y*2)
            pixel_01 = filename.get_pixel(x*2, y*2+1)
            pixel_11 = filename.get_pixel(x*2+1, y*2+1)
            # Average the RGB, which can retain the original information
            shrink_pixel.red = (pixel.red + pixel_10.red + pixel_01.red + pixel_11.red) / 4
            shrink_pixel.green = (pixel.green + pixel_10.green + pixel_01.green + pixel_11.green) / 4
            shrink_pixel.blue = (pixel.blue + pixel_10.blue + pixel_01.blue + pixel_11.blue) / 4
    return shrink


def main():
    """
    After graduation from the stanCode, Dr. James Chung successfully made use of Python coding skills to develop
    a better battery testing technique, which was published on the journal of Nature Energy this year
    and selected as the cover letter.
    Meanwhile, the results were also contributed by the group led by MIT professor Richard Braatz, left,
    and Stanford professor William Chueh, right, respectively.
    """
    # Open the file
    background_half = SimpleImage('image_contest/641.jpg')
    background_half.show()
    me = SimpleImage('image_contest/me.jpeg')
    me.show()
    me_shrink = shrink(me)
    me_shrink.show()
    background = SimpleImage('image_contest/Chueh.jpg')
    nature = SimpleImage('image_contest/nature_energy_cover.png')
    logo = SimpleImage('image_contest/stanford_university.png')
    word = SimpleImage('image_contest/AI.png')
    logo_MIT = SimpleImage('image_contest/MIT_logo.jpg')
    word_stanCode = SimpleImage('image_contest/stanCode.png')
    # background.make_as_big_as(me)
    # Adjust picture size
    nature_shrink = shrink(nature)
    logo_shrink = shrink(logo)
    logo_shrink1 = shrink(logo_shrink)
    logo_shrink2 = shrink(logo_shrink1)
    word_shrink = shrink(word)
    logo_MIT_shrink = shrink(logo_MIT)
    logo_MIT_shrink1 = shrink(logo_MIT_shrink)
    word_stanCode_shrink = shrink(word_stanCode)
    # Image synthesis
    synthesis_different_size_image = synthesis_different_size(me_shrink, background_half,
                                                              nature_shrink, logo_shrink2, logo_MIT_shrink1,
                                                              word_shrink, word_stanCode_shrink)
    synthesis_different_size_image.show()
    # synthesis_image = synthesis(me, background)
    # synthesis_image.show()


if __name__ == '__main__':
    main()
