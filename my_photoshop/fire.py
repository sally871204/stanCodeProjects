"""
File: fire.py
Name: 許景涵
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""


from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    """
    This file detects the pixels that are recognized as fire
    and highlights them for better observation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image
    :return: SimpleImage, the updated image with pixels that are recognized as fire turning red
    and others turning to gray scaled
    """
    highlight_img = SimpleImage(filename)
    for x in range(highlight_img.width):
        for y in range(highlight_img.height):
            pixel = highlight_img.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) // 3
            if pixel.red > avg * HURDLE_FACTOR:
                # Pixel of big fire
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                # Grayscale
                pixel.red = avg
                pixel.green = avg
                pixel.blue = avg
    return highlight_img


if __name__ == '__main__':
    main()
