import sys

from pygame import *
from ball import *
from difficulty import *
from paddle import *

import time

pygame.init()

# Setup display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Set variables
FPS = 60
TARGET_FPS = 60

BG_COLOR = (0, 0, 0)

PADDLE_GAP = 50
PLAYER_PADDLE_SPEED = 7
COMPUTER_PADDLE_SPEED = 5

INITIAL_BALL_SPEED = 7
BALL_SIZE = 10

DIFFICULTY = Difficulty.IMPOSSIBLE

font = pygame.font.Font("freesansbold.ttf", 32)

# Initialize objects
ball = Ball(Vector2(PADDLE_GAP + BALL_SIZE + 10, 50), Vector2(1, 0.5), INITIAL_BALL_SPEED, BALL_SIZE, DISPLAY,
            PADDLE_GAP)

paddle_player = Player(Vector2(PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 150, DISPLAY)
paddle_computer = Computer(Vector2(SCREEN_WIDTH - PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 150, DISPLAY,
                           COMPUTER_PADDLE_SPEED, DIFFICULTY)

paddles = [paddle_player, paddle_computer]


def mainloop():
    up = False
    down = False

    # Delta time
    clock = pygame.time.Clock()
    prev_time = time.time()

    while True:

        # Set window title and scoreboard
        pygame.display.set_caption("pong - speed | {}".format(ball.speed))
        text = font.render("{} - {}".format(paddle_player.score, paddle_computer.score), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH / 2, 20)

        # Calc delta time
        clock.tick(FPS)
        now = time.time()
        dt = now - prev_time
        prev_time = now

        for e in pygame.event.get():

            if e.type == KEYDOWN:
                if e.key == K_w:
                    down = False
                    up = True

                if e.key == K_s:
                    up = False
                    down = True

                if e.key == K_F11:
                    pygame.display.toggle_fullscreen()

            if e.type == KEYUP:
                if e.key == K_w:
                    up = False

                if e.key == K_s:
                    down = False

            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        if up:
            paddle_player.move((0, -PLAYER_PADDLE_SPEED * dt * TARGET_FPS))

        if down:
            paddle_player.move((0, PLAYER_PADDLE_SPEED * dt * TARGET_FPS))

        DISPLAY.fill(BG_COLOR)
        DISPLAY.blit(text, text_rect)

        paddle_player.update()
        paddle_computer.update(ball, dt * TARGET_FPS)

        ball.update(paddles, dt * TARGET_FPS)

        pygame.display.update()


if __name__ == "__main__":
    mainloop()
