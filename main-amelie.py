import pygame, sys
from alien import Alien
import numpy as np

class Game:
    def __init__(self):
        #Alien Setup
        self.aliens = pygame.sprite.Group()
        self.alien_grid(rows=6, cols=8)

    def run(self):
        #Aliens Run Code
        self.aliens.update()
        self.aliens.draw(screen)
    
    def alien_grid(self, rows, cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 100):
        row_indices = np.repeat(np.arange(rows), cols)
        col_indices = np.tile(np.arange(cols), rows)

        x_positions = col_indices * x_distance + x_offset
        y_positions = row_indices * y_distance + y_offset

        for i in range(len(x_positions)):
            row = row_indices[i]
            x = x_positions[i]
            y = y_positions[i]

            if row == 0: color = 'yellow'
            elif 1 <= row <= 2: color = 'green'
            else: color = 'red'

            alien_sprite = Alien(color, x, y)
            self.aliens.add(alien_sprite)





if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()
        pygame.display.flip()
        clock.tick(60)