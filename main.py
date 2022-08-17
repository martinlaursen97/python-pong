import sys
from pygame import *
from ball import *
from paddle import *
from difficulty import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

BG_COLOR = (0, 0, 0)

PADDLE_GAP = 50
PLAYER_PADDLE_SPEED = 5
COMPUTER_PADDLE_SPEED = 3

INITIAL_BALL_VELOCITY = 5
BALL_SIZE = 10

DIFFICULTY = Difficulty.HARD

ball = Ball(Vector2(PADDLE_GAP + BALL_SIZE + 10, 50), Vector2(1, 0.5), INITIAL_BALL_VELOCITY, BALL_SIZE, DISPLAY,
            PADDLE_GAP)

paddle_player = Player(Vector2(PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 150, DISPLAY)
paddle_computer = Computer(Vector2(SCREEN_WIDTH - PADDLE_GAP, SCREEN_HEIGHT / 2), 20, 150, DISPLAY,
                           COMPUTER_PADDLE_SPEED, DIFFICULTY)

paddles = [paddle_player, paddle_computer]

font = pygame.font.Font("freesansbold.ttf", 32)


def mainloop():
    up = False
    down = False

    while True:
        text = font.render("{} - {}".format(paddle_player.score, paddle_computer.score), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH / 2, 20)

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
            paddle_player.move((0, -PLAYER_PADDLE_SPEED))

        if down:
            paddle_player.move((0, PLAYER_PADDLE_SPEED))

        DISPLAY.fill(BG_COLOR)
        DISPLAY.blit(text, text_rect)

        ball.update(paddles)
        paddle_player.update()
        paddle_computer.update(ball)

        pygame.display.update()
        pygame.time.delay(10)


if __name__ == "__main__":
    mainloop()
