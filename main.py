import sys
from pygame import *
from ball import *
from paddle import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

BG_COLOR = (0, 0, 0)

PADDLE_GAP = 50
PADDLE_SPEED = 10

ball = Ball(Vector2(10, 10), Vector2(12, 10), 5, 10, DISPLAY)
paddle_player = Player(Vector2(PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 100, DISPLAY)
paddle_computer = Computer(Vector2(SCREEN_WIDTH - PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 100, DISPLAY)


def main():
    while True:

        for e in pygame.event.get():
            _key = pygame.key.get_pressed()

            if _key[K_s]:
                paddle_player.move((0, PADDLE_SPEED))

            if _key[K_w]:
                paddle_player.move((0, -PADDLE_GAP))

            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)

        ball.update()
        paddle_player.update()
        paddle_computer.update()

        pygame.display.update()
        pygame.time.delay(10)


if __name__ == "__main__":
    main()
