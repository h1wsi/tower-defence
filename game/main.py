import pygame
from enemy import Enemy

pygame.init()

# screen
HIGHT, WEIGHT = 600, 700
FPS = 60

window = pygame.display.set_mode((WEIGHT, HIGHT))
clock = pygame.time.Clock()

# images
enemy_img = pygame.image.load("src/troll.png").convert_alpha()

# groups
enemy_grp = pygame.sprite.Group()

# characters
enemy = Enemy((200, 300), enemy_img)
enemy_grp.add(enemy)


play = True
while play:

    window.fill("white")

    enemy_grp.update()
    enemy_grp.draw(window)

    for enemy in enemy_grp:
        enemy.move()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            play = False

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()