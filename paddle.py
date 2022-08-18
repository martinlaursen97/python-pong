import pygame
import difficulty


class Paddle:
    def __init__(self, position, width, height, display):
        self.position = position
        self.width = width
        self.height = height
        self.display = display
        self.score = 0

    def draw(self):
        rect = pygame.Rect(self.position.x - self.width / 2, self.position.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(self.display, (255, 255, 255), rect)

    def move(self, shift):
        next_pos = self.position + shift

        if next_pos.y + self.height / 2 >= self.display.get_height():
            self.position.y = self.display.get_height() - self.height / 2
        elif next_pos.y - self.height / 2 <= 0:
            self.position.y = self.height / 2
        else:
            self.position += shift


class Player(Paddle):
    def update(self):
        self.draw()


class Computer(Paddle):
    def __init__(self, position, width, height, display, paddle_speed, _difficulty):
        super().__init__(position, width, height, display)
        self.paddle_speed = paddle_speed
        self.DIFFICULTY = _difficulty

    def update(self, ball, dt):
        if self.DIFFICULTY == difficulty.Difficulty.HARD or difficulty.Difficulty.IMPOSSIBLE:
            self.track_ball_trajectory(ball.trajectory_pos, dt)
        else:
            self.track_ball(ball.position, dt)

        self.draw()

    def track_ball(self, ball_position, dt):
        if self.position.y > ball_position.y:
            self.move((0, -self.paddle_speed * dt))
        else:
            self.move((0, self.paddle_speed * dt))

    def track_ball_trajectory(self, ball_trajectory_pos, dt):
        if self.position.y > ball_trajectory_pos.y:
            self.move((0, -self.paddle_speed * dt))
        else:
            self.move((0, self.paddle_speed * dt))
