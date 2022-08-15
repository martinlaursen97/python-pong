import pygame


class Paddle:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def update(self, display):
        self.draw(display)
        pass

    def move(self):
        pass

    def draw(self, display):
        pygame.draw.rect(
            display, (255, 255, 255), pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        )
