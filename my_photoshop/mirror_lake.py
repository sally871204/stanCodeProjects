"""
File: mirror_lake.py
Name: 許景涵
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""


from simpleimage import SimpleImage


def main():
    """
    This file makes a new image that creates a mirror lake vibe
    by placing an inverse image below the original image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: SimpleImage, the image which is a mirror lake vibe of the original image
    """
    original_img = SimpleImage(filename)
    reflected_img = SimpleImage.blank(original_img.width, original_img.height * 2)
    for x in range(original_img.width):
        for y in range(original_img.height):
            old_p = original_img.get_pixel(x, y)

            new_p_up = reflected_img.get_pixel(x, y)
            new_p_up.red = old_p.red
            new_p_up.green = old_p.green
            new_p_up.blue = old_p.blue

            new_p_down = reflected_img.get_pixel(x, reflected_img.height-1-y)
            new_p_down.red = old_p.red
            new_p_down.green = old_p.green
            new_p_down.blue = old_p.blue
    return reflected_img


if __name__ == '__main__':
    main()
