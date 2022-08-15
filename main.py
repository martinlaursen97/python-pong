import sys
from pygame import *
from ball import *
from paddle import *

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

BG_COLOR = (0, 0, 0)

ball = Ball(Vector2(10, 10), Vector2(12, 10), 12, 10)
paddle_1 = Paddle(Vector2(30, 250), 10, 50)


def main():
    while True:

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)

        ball.update(DISPLAY)
        paddle_1.update(DISPLAY)


        pygame.display.update()
        pygame.time.delay(100)


if __name__ == "__main__":
    main()
