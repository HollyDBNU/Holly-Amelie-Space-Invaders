# Space_Invaders_Python

import pygame, sys
from alien import Alien
from laser import Laser
from random import choice
from alien import MysteryShip

alien_rows = 6
alien_cols = 8
alien_timer = 800

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

class Game:
  def __init__(self, screen, screen_width, screen_height):
    #Screen Setup
    self.screen = screen
    self.screen_width = screen_width
    self.screen_height = screen_height
    #Alien Setup
    self.aliens = pygame.sprite.Group()
    self.alien_grid(rows = alien_rows, cols = alien_cols)
    self.alien_direction = 1 
    self.alien_speed = 1
    self.previous_alien_count = len(self.aliens.sprites())
    self.mystery_ship_group = pygame.sprite.GroupSingle()
  
    #Alien Lasers
    self.alien_lasers = pygame.sprite.Group()

  def run(self):
    #Aliens Run Code
    self.aliens.update(self.alien_direction * self.alien_speed)
    self.alien_finder()
    self.aliens.draw(self.screen)
    self.check_alien_speed_up() 

    #Lasers Run Code
    self.alien_lasers.update()
    self.alien_lasers.draw(self.screen)

  #Alien Grid Setup
  def alien_grid(self, rows, cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 100):
    #Arranging the Aliens in Rows and Columns
    for row in range(rows):
      for col in range(cols):
        x = col * x_distance + x_offset
        y = row * y_distance + y_offset

        
        #Colour Coding the Aliens
        if row == 0: alien_sprite = Alien('yellow', x, y)
        elif 1 <= row <=2: alien_sprite = Alien('green', x, y)
        else: alien_sprite = Alien('red', x, y)
        self.aliens.add(alien_sprite)

  def alien_finder(self):
    all_aliens = self.aliens.sprites()

    #Alien Directional Changes
    for alien in all_aliens:
      if alien.rect.right >= screen_width:
        self.alien_direction = -1
        self.alien_down(2)
      elif alien.rect.left <= 0:
        self.alien_direction = 1
        self.alien_down(2)

  def alien_down(self, distance):
    #Moves the aliens down
    if self.aliens:
      for alien in self.aliens.sprites():
        alien.rect.y += distance

  def check_alien_speed_up(self):
    #Speeds up aliens when killed
    alien_count = len(self.aliens.sprites())

    if alien_count < self.previous_alien_count:
      self.alien_speed += 0.05

    self.previous_alien_count = alien_count

  def alien_shoot(self):
    #Alien Shooting Mechanics
    if self.aliens:
      random_alien = choice(self.aliens.sprites())
      laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
      self.alien_lasers.add(laser_sprite)

  def create_mystery_ship(self):
		self.mystery_ship_group.add(MysteryShip(self.screen_width, self.offset))

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    game = Game(screen, screen_width, screen_height)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == ALIENLASER:
              game.alien_shoot()

            if event.type == MYSTERYSHIP and game.run:
                game.create_mystery_ship()
                pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))
            
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE and game.aliens:
                random_alien = choice(game.aliens.sprites())
                random_alien.kill()
        
        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)
