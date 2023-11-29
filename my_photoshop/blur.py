"""
File: blur.py
Name: 許景涵
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""
from simpleimage import SimpleImage

#
#
# def main():
#     """
#     This file shows the original image first, and then its blurred image.
#     The blurred image is blurred more than once by using the for loop.
#     """
#     old_img = SimpleImage("images/smiley-face.png")
#     old_img.show()
#
#     blurred_img = blur(old_img)
#     for i in range(5):
#         blurred_img = blur(blurred_img)
#     blurred_img.show()
#
#
# def blur(img):
#     """
#     :param img: SimpleImage, the original image
#     :return: SimpleImage, blurred image
#     """
#     old_img = SimpleImage(img)
#     new_img = SimpleImage.blank(old_img.width, old_img.height)
#     for x in range(old_img.width):
#         for y in range(old_img.height):
#             # At first, get the pixel and RGB of (x, y) itself
#             old_p = old_img.get_pixel(x, y)
#             new_red = old_p.red
#             new_green = old_p.green
#             new_blue = old_p.blue
#             neighbor_count = 0
#
#             # (x, y) has left column
#             if x-1 >= 0:
#
#                 # (x, y) has top left
#                 if y-1 >= 0:
#                     old_p = old_img.get_pixel(x-1, y-1)
#                     new_red += old_p.red
#                     new_green += old_p.green
#                     new_blue += old_p.blue
#                     neighbor_count += 1
#
#                 # (x, y) has bottom left
#                 if y+1 <= old_img.height - 1:
#                     old_p = old_img.get_pixel(x-1, y+1)
#                     new_red += old_p.red
#                     new_green += old_p.green
#                     new_blue += old_p.blue
#                     neighbor_count += 1
#
#                 # if (x, y) has left column, (x, y) must have middle left
#                 old_p = old_img.get_pixel(x-1, y)
#                 new_red += old_p.red
#                 new_green += old_p.green
#                 new_blue += old_p.blue
#                 neighbor_count += 1
#
#             # middle column [the column of (x, y)]
#             if x >= 0:
#
#                 # (x, y) has up
#                 if y-1 >= 0:
#                     old_p = old_img.get_pixel(x, y-1)
#                     new_red += old_p.red
#                     new_green += old_p.green
#                     new_blue += old_p.blue
#                     neighbor_count += 1
#
#                 # (x, y) has down
#                 if y+1 <= old_img.height - 1:
#                     old_p = old_img.get_pixel(x, y+1)
#                     new_red += old_p.red
#                     new_green += old_p.green
#                     new_blue += old_p.blue
#                     neighbor_count += 1
#
#             # (x, y) has right column
#             if x+1 <= old_img.width - 1:
#
#                 # (x, y) has top right
#                 if y-1 >= 0:
#                     old_p = old_img.get_pixel(x+1, y-1)
#                     new_red += old_p.red
#                     new_green += old_p.green
#                     new_blue += old_p.blue
#                     neighbor_count += 1
#
#                 # (x, y) has bottom right
#                 if y+1 <= old_img.height - 1:
#                     old_p = old_img.get_pixel(x+1, y+1)
#                     new_red += old_p.red
#                     new_green += old_p.green
#                     new_blue += old_p.blue
#                     neighbor_count += 1
#
#                 # if (x, y) has right column, (x, y) must have middle right
#                 old_p = old_img.get_pixel(x+1, y)
#                 new_red += old_p.red
#                 new_green += old_p.green
#                 new_blue += old_p.blue
#                 neighbor_count += 1
#
#             new_red.red = new_red / (1+neighbor_count)
#             new_green.green = new_green / (1+neighbor_count)
#             new_blue.blue = new_blue / (1+neighbor_count)
#     return new_img


"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""
# from simpleimage import SimpleImage

# Adjust the degree of blurring, preset 5 times
BLUR_LAYER = 5


def main():
    """
    Function: Blur the picture in 5 layers.
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLUR_LAYER):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: SimpleImage, Original picture
    :return new_img: SimpleImage, Blurred image
    Function: Blur the imported image
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):

            pixel = new_img.get_pixel(x, y)

            total_red = 0
            total_blue = 0
            total_green = 0
            total_num = 0

            # Judgment is the first row, which determines the upper limit area
            if x == 0:
                row_left = x
            else:
                row_left = x - 1

            # Judgment is the first column, determines the left limit area
            if y == 0:
                col_up = y
            else:
                col_up = y - 1

            # Judgment is the last row, determine the lower limit area
            if x == (img.width-1):
                row_right = x
            else:
                row_right = x + 1

            # Judgment is the last column, determines the right limit area
            if y == (img.height-1):
                col_down = y
            else:
                col_down = y + 1

            # RGB values, add up individually
            for r in range(row_left, row_right + 1):       # x
                for c in range(col_up, col_down + 1):   # y
                    total_red += img.get_pixel(r, c).red
                    total_blue += img.get_pixel(r, c).blue
                    total_green += img.get_pixel(r, c).green
                    total_num += 1

            # RGB average value, put it back separately.
            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blue / total_num

    return new_img


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()
