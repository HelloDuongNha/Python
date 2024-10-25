import pygame

class GameDemo:
    def __init__(self):
        # init pygame
        pygame.init()
        # create game screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game Demo")
        # set game speed
        self.game_speed = pygame.time.Clock()
        # set background colour
        self.bg_color = (255, 255, 255) # white

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
                
                # handle key down event
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                center_x -= 10
            if keys[pygame.K_RIGHT]:
                center_x += 10
            if keys[pygame.K_UP]:
                center_y -= 10
            if keys[pygame.K_DOWN]:
                center_y += 10
                    
            # fill background colour
            self.screen.fill(self.bg_color)
            # draw a circle
            self.draw_circle(center_x, center_y, radius=100, color=(255, 192, 203))
            # update display
            pygame.display.flip()
            # control game speed
            self.game_speed.tick(30)
        pygame.quit()

    def draw_circle(self, center_x, center_y, radius, color):
        # draw circle on screen
        pygame.draw.circle(self.screen, color, (center_x, center_y), radius)






if __name__ == "__main__":
    game = GameDemo()
    game.run()

