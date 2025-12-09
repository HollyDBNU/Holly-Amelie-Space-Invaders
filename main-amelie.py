import pygame, sys
from alien import Alien

class Game:
    def __init__(self):
        #Alien Setup
        self.aliens = pygame.sprite.Group()

    def run(self):
        #Aliens Run Code
        self.aliens.draw(screen)
        alien_sprite = Alien('red', 150, 150)
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