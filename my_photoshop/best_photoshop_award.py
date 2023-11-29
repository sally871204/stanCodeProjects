"""
File: best_photoshop_award.py
Name: 許景涵
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""


from simpleimage import SimpleImage


# Controls the upper bound for black pixel
BLACK_PIXEL = 130


def main():
    """
    This function replaces the green screen of sally.JPG
    and photoshops myself onto a background, which is the window seat of an airplane.
    Want to travel to other country so bad :(
    """
    me = SimpleImage('image_contest/sally.jpg')      # 2014 x 2738
    # me.show()
    bg = SimpleImage('image_contest/airplane.JPG')   # 1811 x 3220
    bg.make_as_big_as(me)                            # 2014 x 2738
    combined_img = combine(me, bg)
    combined_img.show()


def combine(me, bg):
    """
    :param me: SimpleImage, the sally.JPG image
    :param bg: SimpleImage, the airplane.JPG image
    :return: SimpleImage, the updated image with airplane.JPG as background
    replacing the green pixels in sally.JPG
    """
    for x in range(me.width):
        for y in range(me.height):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.green + pixel_me.blue) // 3
            total = pixel_me.red + pixel_me.green + pixel_me.blue
            if pixel_me.green > avg and total > BLACK_PIXEL:
                # Remove green screen
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.green = pixel_bg.green
                pixel_me.blue = pixel_bg.blue
    return me


if __name__ == '__main__':
    main()
