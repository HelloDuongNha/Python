import pygame
from w11_bar import Bar
from w11_ball import Ball
import random as rd

class CatchingGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Catching Game")
        self.game_speed = pygame.time.Clock()
        self.bg_color = (255, 255, 255)
        self.bar = self.create_bar()
        self.ball = self.reset_ball()
        self.score = 0


    def create_bar(self):
        # set bar at the bottom at the screen, in the center
        width = 100
        height = 20
        pad_y = 10
        x = self.screen.get_width() // 2 - width // 2
        y = self.screen.get_height() - height - pad_y
        color = (0, 0, 255)
        step = 10
        return Bar(self.screen, x, y, width, height, color, step)
    
    def reset_ball(self):
        radius = 20
        x = rd.randint(0, self.screen.get_width() - radius)
        y = radius
        color = (rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
        step = 10
        return Ball(self.screen, x, y, radius, color, step)
    
    def is_collie(self):
        collie_top_left = self.ball.x + self.ball.y >= self.bar.x and self.ball.y + self.ball.radius >= self.bar.y
        collie_top_right = self.ball.x - self.ball.radius <= self.bar.x + self.bar.width and self.ball.y + self.ball.radius >= self.bar.y
        collie_bottom_left = self.ball.x + self.ball.radius >= self.bar.x and self.ball.y - self.ball.radius <= self.bar.y + self.bar.height
        collie_bottom_right = self.ball.x - self.ball.radius <= self.bar.x + self.bar.width and self.ball.y - self.ball.radius <= self.bar.y + self.bar.height

        return collie_top_left and collie_top_right and collie_bottom_left and collie_bottom_right

    def is_bottom(self):
        return self.ball.y + self.ball.radius >= self.screen.get_height()
    
    def run(self):
        running = True
        center_x = 400
        center_y = 300
        while running:
            # check game event
            for event in pygame.event.get():
                # handle event (close window)
                if event.type == pygame.QUIT:
                    running = False
                
            # handle key pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.bar.move_left()
            elif keys[pygame.K_RIGHT]:
                self.bar.move_right()

            # update ball position
            self.ball.move()
            # check ball collide with bar
            if self.is_collie():
                self.ball = self.reset_ball()
                self.score += 1
                if self.score == 5:
                    running = False
            if self.is_bottom():
                running = False
                return
            
            # clear screen
            self.screen.fill(self.bg_color)
            # draw bar at new position
            self.bar.draw()
            self.ball.draw()
            # update display
            pygame.display.flip()
            # control game speed
            self.game_speed.tick(30)
        pygame.quit()

if __name__ == "__main__":
    game = CatchingGame()
    game.run()
