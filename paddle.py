import pygame


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

    def move(self, translation):
        next_pos = self.position + translation

        if next_pos.y + self.height / 2 >= self.display.get_height():
            self.position.y = self.display.get_height() - self.height / 2
        elif next_pos.y - self.height / 2 <= 0:
            self.position.y = self.height / 2
        else:
            self.position += translation


class Player(Paddle):
    def update(self):
        self.draw()


class Computer(Paddle):
    def __init__(self, position, width, height, display, paddle_speed, difficulty):
        super().__init__(position, width, height, display)
        self.paddle_speed = paddle_speed
        self.DIFFICULTY = difficulty

    def update(self, ball):
        self.draw()
        if self.DIFFICULTY.HARD:
            self.track_ball_trajectory(ball.trajectory_pos)
        else:
            self.track_ball(ball.position)

    def track_ball(self, ball_position):
        if self.position.y > ball_position.y:
            self.move((0, -self.paddle_speed))
        else:
            self.move((0, self.paddle_speed))

    def track_ball_trajectory(self, ball_trajectory_pos):
        pass

