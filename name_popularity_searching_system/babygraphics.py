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
         1960, 1970, 1980, 1990, 2000, 2010]  # Python List，裡面的每一個元素為我們想要分析的年份(不一定只有 12 個年份)
GRAPH_MARGIN_SIZE = 20                        # 線與視窗的保留距離
COLORS = ['red', 'purple', 'green', 'blue']   # 不同名字的折線使用的顏色，依照順序使用
TEXT_DX = 2                                   # 文字「左邊」與直線之間的距離
LINE_WIDTH = 2                                # The width of each line
MAX_RANK = 1000                               # 每年的資料有保留到的最低的名次


def get_x_coordinate(width, year_index):      # The corresponding x-coordinate of each year
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    interval = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * interval


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw bottom horizontal line, having GRAPH_MARGIN_SIZE distance from the bottom
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # Draw top horizontal line, having GRAPH_MARGIN_SIZE distance from the top
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Draw vertical lines and add year text
    for year_index, year in enumerate(YEARS):
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX, anchor=tkinter.NW, text=str(year))


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

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
    Draws the lines for given names on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        name (str): The name for which the line is drawn
        color (str): The color of the lines and names

    Returns:
        This function does not return any value.
    """
    x_values = []
    y_values = []

    for year_index, year in enumerate(YEARS):
        # Calculate x-coordinate
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        x_values.append(x)

        if year in name_data[name]:
            rank = int(name_data[name][year])

            # Calculate y-coordinate based on rank
            if rank <= MAX_RANK:
                interval = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / (MAX_RANK - 1)
                y = GRAPH_MARGIN_SIZE + (MAX_RANK - rank) * interval
            else:
                # If rank is over MAX_RANK, set y-coordinate to the bottom line
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            y_values.append(y)

            # Show name and rank on the upper right of each data point
            label_x = x + TEXT_DX
            label_y = y - TEXT_DX
            canvas.create_text(label_x, label_y, text=f"{name} {rank}", anchor=tkinter.SW, fill=color)

        else:
            # If the year is not in the data, set y-coordinate to the bottom line
            y_values.append(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Draw line graphs
    canvas.create_line(*zip(x_values, y_values), width=LINE_WIDTH, fill=color)


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
