import pygame
from fruit import Fruit
from catcher import *

pygame.init()
bounds = (300, 300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Catch Fruit")

block_size = 20
catcher = Catcher(block_size, bounds)
fruit = Fruit(block_size, bounds)

font = pygame.font.SysFont('comicsans', 60, True)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        catcher.move(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
        catcher.move(Direction.RIGHT)

    fruit.move()

    if fruit.check_bounds() == True:
        text = font.render('Game Over', True, (255, 255, 255))
        window.blit(text, (20, 120))
        pygame.display.update()
        pygame.time.delay(1000)
        fruit.respawn()

    window.fill((0, 0, 0))
    fruit.draw(pygame, window)
    catcher.draw(pygame, window)
    pygame.display.update()
