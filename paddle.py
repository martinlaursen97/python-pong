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
    pass


class Computer(Paddle):
    pass
