from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


class Catcher:
    score = 0
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

    def move(self, direction):
        #print(direction)
        if direction == Direction.LEFT and self.x >= self.speed:
            self.x -= self.speed
        elif direction == Direction.RIGHT and self.x < self.bounds[
                0] - self.speed:
            self.x += self.speed

    def eat(self):
        self.score += 1

    def reset(self):
        self.score = 0

    #sees if catcher is over the fruit
    def check_for_fruit(self, fruit):
        #if self.x == fruit.x and self.y == fruit.y:
        if self.x <= fruit.x and fruit.x <= self.x + self.block_size and self.y <= fruit.y and fruit.y <= self.y + self.block_size:
            self.eat()
            fruit.respawn()
