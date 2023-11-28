"""
File: blur.py
Name: 許景涵
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage
num_blurs = 5   # Adjust the degree of blurring


def main():
    """
    Function: Blur the image 5 times
    Principle: The new RGB of each pixel is the average RGB values of its nearest neighbors
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(num_blurs):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the blurred image
    Function: Blur the original image
    Principle: The new RGB of each pixel is the average RGB values of its nearest neighbors
    """
    new_w, new_h = img.width, img.height
    new_img = SimpleImage.blank(new_w, new_h)

    for x in range(new_w):
        for y in range(new_h):
            total_r, total_g, total_b = 0, 0, 0
            count = 0

            # 確保左邊(x 軸)的鄰居像素 x 不能小於 0。如果 x-1 小於 0，max 函數將返回 0，這是為了確保不超出左邊界。
            row_left = max(0, x - 1)

            # 確保上方(y 軸)的鄰居像素 y 不能小於 0。如果 y-1 小於 0，max 函數將返回 0，這是為了確保不超出上邊界。
            col_up = max(0, y - 1)

            # 確保右邊(x 軸)的鄰居像素 x 不能超過 new_w-1。如果 x+1 大於 new_w-1，min 函數將返回 new_w-1，這是為了確保不超出右邊界。
            row_right = min(new_w - 1, x + 1)

            # 確保下方(y 軸)的鄰居像素 y 不能超過 new_h-1。如果 y+1 大於 new_h-1，min 函數將返回 new_h-1，這是為了確保不超出下邊界。
            col_down = min(new_h - 1, y + 1)

            for r in range(row_left, row_right + 1):       # x
                for c in range(col_up, col_down + 1):      # y
                        total_r += img.get_pixel(r, c).red
                        total_g += img.get_pixel(r, c).green
                        total_b += img.get_pixel(r, c).blue
                        count += 1

            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = total_r // count
            new_pixel.green = total_g // count
            new_pixel.blue = total_b // count

            # new_img.set_pixel(x, y, (avg_r, avg_g, avg_b))

    return new_img


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
