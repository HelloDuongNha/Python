import pygame

class Ball:
    def __init__(self, screen, x, y, radius, color, step):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.step = step

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.step
    
