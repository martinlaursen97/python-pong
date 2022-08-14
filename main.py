import sys
from pygame import *
from ball import *

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

BG_COLOR = (0, 0, 0)

ball = Ball(Vector2(10, 10), Vector2(12, 10), 5, 10)


def main():
    while True:

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)

        ball.update(DISPLAY)

        pygame.display.update()
        pygame.time.delay(10)


if __name__ == "__main__":
    main()
