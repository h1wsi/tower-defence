import pygame
from enemy import Enemy

pygame.init()

# настройки игровой панели
HIGHT, WEIGHT = 600, 700
FPS = 60
walking_points = [(100, 100), (500, 300), (500, 200), (300, 400)]

window = pygame.display.set_mode((WEIGHT, HIGHT))
clock = pygame.time.Clock()

# изображения
enemy_img = pygame.image.load("src/tank.png").convert_alpha()

# группы
enemy_grp = pygame.sprite.Group()

# персонажи
enemy = Enemy(walking_points, enemy_img)
enemy_grp.add(enemy)


play = True
while play:

    window.fill("white")
    
    # движение вражеского персонажа
    pygame.draw.lines(window, "black", False, walking_points)

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