import pygame


class Ball:
    def __init__(self, position, direction, velocity, size):
        self.position = position
        self.direction = direction
        self.velocity = velocity
        self.size = size

    def update(self, display):
        self.check_collisions()
        self.move()
        self.draw(display)

    def move(self):
        self.position += self.direction

    def draw(self, display):
        pygame.draw.circle(display, (255, 255, 255), self.position, self.size)

    def check_collisions(self):
        next_x = self.position.x + self.direction.x
        next_y = self.position.y + self.direction.y

        if next_x > 500:
            self.direction.x = -self.direction.x

        if next_x < 0:
            self.direction.x = abs(self.direction.x)

        if next_y > 500:
            self.direction.y = -self.direction.y

        if next_y < 0:
            self.direction.y = abs(self.direction.y)
