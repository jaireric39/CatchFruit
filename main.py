import pygame
from fruit import Fruit
from catcher import *


def main():
    pygame.init()
    bounds = (300, 300)
    window = pygame.display.set_mode(bounds)
    pygame.display.set_caption("Catch Fruit")

    block_size = 20
    catcher = Catcher(block_size, bounds)
    fruit = Fruit(block_size, bounds)

    font = pygame.font.SysFont('arial', 40, True)
    font2 = pygame.font.SysFont('arial', 35, True)

    titleText = font2.render('Click to start', True, (255, 255, 255))
    showTitle(titleText, window)

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
        catcher.check_for_fruit(fruit)
        if fruit.check_bounds() == True:
            text = font.render('Game Over', True, (255, 255, 255))
            text2 = font.render('Score: ' + str(catcher.score), True,
                                (255, 255, 255))
            window.blit(text, (20, 120))
            window.blit(text2, (40, 180))
            pygame.display.update()
            pygame.time.delay(2500)
            showTitle(titleText, window)
            fruit.reset()
            catcher.reset()

        window.fill((0, 0, 0))
        fruit.draw(pygame, window)
        catcher.draw(pygame, window)
        pygame.display.update()


def showTitle(titleText, window):
    window.fill((0, 0, 0))
    window.blit(titleText, (15, 120))
    pygame.display.update()

    title = True
    while title:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                title = False


main()
