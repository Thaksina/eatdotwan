import arcade.key
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
DIR_CENTER = 5

DIR_OFFSET = {DIR_UP: (0, 1),
              DIR_RIGHT: (1, 0),
              DIR_DOWN: (0, -1),
              DIR_LEFT: (-1, 0),
              DIR_CENTER: (0,0)}

class Pom:
    BLOCK_SIZE = 5
    
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = DIR_CENTER

    def update(self,k):
        if self.x>self.world.width:
            self.x=0

        self.x += DIR_OFFSET[self.direction][0]*self.BLOCK_SIZE
        self.y += DIR_OFFSET[self.direction][1]*self.BLOCK_SIZE

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.pom = Pom(self,width//2,height//2)

    def update(self,k):
        self.pom.update(k)

    def on_key_press(self, key, key_modifiers):
        if arcade.key.UP == key:
            self.pom.direction = DIR_UP

        elif arcade.key.DOWN == key:
            self.pom.direction = DIR_DOWN

        elif arcade.key.LEFT == key:
            self.pom.direction = DIR_LEFT

        elif arcade.key.RIGHT == key:
            self.pom.direction = DIR_RIGHT

