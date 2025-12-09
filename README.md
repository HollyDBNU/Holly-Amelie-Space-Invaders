# Holly-Amelie-Space-Invaders

import pygame, sys from alien import Alien from laser import Laser from random import choice

class Game: def init(self): #Alien Setup self.aliens = pygame.sprite.Group() self.alien_grid(rows = 6, cols = 8) self.alien_direction = 1

#Alien Lasers
self.alien_lasers = pygame.sprite.Group()
def run(self): #Aliens Run Code self.aliens.update(self.alien_direction) self.alien_finder() self.aliens.draw(screen)

#Lasers Run Code
self.alien_lasers.update()
self.alien_lasers.draw(screen)
#Alien Grid Setup def alien_grid(self, rows, cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 100): #Arranging the Aliens in Rows and Columns for row_index, row in enumerate(range(rows)): for col_index, col in enumerate(range(cols)): x = col_index * x_distance + x_offset y = row_index * y_distance + y_offset

    #Colour Coding the Aliens
    if row_index == 0: alien_sprite = Alien('yellow', x, y)
    elif 1 <= row_index <=2: alien_sprite = Alien('green', x, y)
    else: alien_sprite = Alien('red', x, y)
    self.aliens.add(alien_sprite)
def alien_finder(self): all_aliens = self.aliens.sprites() for alien in all_aliens: if alien.rect.right >= screen_width: self.alien_direction = -1 self.alien_down(2) elif alien.rect.left <= 0: self.alien_direction = 1 self.alien_down(2)

def alien_down(self, distance): if self.aliens: for alien in self.aliens.sprite(): alien.rect.y += distance

def alien_shoot(self): if self.aliens: random_alien = choice(self.aliens.sprites()) laser_sprite = Laser(random_alien.rect.center, 6, screen_height) self.alien_lasers.add(laser_sprite)

if name == 'main': pygame.init() screen_width = 600 screen_height = 600 screen = pygame.display.set_mode((screen_width, screen_height)) clock = pygame.time.Clock() game = Game()

ALIENLASER = pygaame.USEREVENT + 1
pygame.time.set_timer(ALIENLASER, 800)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((30,30,30))
    game.run()

    pygame.display.flip()
    clock.tick(60)
