"""
File: breakout_extensions.py
Name: James Chung
----------------------------
This project is a breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program runs to eliminate the bricks by a ball rebounding from a paddle many times.
    """
    graphics = BreakoutGraphics(paddle_width = 150, turns = NUM_LIVES)
    # Add animation loop here!
    turns = graphics.nturns
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.set_flash()
        graphics.ball_hit_boundary() # Only top, left and right edge
        if graphics.ball.y + graphics.ball_radius*2 >= graphics.window.height:
            turns -= 1
            graphics.turns.text = 'Nturns: ' + str(turns)
            if turns > 0:
                graphics.reset_ball()
            else:
                graphics.set_gameover()
                break
        graphics.check_for_collisions()
        graphics.check_brick_or_paddle()
        if graphics.score == 300:
            graphics.set_you_win()
            break

if __name__ == '__main__':
    main()
