"""
File: babygraphics.py
Name: 許景涵
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000                           # The width of the window
CANVAS_HEIGHT = 600                           # The height of the window
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]  # Python List，我們想要分析的年份(可依需求縮減，不一定 12 個年份都要分析)
GRAPH_MARGIN_SIZE = 20                        # 線(上下左右四條)與視窗的保留距離
COLORS = ['red', 'purple', 'green', 'blue']   # 不同名字的折線使用的顏色，依照名字輸入順序使用，可依需求增加顏色
TEXT_DX = 2                                   # 文字「左邊」與直線之間的距離
LINE_WIDTH = 2                                # The width of each line
MAX_RANK = 1000                               # 每年的資料有保留到的最低的名次


def get_x_coordinate(width, year_index):      # The corresponding x-coordinate of each year
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas = CANVAS_WIDTH
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of year_index on the canvas
    """
    year_space = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)  # Interval between year and year
    return GRAPH_MARGIN_SIZE + year_index * year_space


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw bottom horizontal line with GRAPH_MARGIN_SIZE distance from the bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # Draw top horizontal line with GRAPH_MARGIN_SIZE distance from the top
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Draw vertical lines and add year text
    # enumerate: iterates over a sequence (such as a list, tuple, or string)
    # while keeping track of the index of the current item. It returns pairs of the form (index, element).
    for year_index, year in enumerate(YEARS):
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX, text=str(year), anchor=tkinter.NW)
        # The year text has the distance of TEXT_DX from the vertical line and the bottom horizontal line.
        # The text is on the lower right corner of the intersection, using northwest as its datum point.

    '''
    # Another Solution
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)
    '''


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of names, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (list[str]): A list of names whose data we want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # Initialize the index of names typed in the "Names" bar
    name_index = 0

    for name in lookup_names:
        # Get line color in sequence of COLORS
        color = COLORS[name_index % len(COLORS)]

        # Draw the name line graphs
        draw_name_lines(canvas, name_data, name, color)

        # Increment color index for the next name
        name_index += 1


def draw_name_lines(canvas, name_data, name, color):
    """
    Draw the lines for given names on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        name (str): The name for which the line is drawn
        color (str): The color of the lines and names

    Returns:
        This function does not return any value.
    """
    x_list = []  # A list storing x-coordinate every year
    y_list = []  # A list storing y-coordinate every year
    ranks = []     # Corrected

    for year_index, year in enumerate(YEARS):  # Data type of year_index & year are both int
        # Calculate x-coordinate
        x_list.append(get_x_coordinate(CANVAS_WIDTH, year_index))
        print(str(year))  # Corrected, to check on console if the program is running correctly

        # Corrected
        if str(year) in name_data[name]:            # Data type of year in name_data is str
            rank = int(name_data[name][str(year)])  # Data type of rank is int
            ranks.append(rank)

            # Calculate y-coordinate based on rank
            rank_interval = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / (MAX_RANK - 1)
            y_list.append(GRAPH_MARGIN_SIZE + (rank - 1) * rank_interval)
            # Corrected. The higher the ranking, the higher the y-coordinate is.

        # Corrected
        else:
            # If the year is not in the data, set y-coordinate to the bottom line
            y_list.append(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
            ranks.append('*')

        # Show name and rank on the upper right of each data point
        label_x = get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX
        label_y = y_list[year_index] - TEXT_DX
        canvas.create_text(label_x, label_y, text=f"{name} {ranks[year_index]}", anchor=tkinter.SW, fill=color)
        print(y_list)  # List of y-coordinates of each data point
        # Corrected, to check on console if the program is running correctly

    # Draw line graphs
    # zip: takes iterables (like lists) as input and returns an iterator of tuples,
    # where the i-th(the tuple at position i) tuple contains the i-th element from each of the input iterables.
    # *zip(x_list, y_list) becomes two separate lists, one for x-coordinates and one for y-coordinates.
    # These lists are then passed as arguments to draw a line on the canvas using the specified x and y coordinates.
    canvas.create_line(*zip(x_list, y_list), width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
