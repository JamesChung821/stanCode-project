"""
File: sierpinski.py
Name: James Chung
This program is designed to plot a triangle with numerous triangles inside.
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Start a recursive function to plot a triangle with numerous triangles inside
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	A recursive function to plot numerous triangles
	:param order: int, number of different sizes of triangles
	:param length: int, side length of triangles
	:param upper_left_x: int, x coordination of an initial triangle
	:param upper_left_y: int, y coordination of an initial triangle
	:return: object, three side lengths
	"""
	# The first big triangle, top down
	if order == ORDER:
		edge_left = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		edge_top = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		edge_right = GLine(upper_left_x + length * 0.5, upper_left_y + length * 0.866, upper_left_x + length,
						   upper_left_y)
		window.add(edge_left)
		window.add(edge_top)
		window.add(edge_right)
	# Base case
	if order == 0:
		pass
	# Recursion
	else:
		# A setting of top-up triangle, half of the original one
		edge_left1 = GLine(upper_left_x + length * 0.5 * 0.5, upper_left_y + length * 0.866 * 0.5,
						   upper_left_x + length * 0.5, upper_left_y)
		edge_bottom = GLine(upper_left_x + length * 0.5 * 0.5, upper_left_y + length * 0.866 * 0.5,
							upper_left_x + length * 0.5 * 0.5 + length * 0.5, upper_left_y + length * 0.866 * 0.5)
		edge_right1 = GLine(upper_left_x + length * 0.5, upper_left_y,
							upper_left_x + length * 0.5 * 0.5 + length * 0.5, upper_left_y + length * 0.866 * 0.5)
		window.add(edge_left1)
		window.add(edge_bottom)
		window.add(edge_right1)
		# Recursive triangles, each triangle is half of the triangle before recursion
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length * 0.5, upper_left_y)
		sierpinski_triangle(order - 1, length / 2,
							upper_left_x + length * 0.5 * 0.5, upper_left_y + length * 0.866 * 0.5)


if __name__ == '__main__':
	main()