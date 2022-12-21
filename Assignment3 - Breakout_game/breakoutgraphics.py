"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
File: breakoutgraphics.py
Name: James Chung
---------------------
This project is a class created to execute a breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.ball_radius = ball_radius

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)

        # Instance variable
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        # Set keyword argument in case users change the parameters
        self.paddle = GRect(width = paddle_width, height = paddle_height, x = (window_width - paddle_width)/2, y = window_height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(width = ball_radius*2, height = ball_radius*2, x = (window_width - ball_radius)/2, y = (window_height - ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmouseclicked(self.wait_for_click)
        onmousemoved(self.drag_paddle)

        # Draw bricks.
        self.remove_bricks = 0
        for j in range(brick_rows):
            for i in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.window.add(self.brick, x=(brick_spacing + brick_width) * i,
                                y=brick_offset + (brick_spacing + brick_height) * j)
                if j < 2:
                    self.brick.color = 'red'
                    self.brick.filled = True
                    self.brick.fill_color = 'red'

                elif 4 > j >= 2:
                    self.brick.color = 'orange'
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'

                elif 6 > j >= 4:
                    self.brick.color = 'yellow'
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'

                elif 8 > j >= 6:
                    self.brick.color = 'green'
                    self.brick.filled = True
                    self.brick.fill_color = 'green'

                elif 10 > j >= 8:
                    self.brick.color = 'blue'
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'

    def drag_paddle(self, event):
        self.window.add(self.paddle, x = event.x - self.paddle_width / 2,
                        y = self.window.height - self.paddle_offset - self.paddle_height)
        if self.paddle.x < 0:
            self.window.add(self.paddle, x = 0,
                            y = self.window.height - self.paddle_offset - self.paddle_height)
        elif self.paddle.x >= self.window.width - self.paddle_width:
            self.window.add(self.paddle, x = self.window.width - self.paddle_width,
                            y = self.window.height - self.paddle_offset - self.paddle_height)

    def wait_for_click(self, event):
        x = event.x
        y = event.y
        if self.__dx == 0 and 0 < x <= self.window.width and 0 < y <= self.window.height:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def ball_hit_boundary(self):
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball_radius*2:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def reset_ball(self):
        self.set_ball_position()
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball)

    def set_ball_position(self):
        self.ball.x = (self.window.width - self.ball_radius)/2
        self.ball.y = (self.window.height - self.ball_radius)/2

    def check_for_collisions(self):
        self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
        if self.obj is not None:
            pass
            # return self.obj
        else:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius*2)
            if self.obj is None:
                self.obj = self.window.get_object_at(self.ball.x + self.ball_radius*2, self.ball.y + self.ball_radius*2)
                if self.obj is None:
                    self.obj = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
                    if self.obj is None:
                        return None
                    else:
                        pass
                        # return self.obj
                else:
                    pass
                    # return self.obj
            else:
                pass
                # return self.obj

    def check_brick_or_paddle(self):
        if self.obj is self.paddle:
            self.__dy = -self.__dy
        elif self.obj is not None and self.obj is not self.paddle:
            self.window.remove(self.obj)
            self.remove_bricks += 1
            self.__dy = -self.__dy

    # Getter
    # You can see but you cannot change
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy