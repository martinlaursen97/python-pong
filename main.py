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
PLAYER_PADDLE_SPEED = 10
COMPUTER_PADDLE_SPEED = 5

INITIAL_BALL_VELOCITY = 5

ball = Ball(Vector2(500, SCREEN_WIDTH / 2), Vector2(-1, 0), INITIAL_BALL_VELOCITY, 10, DISPLAY)
paddle_player = Player(Vector2(PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 200, DISPLAY)
paddle_computer = Computer(Vector2(SCREEN_WIDTH - PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 200, DISPLAY,
                           COMPUTER_PADDLE_SPEED)

paddles = [paddle_player, paddle_computer]

font = pygame.font.Font("freesansbold.ttf", 32)


def mainloop():
    while True:
        text = font.render("{} - {}".format(paddle_player.score, paddle_computer.score), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH / 2, 20)

        for e in pygame.event.get():
            _key = pygame.key.get_pressed()

            if _key[K_s]:
                paddle_player.move((0, PLAYER_PADDLE_SPEED))

            if _key[K_w]:
                paddle_player.move((0, -PLAYER_PADDLE_SPEED))

            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)
        DISPLAY.blit(text, text_rect)

        ball.update(paddles)
        paddle_player.update()
        paddle_computer.update(ball)

        pygame.display.update()
        pygame.time.delay(10)


if __name__ == "__main__":
    mainloop()
