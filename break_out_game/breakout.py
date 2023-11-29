"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program plays a Python game 'breakout'.
In the window, there are three elements: bricks, a ball, and a paddle.
The player uses the mouse to control the paddle's position
and rebounds the falling ball to eliminate all bricks.
The ball will rebound when it hits any object except the bottom boundary of the window.
There are two conditions for terminating the game:
1. The player eliminates all the bricks in the window.
2. When the ball exceeds the bottom boundary of the window three times, game over!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 100  # 100 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    This program executes breakout game.
    The game terminates when all bricks are removed or
    ball falls out of the bottom of the window NUM_LIVES times.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if graphics.switch:  # 點擊畫面才會啟動，加這條才能讓滑鼠事件不受 lives 影響（即使沒命了，玩家還是可以移動 paddle）

            vx = graphics.get_vx()
            vy = graphics.get_vy()
            # Update
            graphics.ball.move(vx, vy)

            # Check for boundary collisions and check what object the ball hits to
            # 原本把 reset_ball() 寫在 check_for_boundary() 裡，這樣每次墜落到最底下就會返回起始點，
            # 導致進不到 if graphics.ball.y + graphics.ball.height >= graphics.window.height 這個條件，就不會 lives -= 1
            graphics.check_for_boundary()
            graphics.check_for_collision()

            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                print('Remaining live(s): ' + str(lives))
            if lives == 0 or graphics.all_bricks_removed():
                break

        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
