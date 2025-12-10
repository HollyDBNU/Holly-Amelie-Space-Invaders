import pygame, sys, random

pygame.init()

 # Mystery Ship Appearance and Timer
 MYSTERYSHIP = pygame.USEREVENT + 2
 pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

# --- Background Music --- Ensure to add to main game, above requirments
pygame.mixer.music.load("Graphics/music.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

  #---------- Obstacle Grid Definition ----------# ADD to Main - Requirment

# Constants for Obstacles
CELL_SIZE = 6# size of each block cell (pixel width & height)
BLOCK_COLOR = (243,216,63)  # colour of the obstical

# ---------- Block Sprite (single obstacle cell) ----------
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill((0,255,0))  # colour
        self.rect = self.image.get_rect(topleft=(x, y))

# ---------- Define the Grid ----------#
grid = [
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]]

class Obstacle:
	def __init__(self, x, y):
		self.blocks_group = pygame.sprite.Group()
		for row in range(len(grid)):
			for column in range(len(grid[0])):
				if grid[row][column] == 1:
					pos_x = x + column * 3
					pos_y = y + row * 3
					block = Block(pos_x, pos_y)
					self.blocks_group.add(block)


# Creates obstacles at specified positions
def create_obstacles(num=4, top_y=420):
    obstacles = []
    blocks_group = pygame.sprite.Group()
    margin = 80
    usable_width = SCREEN_WIDTH - 2 * margin
    spacing_between = usable_width // (num - 1) if num > 1 else 0

    for i in range(num):
        x = margin - 20 + i * spacing_between
        y = top_y
        obs = Obstacle(x, y)
        obstacles.append(obs)
        for b in obs.blocks_group:
            blocks_group.add(b)

    return obstacles, blocks_group


#---------- Lazer section ----------# ADD to Main - Requirment


# Laser class for player lasers 
class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill((243, 216, 63))
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0 or self.rect.y > self.screen_height + 15:
            self.kill()


#---------- Spaceship ----------# ADD to Main - Requirment


# Spaceship (Player) class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, offset=0):
        super().__init__()

        # Loading of Yellow Spaceship Image
        try:
            self.image = pygame.image.load("Graphics/spaceship.png").convert_alpha()
        except:
            self.image = pygame.Surface((50, 30))
            self.image.fill((255, 255, 0))  # yellow fallback

        # Position of spaceship at the bottom of the screen
        self.rect = self.image.get_rect(midbottom=((screen_width + offset) // 2,
                                                   screen_height - 10))

        # Movement of the spaceship
        self.speed = 6
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset

        # Laser system
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_delay = 300
        self.laser_time = 0

        # Laser sound - Beyond my Requirment
        try:
            self.laser_sound = pygame.mixer.Sound("Graphics/laser.ogg")
        except:
            self.laser_sound = None

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, self.screen_height)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            if self.laser_sound:
                self.laser_sound.play()

    def update(self):
        self.get_input()
        self.constrain()
        self.lasers_group.update()
        self.recharge()

    def constrain(self):
        if self.rect.left < self.offset:
            self.rect.left = self.offset
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    def recharge(self):
        if not self.laser_ready:
            if pygame.time.get_ticks() - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def reset(self):
        # re-centre player
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) // 2,
                                                   self.screen_height - 10))
        self.lasers_group.empty()
        self.laser_ready = True
        self.laser_time = 0

  
#---------- Mystery Ship ----------# ADD to Main - Above Requirment


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width, y_position, speed=-3):
        super().__init__()

        try:
            self.image = pygame.image.load("Graphics/mystery.png").convert_alpha()
        except:
            self.image = pygame.Surface((60, 25))
            self.image.fill((255, 200, 50))

        self.rect = self.image.get_rect(midleft=(screen_width + 40, y_position))
        self.speed = speed
        self.screen_width = screen_width

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()

  # under class game 

class Game:
    def __init__(self, screen):
        self.screen = screen

        # Player
        self.player = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player_group = pygame.sprite.GroupSingle(self.player)

        # Explosion sound for mystery ship                                                                 
        try:
           self.explosion_sound = pygame.mixer.Sound("Graphics/explosion.ogg")
           self.explosion_sound.set_volume(1.0)
        except:
            self.explosion_sound = None

        # Mystery ship
        self.mystery_ship_group = pygame.sprite.Group()       

        # Obstacles
        self.obstacles, self.blocks_group = create_obstacles(num=4, top_y=420)

        # simple score
        self.score = 0

        # Create mystery ship                                                                                  
        def create_mystery_ship(self):
            self.mystery_ship_group.add(MysteryShip(SCREEN_WIDTH, 60))



 # under def run(self)
  def run(self):
      # update moving things
        self.player_group.update()
        self.enemy_lasers.update()
        self.mystery_ship_group.update()
        self.player.lasers_group.update()
  
        # draws everything
        self.screen.fill((30, 30, 30))
        self.blocks_group.draw(self.screen)
        self.mystery_ship_group.draw(self.screen)
        self.aliens.draw(self.screen)
        self.enemy_lasers.draw(self.screen)
        self.player_group.draw(self.screen)
        self.player.lasers_group.draw(self.screen)

        font = pygame.font.Font("Graphics/monogram.ttf", 24)
        score_surf = font.render(f"Score: {self.score}", True, (200, 200, 200))
        self.screen.blit(score_surf, (10, 10))


# Under while true:

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MYSTERYSHIP:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))























  
