"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program executes breakout game. If the user click the
mouse for the 1st time each round, the game starts. If the
ball falls to the ground, lives deducts one. The game will
end if there is no more lives or bricks.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)
        self.paddle.filled = True
        self.paddle_height = self.window.height - PADDLE_OFFSET
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2,
                          x=window_width // 2 - ball_radius, y=window_height // 2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Initial velocities of the ball.
        self.__dx = 0
        self.__dy = 0

        # Draw bricks.
        brick_colors = ['red', 'red', 'orange', 'orange', 'yellow', 'yellow', 'green', 'green', 'blue', 'blue']
        for row in range(brick_rows):
            color = brick_colors[row]
            for col in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, x=col * (brick_width + brick_spacing),
                                y=brick_offset + row * (brick_height + brick_spacing))
        self.brick_count = 0    # Initial number of the bricks removed

        # Paddle animation
        onmousemoved(self.move_paddle)
        self.switch = False  # Even if no lives remaining, the user can still move the paddle

    def move_paddle(self, mouse):
        """
        This function has the paddle move with its center following the mouse.
        :param mouse: the mouse event
        :return: None
        """
        paddle_x = mouse.x - self.paddle.width / 2  # Place the mouse in the middle of the paddle
        if paddle_x <= 0:
            self.paddle.x = 0  # Ensure the paddle doesn't exceed the left side of the window
        elif paddle_x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
            # Ensure the paddle doesn't exceed the right side of the window
        else:
            self.paddle.x = paddle_x

        # Ball animation
        if onmouseclicked(self.start_game):
            self.check_for_collision()

    def start_game(self, event):
        """
        This function sets the velocity of the ball.
        :param event: the mouse event.
        :return: None
        """
        if not self.switch:
            # if self.__dy == 0:  # If the ball is not moving
            self.switch = True
            self.set_ball_velocity(random.randint(1, MAX_X_SPEED), INITIAL_Y_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx  # Randomly change the direction of the ball along the x-axis
        # else:     # If the ball is moving
        #    pass   # The ball won't be effected by repeated mouse click

    def set_ball_velocity(self, dx, dy):
        self.__dx = dx
        self.__dy = dy

    # Getter functions for ball velocity
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    # (Should put in breakout.py) Ball rebounds when hitting the boundaries of the window
    def check_for_boundary(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:  # Left of right boundaries
            self.__dx = -self.__dx  # Change ball's horizontal direction
        if self.ball.y <= 0:        # Top boundary
            self.__dy = -self.__dy  # Change ball's vertical direction

    def reset_ball(self):
        """
        This function resets the ball to its original position.
        :return: None
        """
        if self.ball.y + self.ball.height >= self.window.height:  # Bottom boundary
            # Return the ball to starting position
            self.ball.x = self.window.width / 2 - BALL_RADIUS
            self.ball.y = self.window.height / 2 - BALL_RADIUS
            self.switch = False
            # Stop the ball's movement
            self.__dy = 0
            self.__dx = 0

    def check_for_collision(self):
        """
        Detects whether the ball hits the paddle or any bricks.
        :return: None
        """
        # Simulate a bounding box around the ball for collision detection
        collisions = [self.window.get_object_at(x, y) for x, y in [(self.ball.x, self.ball.y),
                                                                   (self.ball.x + self.ball.width, self.ball.y),
                                                                   (self.ball.x, self.ball.y + self.ball.height),
                                                                   (self.ball.x + self.ball.width,
                                                                    self.ball.y + self.ball.height)]]
        paddle_collision = False
        brick_collision = None

        for self.obj in collisions:
            if self.obj == self.paddle:  # The ball hits the paddle
                paddle_collision = True
            elif self.obj != self.paddle and self.obj is not None:  # The ball collides with the brick
                brick_collision = self.obj  # = The brick that the ball collided with
                break  # Exit loop after detecting the first brick collision

        if paddle_collision:
            if self.__dy > 0:           # So that ball will not stuck in the paddle
                self.__dy = -self.__dy  # Ball rebounds if any part of the ball collides with the paddle
        if brick_collision:
            # Brick will be removed only when the ball is moving
            # Add this so that the brick will not disappear when the starting position of the ball meets the brick
            if self.__dy != 0:
                self.__dy = -self.__dy  # Ball rebounds if any part of the ball collides with the brick
                self.window.remove(brick_collision)  # Remove the brick
                self.brick_count += 1   # Plus 1 to the number of removed bricks

    def all_bricks_removed(self):
        # The number of removed bricks reaches the number of original total bricks
        if self.brick_count == BRICK_ROWS * BRICK_COLS:
            # Return the ball to starting position
            self.ball.x = self.window.width / 2 - BALL_RADIUS
            self.ball.y = self.window.height / 2 - BALL_RADIUS
            # Stop the ball's movement
            self.__dy = 0
            self.__dx = 0
