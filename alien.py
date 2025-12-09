import pygame

# Alien Sprite
class Alien(pygame.sprite.Sprite):
    # Alien Setup
	def __init__(self,color,x,y):
        super().__init__()
        file_path = 'Graphics/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

        if color == 'red' : self.value = 100
        elif color == 'green' : self.value = 200
        else: self.value = 300
# Alien Movement Update
    def update(self, direction):
        self.rect.x += direction
# Mystery Ship Sprite (spawns from a random side and moves across screen)
class MysteryShip(pygame.sprite.Sprite):
	def __init__(self, screen_width, offset):
		super().__init__()
		self.screen_width = screen_width
		self.offset = offset
		self.image = pygame.image.load("mystery.png")

		x = random.choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])
		if x == self.offset/2:
			self.speed = 3
		else:
			self.speed = -3

		self.rect = self.image.get_rect(topleft = (x, 90))
# Mystery Ship Movement & Auto-Despawn
	def update(self):
		self.rect.x += self.speed
		if self.rect.right > self.screen_width + self.offset/2:
			self.kill()
		elif self.rect.left < self.offset/2:
			self.kill()
