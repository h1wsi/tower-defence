import pygame
from pygame.math import Vector2
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, points, image):
        
        pygame.sprite.Sprite.__init__(self)

        self.primary_image = image
        self.walking_points = points
        self.position = Vector2(self.walking_points[0])
        self.next_point = 1
        self.speed = 2
        self.corner = 0        
    
    def update(self):
        self.move()
        self.rotate()

    def move(self):
        
        if self.next_point < len(self.walking_points):
            self.trgt = Vector2(self.walking_points[self.next_point])
            self.movement = self.trgt - self.position
        else:
            self.kill()

        distance = self.movement.length()
        if distance >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.position += self.movement.normalize() * distance
            self.next_point += 1
        # self.rect.center = self.position

    def rotate(self):

        distance = self.trgt - self.position
        self.corner = math.degrees(math.atan2(-distance[1], distance[0]))
        
        self.image = pygame.transform.rotate(self.primary_image, self.corner)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
