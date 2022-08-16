import random

import pygame


class Ball:
    def __init__(self, position, direction, velocity, size, display, paddle_gap):
        self.position = position
        self.direction = direction
        self.velocity = velocity

        self.initial_velocity = velocity

        self.size = size
        self.display = display
        self.shooting_angle = 80
        self.PADDLE_GAP = paddle_gap

        self.set_trajectory_pos()

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

                    left_side = self.position.x < self.display.get_width() / 2

                    if left_side:
                        temp_shifted_paddle_pos.x -= self.shooting_angle
                    else:
                        temp_shifted_paddle_pos.x += self.shooting_angle

                    new_dir = (self.position - temp_shifted_paddle_pos).normalize()
                    self.direction = new_dir

                    self.move(next_x, next_y)
                    if left_side:
                        self.set_trajectory_pos()
                    else:
                        self.reset_trajectory_pos()
                    return

            if self.collides_with_right_wall(next_x):
                paddles[0].score += 1
                self.reset_ball()
                self.reset_trajectory_pos()
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

    def reset_trajectory_pos(self):
        self.trajectory_pos.x = self.PADDLE_GAP + self.size / 2
        self.trajectory_pos.y = self.display.get_height() / 2

    def set_trajectory_pos(self):
        x_paddle_plane = self.display.get_width() - (self.PADDLE_GAP + self.size / 2)
        dir_norm = self.direction.normalize()
        temp_trajectory_pos = pygame.Vector2(self.position.x, self.position.y)

        while temp_trajectory_pos.x <= x_paddle_plane:
            if self.collides_with_floor(temp_trajectory_pos.y):
                dir_norm.y = -abs(dir_norm.y)
            elif self.collides_with_roof(temp_trajectory_pos.y):
                dir_norm.y = abs(dir_norm.y)

            temp_trajectory_pos += dir_norm

        self.trajectory_pos = temp_trajectory_pos

    def collides_with_paddle(self, paddle, next_x, next_y):
        within_x_plane = paddle.position.x - paddle.width / 2 <= next_x <= paddle.position.x + paddle.width / 2
        within_y_plane = paddle.position.y - paddle.height / 2 <= next_y <= paddle.position.y + paddle.height / 2
        return within_x_plane and within_y_plane

    def collides_with_roof(self, next_y):
        return next_y < self.size

    def collides_with_floor(self, next_y):
        return next_y > self.display.get_height() - self.size

    def collides_with_left_wall(self, next_x):

        return next_x <= self.size

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

        if n == 0:
            self.set_trajectory_pos()
