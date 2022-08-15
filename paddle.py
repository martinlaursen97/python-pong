import pygame


class Paddle:
    def __init__(self, position, width, height, display):
        self.position = position
        self.width = width
        self.height = height
        self.display = display

    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.rect(
            self.display, (255, 255, 255),
            pygame.Rect(self.position.x - self.width/2, self.position.y - self.height/2, self.width, self.height)
        )


class Player(Paddle):

    def move(self, shift):
        self.position += shift


class Computer(Paddle):

    def move(self):
        pass
