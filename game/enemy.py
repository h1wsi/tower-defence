import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, image):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def move(self):
        self.rect.x += 1

    def update(self):
        self.move()