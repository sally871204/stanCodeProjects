"""
File: green_screen.py
Name: 許景涵
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""


from simpleimage import SimpleImage


def main():
    """
    This function replaces the green pixels in "ReyGreenScreen.png"
    with MillenniumFalcon.png
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the space_ship image
    :param figure_img: SimpleImage, the figure image
    :return: SimpleImage, the updated image with space_ship as background
    replacing the green pixels in figure
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            fig_pixel = figure_img.get_pixel(x, y)
            bigger = max(fig_pixel.red, fig_pixel.blue)    # Returns the one that is bigger
            if fig_pixel.green > 2 * bigger:
                bg_pixel = background_img.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.blue = bg_pixel.blue
                fig_pixel.green = bg_pixel.green
    return figure_img


if __name__ == '__main__':
    main()
