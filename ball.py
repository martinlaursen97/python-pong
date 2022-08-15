import pygame


class Ball:
    def __init__(self, position, direction, velocity, size, display):
        self.position = position
        self.direction = direction.normalize() * velocity
        self.velocity = velocity
        self.size = size
        self.display = display

    def update(self):
        self.check_collisions()
        self.draw()

    def move(self, next_x, next_y):
        self.position.x = next_x
        self.position.y = next_y

    def draw(self):
        pygame.draw.circle(self.display, (255, 255, 255), self.position, self.size)

    def check_collisions(self):

        dir_norm = self.direction.normalize()
        next_x = self.position.x
        next_y = self.position.y

        # check for collision between current and next position
        for i in range(self.velocity):

            next_x += dir_norm.x
            next_y += dir_norm.y

            if next_x >= self.display.get_width() - self.size:
                self.direction.x = -self.direction.x
                break

            elif next_x <= 0 + self.size:
                self.direction.x = abs(self.direction.x)
                break

            elif next_y > self.display.get_height() - self.size:
                self.direction.y = -self.direction.y
                break

            elif next_y < 0 + self.size:
                self.direction.y = abs(self.direction.y)
                break

        self.move(next_x, next_y)
