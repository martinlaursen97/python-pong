import sys

from pygame import *

from ball import *

pygame.init()

DISPLAY = pygame.display.set_mode((500, 500), 0, 32)

BG_COLOR = (0, 0, 0)

ball = Ball(Vector2(10, 10), Vector2(1, 0), 5, 10)


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


main()
