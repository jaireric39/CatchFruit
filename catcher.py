from enum import Enum

class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Catcher:
    block_size = None
    color = (0, 0, 255)
    x = 0
    y = 0
    bounds = None
    speed = 20

    def draw(self, game, window):
        game.draw.rect(window, self.color,
                       (self.x, self.y, self.block_size, self.block_size))

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.y = bounds[1] - block_size
        self.respawn()

    def respawn(self):
      print("hi")

    def move(self, direction):
      print(direction)
      if direction == Direction.LEFT and self.x >= self.speed:
          print("left")
          self.x -= self.speed
      elif direction == Direction.RIGHT and self.x <= self.bounds[0]:
          self.x += self.speed
          

    #def eat(self):

    # sees if the head of the snake is over the food
    #def check_for_food(self, food):
    #  head = self.body[-1]
    #  if head[0] == food.x and head[1] == food.y:
    #    self.eat()
    #    fruit.respawn()