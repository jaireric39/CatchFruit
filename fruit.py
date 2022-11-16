import random


class Fruit:
    block_size = None
    color = (0, 255, 0)
    x = 0
    y = 0
    speed = 10
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, window):
        game.draw.circle(window, self.color, (self.x, self.y),
                         self.block_size / 2)

    def respawn(self):
        self.speed += 1
        blocks_in_x = (self.bounds[0]) / self.block_size
        self.x = random.randint(
            0, blocks_in_x - 1) * self.block_size + self.block_size / 2
        self.y = 0

    def reset(self):
        self.speed = 9
        self.respawn()

    def move(self):
        self.y += self.speed

    #true = out of bounds
    def check_bounds(self):
        if self.y >= self.bounds[0]:
            return True

        return False
