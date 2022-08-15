import random

import pygame


class Ball:
    def __init__(self, position, direction, velocity, size, display):
        self.position = position
        self.direction = direction
        self.velocity = velocity

        self.initial_velocity = velocity

        self.size = size
        self.display = display
        self.shooting_angle = 80

    def update(self, paddles):
        self.check_collisions(paddles)
        self.draw()

    def move(self, next_x, next_y):
        self.position.x = next_x
        self.position.y = next_y

    def draw(self):
        pygame.draw.circle(self.display, (255, 255, 255), self.position, self.size)

    def check_collisions(self, paddles):

        dir_norm = self.direction.normalize()
        next_x = self.position.x
        next_y = self.position.y

        # check for collision between current and next position
        for i in range(self.velocity):

            next_x += dir_norm.x
            next_y += dir_norm.y

            for paddle in paddles:
                if self.collides_with_paddle(paddle, next_x, next_y):

                    self.velocity += 1
                    temp_shifted_paddle_pos = pygame.Vector2(paddle.position.x, paddle.position.y)

                    if self.position.x < self.display.get_width() / 2:
                        temp_shifted_paddle_pos.x -= self.shooting_angle
                    else:
                        temp_shifted_paddle_pos.x += self.shooting_angle

                    new_dir = (self.position - temp_shifted_paddle_pos).normalize()
                    self.direction = new_dir

                    self.move(next_x, next_y)
                    return

            if self.collides_with_right_wall(next_x):
                paddles[0].score += 1
                self.reset_ball()
                return

            elif self.collides_with_left_wall(next_x):
                paddles[1].score += 1
                self.reset_ball()
                return

            elif self.collides_with_floor(next_y):
                self.direction.y = -abs(self.direction.y)
                break

            elif self.collides_with_roof(next_y):
                self.direction.y = abs(self.direction.y)
                break

        self.move(next_x, next_y)

    def collides_with_paddle(self, paddle, next_x, next_y):
        within_x_plane = paddle.position.x - paddle.width / 2 <= next_x <= paddle.position.x + paddle.width / 2
        within_y_plane = paddle.position.y - paddle.height / 2 <= next_y <= paddle.position.y + paddle.height / 2
        return within_x_plane and within_y_plane

    def collides_with_roof(self, next_y):
        return next_y < 0 + self.size

    def collides_with_floor(self, next_y):
        return next_y > self.display.get_height() - self.size

    def collides_with_left_wall(self, next_x):
        return next_x <= 0 + self.size

    def collides_with_right_wall(self, next_x):
        return next_x >= self.display.get_width() - self.size

    def reset_ball(self):
        n = random.randint(0, 1)
        x_shift = -200 if n == 0 else 200
        x_dir_shift = 1 if n == 0 else -1
        y_dir_shift = 1 if n == 0 else -1
        self.position.x = self.display.get_width() / 2 + x_shift
        self.position.y = self.display.get_height() / 2
        self.direction.x = x_dir_shift
        self.direction.y = y_dir_shift
        self.velocity = self.initial_velocity
