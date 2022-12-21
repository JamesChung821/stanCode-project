"""
File: breakoutgraphics_extensions.py
Name: James Chung
----------------------------
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
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING, turns = 0,
                 title='Breakout'):
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.ball_radius = ball_radius
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.nturns = turns
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)

        # Instance variable
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.background = GRect(width = self.window.width, height = self.window.height)
        self.background.filled = True
        self.window.add(self.background)

        # Create a paddle.
        # Set keyword argument in case users change the parameters
        self.paddle = GRect(width = paddle_width, height = paddle_height, x = (window_width - paddle_width)/2, y = window_height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'white'
        self.window.add(self.paddle)

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
        # Real and fake bricks
        self.random_brick_real = GRect(self.brick_width, self.brick_height)
        self.random_brick_fake = GRect(self.brick_width, self.brick_height)
        # Number of statistic bricks
        self.score_brick_red = 0
        self.score_brick_orange = 0
        self.score_brick_yellow = 0
        self.score_brick_green = 0
        self.score_brick_blue = 0

        # Labels
        # Scores label
        self.score = 0
        self.score_label = GLabel('Scores: ' + str(self.score))
        self.score_label.color = 'white'
        self.score_label.font = '-20'
        self.window.add(self.score_label, 1, self.score_label.height + 10)

        # Number of turns
        self.turns = GLabel('Nturns: ' + str(self.nturns))
        self.turns.color = 'white'
        self.turns.font = '-20'
        self.window.add(self.turns, 320, self.score_label.height + 10)

        # Combo
        self.combos = 0
        self.combo = GLabel('Combo!!!')
        self.combo.font = '-32'
        self.window.add(self.combo, (self.window.width - self.combo.width) / 2,
                        (self.window.height - self.combo.height) / 2 + 150)

        # Click to start
        self.click_to_start = GLabel('>>> Click to start <<<')
        self.click_to_start.color = 'white'
        self.click_to_start.font = '-16'
        self.window.add(self.click_to_start, (self.window.width - self.click_to_start.width)/2, 500)

        # Set level
        self.level1 = GLabel('Level 1 - Warm up')
        self.level1.color = 'blue'
        self.level1.font = '-20'
        self.window.add(self.level1, (self.window.width - self.level1.width)/2, 625)

        self.level2 = GLabel('Level 2 - Hollow ball')
        self.level2.color = 'green'
        self.level2.font = '-20'
        self.level2_hit = 0

        self.level3 = GLabel('Level 3 - Real and fake bricks')
        self.level3.color = 'yellow'
        self.level3.font = '-20'
        self.level3_hit = 0

        self.level4 = GLabel('Level 4 - Tunneling ball')
        self.level4.color = 'orange'
        self.level4.font = '-20'
        self.level4_hit = 0

        self.level5 = GLabel('Level 5 - Flash ball')
        self.level5.color = 'red'
        self.level5.font = '-20'
        self.level5_hit = 0

        # Center a filled ball in the graphical window.
        self.ball = GOval(width=ball_radius * 2, height=ball_radius * 2, x=(window_width - ball_radius) / 2,
                                  y=(window_height - ball_radius) / 2)
        self.ball.filled = True
        self.ball.fill_color = 'white'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        # Resolve the phenomenon of sticky ball on paddle
        self.dy = INITIAL_Y_SPEED

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
        # Click to react
        if self.__dx == 0 and 0 < x <= self.window.width and 0 < y <= self.window.height:
            # Change ball x velocity
            if self.score > 20:
                self.__dx = MAX_X_SPEED
            else:
                self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
        # Make click-to-start button invisible
        self.click_to_start.color = 'black'

    def ball_hit_boundary(self):
        # Right and left edge
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball_radius*2:
            # Level 4 - Tunneling ball
            if 120 < self.score <= 220:
                if self.ball.x <= 0:
                    self.ball.x = self.window.width - self.ball_radius*2 -1
                elif self.ball.x >= self.window.width - self.ball_radius*2:
                    self.ball.x = 1
                # Set level label
                self.window.remove(self.level3)
                self.level4_hit += 1
                if self.level4_hit == 1:
                    self.window.add(self.level4, (self.window.width - self.level4.width) / 2, 625)
            # Rebound the ball
            else:
                self.__dx = -self.__dx
        # Top edge
        if self.ball.y <= 0:
            # Level 4 - Tunneling ball
            if 120 < self.score <= 250:
                self.ball.y = self.window.height - self.ball_radius * 2 - 1
            # Rebound the ball
            else:
                self.__dy = -self.__dy

    def reset_ball(self):
        self.set_ball_position()
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball)
        self.click_to_start.color = 'white'

    def set_ball_position(self):
        self.ball.x = (self.window.width - self.ball_radius)/2
        self.ball.y = (self.window.height - self.ball_radius)/2

    def check_for_collisions(self):
        self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
        if self.obj is not None:
            return self.obj
        else:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius*2)
            if self.obj is None:
                self.obj = self.window.get_object_at(self.ball.x + self.ball_radius*2, self.ball.y + self.ball_radius*2)
                if self.obj is None:
                    self.obj = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
                    if self.obj is None:
                        return None
                    else:
                        return self.obj
                else:
                    return self.obj
            else:
                return self.obj

    def check_brick_or_paddle(self):
        if self.obj == self.paddle:
            self.__dy = -self.dy
            # Make combo invisible
            self.combos = 0
            self.combo.color = 'black'
            # Level 3 - Real and fake bricks
            if 250 >= self.score > 60 and self.score % 2 == 0:
                self.brick_roll_real_x = random.randint(0, self.window.width - self.brick_width)
                self.brick_roll_real_y = random.randint(self.brick_offset + (self.brick_spacing + self.brick_height) * 10, (self.brick_spacing + self.brick_height) * 20)
                self.brick_roll_fake_x = random.randint(0, self.window.width - self.brick_width)
                self.brick_roll_fake_y = random.randint(self.brick_offset + (self.brick_spacing + self.brick_height) * 10,
                                                        (self.brick_spacing + self.brick_height) * 20)
                self.random_brick_real.filled = True
                self.random_brick_real.fill_color = 'white'
                self.random_brick_real.color = 'white'
                self.window.add(self.random_brick_real, self.brick_roll_real_x, self.brick_roll_real_y)

                self.random_brick_fake.filled = True
                self.random_brick_fake.fill_color = 'white'
                self.random_brick_fake.color = 'white'
                self.window.add(self.random_brick_fake, self.brick_roll_fake_x, self.brick_roll_fake_y)

                # Set level label
                self.window.remove(self.level2)
                self.level3_hit += 1
                if self.level3_hit == 1:
                    self.window.add(self.level3, (self.window.width - self.level3.width) / 2, 625)
            # Speed up
            if 120 > self.score >= 20:
                self.speed_up()
            # Clean the fake brick
            if self.score > 250:
                self.random_brick_fake.color = 'black'
                self.random_brick_fake.fill_color = 'black'

        elif self.obj is not None and self.obj is not self.paddle and self.obj is not self.background \
                and self.obj is not self.score_label and self.obj is not self.turns and self.obj is not self.combo \
                and self.obj is not self.random_brick_fake and self.obj is not self.click_to_start \
                and self.obj is not self.level1 and self.obj is not self.level2 and self.obj is not self.level3 \
                and self.obj is not self.level4 and self.obj is not self.level5:
            # Remove the bricks
            self.window.remove(self.obj)
            # Level 2 - hollow ball
            if self.score > 20:
                self.ball.color = 'white'
                self.ball.fill_color = 'black'
                # Set level label
                self.window.remove(self.level1)
                self.level2_hit += 1
                if self.level2_hit == 1:
                    self.window.add(self.level2, (self.window.width - self.level2.width) / 2, 625)
            # Show combo
            self.combos += 1
            if self.combos > 1:
                self.combo.color = 'white'
            # Record the scores
            if self.brick_offset + (self.brick_spacing + self.brick_height) * 10 \
                    > self.obj.y >= self.brick_offset + (self.brick_spacing + self.brick_height) * 8:
                self.score += 1
                self.score_brick_blue += 1
            elif self.brick_offset + (self.brick_spacing + self.brick_height) * 8 \
                    > self.obj.y >= self.brick_offset + (self.brick_spacing + self.brick_height) * 6:
                self.score += 2
                self.score_brick_green += 1
            elif self.brick_offset + (self.brick_spacing + self.brick_height) * 6 \
                    > self.obj.y >= self.brick_offset + (self.brick_spacing + self.brick_height) * 4:
                self.score += 3
                self.score_brick_yellow += 1
            elif self.brick_offset + (self.brick_spacing + self.brick_height) * 4 \
                    > self.obj.y >= self.brick_offset + (self.brick_spacing + self.brick_height) * 2:
                self.score += 4
                self.score_brick_orange += 1
            elif self.brick_offset + (self.brick_spacing + self.brick_height) * 2 \
                    > self.obj.y >= self.brick_offset + (self.brick_spacing + self.brick_height) * 0:
                self.score += 5
                self.score_brick_red += 1
            # Show score label
            self.score_label.text = 'Scores: ' + str(self.score)
            self.__dy = -self.__dy

    def set_gameover(self):
        self.gameover_cover = GRect(self.window.width, 300)
        self.gameover_cover.filled = True
        self.gameover_cover.fill_color = 'black'
        self.window.add(self.gameover_cover, 0, self.brick_offset + (self.brick_spacing + self.brick_height) * 10)

        self.gameover = GLabel('Game Over')
        self.gameover.font = '-32'
        self.gameover.color = 'white'
        self.window.add(self.gameover, (self.window.width - self.gameover.width) / 2,
                        (self.window.height - self.gameover.height) / 2 + 100)
        self.set_comment()

    def set_you_win(self):
        self.gameover_cover = GRect(self.window.width, 300)
        self.gameover_cover.filled = True
        self.gameover_cover.fill_color = 'black'
        self.window.add(self.gameover_cover, 0, self.brick_offset + (self.brick_spacing + self.brick_height) * 10)

        self.gameover = GLabel('You Win!')
        self.gameover.font = '-32'
        self.gameover.color = 'white'
        self.window.add(self.gameover, (self.window.width - self.gameover.width) / 2,
                        (self.window.height - self.gameover.height) / 2 + 100)

        self.legendary = GLabel('Legendary!')
        self.legendary.font = '-32'
        self.legendary.color = 'red'
        self.window.add(self.legendary, (self.window.width - self.legendary.width) / 2,
                        (self.window.height - self.legendary.height) / 2 + 35)
        self.set_statistics()

    def set_comment(self):
        if self.score <= 20:
            self.loser = GLabel('Are you loser?')
            self.loser.font = '-32'
            self.loser.color = 'red'
            self.window.add(self.loser, (self.window.width - self.loser.width) / 2,
                            (self.window.height - self.loser.height) / 2 + 35)
        elif 20 < self.score <= 60:
            self.way_to_go = GLabel('Way to go!')
            self.way_to_go.font = '-32'
            self.way_to_go.color = 'blue'
            self.window.add(self.way_to_go, (self.window.width - self.way_to_go.width) / 2,
                            (self.window.height - self.way_to_go.height) / 2 + 35)
        elif 60 < self.score <= 120:
            self.good_job = GLabel('Good job!')
            self.good_job.font = '-32'
            self.good_job.color = 'green'
            self.window.add(self.good_job, (self.window.width - self.good_job.width) / 2,
                            (self.window.height - self.good_job.height) / 2 + 35)
        elif 120 < self.score <=200:
            self.you_are_amazing = GLabel('You are amazing!')
            self.you_are_amazing.font = '-32'
            self.you_are_amazing.color = 'yellow'
            self.window.add(self.you_are_amazing, (self.window.width - self.you_are_amazing.width) / 2,
                            (self.window.height - self.you_are_amazing.height) / 2 + 35)
        elif 200 < self.score < 300:
            self.unbelievable = GLabel('Unbelievable!')
            self.unbelievable.font = '-32'
            self.unbelievable.color = 'orange'
            self.window.add(self.unbelievable, (self.window.width - self.unbelievable.width) / 2,
                            (self.window.height - self.unbelievable.height) / 2 + 35)
        self.set_statistics()

    def set_statistics(self):
        # Red brick
        self.brick_red = GRect(self.brick_width, self.brick_height)
        # self.brick_red.color = 'red'
        self.brick_red.filled = True
        self.brick_red.fill_color = 'red'
        self.window.add(self.brick_red, 75, 420)
        # Label
        self.brick_red_number = GLabel('X ' + str(self.score_brick_red))
        self.brick_red_number.color = 'white'
        self.brick_red_number.font = '-14'
        self.window.add(self.brick_red_number, 125, 440)
        # Orange brick
        self.brick_orange = GRect(self.brick_width, self.brick_height)
        # self.brick_orange.color = 'orange'
        self.brick_orange.filled = True
        self.brick_orange.fill_color = 'orange'
        self.window.add(self.brick_orange, 185, 420)
        # Label
        self.brick_orange_number = GLabel('X ' + str(self.score_brick_orange))
        self.brick_orange_number.color = 'white'
        self.brick_orange_number.font = '-14'
        self.window.add(self.brick_orange_number, 235, 440)
        # Yellow brick
        self.brick_yellow = GRect(self.brick_width, self.brick_height)
        # self.brick_yellow.color = 'yellow'
        self.brick_yellow.filled = True
        self.brick_yellow.fill_color = 'yellow'
        self.window.add(self.brick_yellow, 295, 420)
        # Label
        self.brick_yellow_number = GLabel('X ' + str(self.score_brick_yellow))
        self.brick_yellow_number.color = 'white'
        self.brick_yellow_number.font = '-14'
        self.window.add(self.brick_yellow_number, 345, 440)
        # Green brick
        self.brick_green = GRect(self.brick_width, self.brick_height)
        # self.brick_green.color = 'green'
        self.brick_green.filled = True
        self.brick_green.fill_color = 'green'
        self.window.add(self.brick_green, 130, 470)
        # Label
        self.brick_green_number = GLabel('X ' + str(self.score_brick_green))
        self.brick_green_number.color = 'white'
        self.brick_green_number.font = '-14'
        self.window.add(self.brick_green_number, 180, 490)
        # Blue brick
        self.brick_blue = GRect(self.brick_width, self.brick_height)
        # self.brick_blue.color = 'blue'
        self.brick_blue.filled = True
        self.brick_blue.fill_color = 'blue'
        self.window.add(self.brick_blue, 240, 470)
        # Label
        self.brick_blue_number = GLabel('X ' + str(self.score_brick_blue))
        self.brick_blue_number.color = 'white'
        self.brick_blue_number.font = '-14'
        self.window.add(self.brick_blue_number, 290, 490)
        # Total bricks
        self.brick_total_number = GLabel('You get ' + str(self.score_brick_red + self.score_brick_orange +
                                                         self.score_brick_yellow + self.score_brick_green +
                                                         self.score_brick_blue) + ' bricks')
        self.brick_total_number.color = 'white'
        self.brick_total_number.font = '-20'
        self.window.add(self.brick_total_number, (self.window.width - self.brick_total_number.width)/2, 540)

    # Level 5 - Flash ball
    def set_flash(self):
        if self.score > 200:
            # Set level label
            self.window.remove(self.level4)
            self.level5_hit += 1
            if self.level5_hit == 1:
                self.window.add(self.level5, (self.window.width - self.level5.width) / 2, 625)
            # Flash ball
            if self.window.width/5 < self.ball.x < self.window.width/5*2 or \
                self.window.width/5*3 < self.ball.x < self.window.width/5*4:
                self.ball.color = 'black'
                self.ball.fill_color = 'black'
            else:
                self.ball.color = 'white'

    def speed_up(self):
        self.__dx *= 1.1
        self.__dy *= 1.1

    # Getter
    # You can see but you cannot change
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy