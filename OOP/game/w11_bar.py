import pygame

class Bar:
    def __init__(self,screen, x, y, width, height, color, step):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.step = step

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x -= self.step

    def move_right(self):
        self.x += self.step