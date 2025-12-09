# ---------- Constants ----------
CELL_SIZE = 6  # size of each block cell (pixel width & height)
BLOCK_COLOR = (243,216,63)  # colour of the obstical

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        # originally left as None -> nothing to draw
        self.image = None  
        # rect not defined, pygame can't blit this sprite
        # self.rect = None


    [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],

class Obstacle:
    def __init__(self, x, y):
        self.blocks_group = pygame.sprite.Group()
        # looping by index in a way that fails for empty rows
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    pos_x = x + column * 3
                    pos_y = y + row * 3
                    block = Block(pos_x, pos_y)
                    self.blocks_group.add(block)
