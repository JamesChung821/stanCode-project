"""
SC101P Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
File: babygraphic.py
Name: James Chung
----------------------
This program plots the data via line chart
"""

import tkinter
import babynames
import babygraphicsgui as gui
from campy.graphics.gwindow import GWindow

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000

def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    coordination = GRAPH_MARGIN_SIZE + (width-GRAPH_MARGIN_SIZE*2)*year_index/len(YEARS)
    return  coordination


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width = LINE_WIDTH)
    # Top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width = LINE_WIDTH)
    # Vertical lines and year
    for index in range (len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + (CANVAS_WIDTH-GRAPH_MARGIN_SIZE*2)*index/len(YEARS),
                           0,
                           GRAPH_MARGIN_SIZE + (CANVAS_WIDTH-GRAPH_MARGIN_SIZE*2)*index/len(YEARS),
                           CANVAS_HEIGHT, width = LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE + (CANVAS_WIDTH - GRAPH_MARGIN_SIZE * 2) * index / len(YEARS) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX,
                           text = YEARS[index],
                           anchor = tkinter.NW)


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

    # Write your code below this line
    #################################
    d = name_data
    # Find name in lookup_names list
    for name in range (len(lookup_names)):
        # If name in list is in the dictionary
        if lookup_names[name] in d:
            # Mark name and rank
            for name_rank in range (len(YEARS)):
                # If the rank is not recorded
                # Remember the str and int transformation
                if str(YEARS[name_rank]) not in str(d[lookup_names[name]]):
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, name_rank) + TEXT_DX,
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE - TEXT_DX,
                                       text = lookup_names[name] + ' *',
                                       fill = COLORS[name%len(COLORS)],
                                       anchor = tkinter.SW)
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, name_rank) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + int(d[lookup_names[name]][str(YEARS[name_rank])])/2,
                                       text = lookup_names[name] + ' ' + d[lookup_names[name]][str(YEARS[name_rank])],
                                       fill = COLORS[name%len(COLORS)],
                                       anchor = tkinter.SW)
            # Plot the line
            # There is no line after 2020
            for rank in range (len(YEARS)-1):
                # If the first and subsequent year do not record the rank
                if str(YEARS[rank]) not in str(d[lookup_names[name]]) and str(YEARS[rank+1]) not in str(d[lookup_names[name]]):
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, rank),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, rank + 1),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       width = LINE_WIDTH,
                                       fill = COLORS[name%len(COLORS)])
                # The first year does not record the rank, but the subsequent year does
                elif str(YEARS[rank]) not in str(d[lookup_names[name]]):
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, rank),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, rank + 1),
                                       GRAPH_MARGIN_SIZE + int(d[lookup_names[name]][str(YEARS[rank+1])])/2,
                                       width = LINE_WIDTH,
                                       fill = COLORS[name%len(COLORS)])
                # The subsequent year does not record the rank
                elif str(YEARS[rank+1]) not in str(d[lookup_names[name]]):
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, rank),
                                       GRAPH_MARGIN_SIZE + int(d[lookup_names[name]][str(YEARS[rank])]) / 2,
                                       get_x_coordinate(CANVAS_WIDTH, rank + 1),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       width = LINE_WIDTH,
                                       fill = COLORS[name%len(COLORS)])
                else:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, rank),
                                       GRAPH_MARGIN_SIZE + int(d[lookup_names[name]][str(YEARS[rank])])/2,
                                       get_x_coordinate(CANVAS_WIDTH, rank + 1),
                                       GRAPH_MARGIN_SIZE + int(d[lookup_names[name]][str(YEARS[rank+1])])/2,
                                       width = LINE_WIDTH,
                                       fill = COLORS[name%len(COLORS)])


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
