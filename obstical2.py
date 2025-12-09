import pygame

# ---------- Constants ----------
CELL_SIZE = 6  # size of each block cell (pixel width & height)
BLOCK_COLOR = (243,216,63)  # colour of the obstical

# ---------- Block Sprite (single obstacle cell) ----------
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # create a Surface so Pygame can render the block
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill((243, 216, 63))  # colour
        # set rect for positioning and collision
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
