import pygame

pygame.init()

HIGHT, WEIGHT = 600, 700
window = pygame.display.set_mode((WEIGHT, HIGHT))

play = True
while play:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            play = False


pygame.quit()