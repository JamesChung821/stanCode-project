"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
File: breakout.py
Name: James Chung
---------------------
This project is a breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program runs to eliminate the bricks by a ball rebounding from a paddle many times.
    """
    graphics = BreakoutGraphics()
    # Add animation loop here!
    turns = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.ball_hit_boundary() # Only top, left and right edge
        if graphics.ball.y + graphics.ball_radius*2 >= graphics.window.height:
            turns -= 1
            if turns > 0:
                graphics.reset_ball()
            else:
                break
        graphics.check_for_collisions()
        graphics.check_brick_or_paddle()
        if graphics.remove_bricks == 100:
            break







if __name__ == '__main__':
    main()
