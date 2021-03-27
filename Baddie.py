import pygame
from math import degrees, atan2, radians, cos, sin


class Enemy:
    def __init__(self, position):
        self.unAlteredImage = pygame.Surface([25, 25])
        self.unAlteredImage.fill((1, 1, 1))
        pygame.draw.rect(self.unAlteredImage, [255, 0, 0], [0, 0, 25, 25], 1)
        self.imageForDrawing = self.unAlteredImage.copy()
        self.hitBox = pygame.mask.from_surface(self.unAlteredImage)

        self.unAlteredImage.set_colorkey((0, 0, 0))
        self.imageForDrawing.set_colorkey((0, 0, 0))
        self.position = position
        self.angle = 0
        self.alive = True
        self.rectangle = self.unAlteredImage.get_rect(center=self.position)
        self.speed = 5
        self.maxHealth = 50
        self.currentHealth = 50

    def lowLevelUpdate(self, notPaused):
        self.imageForDrawing = pygame.transform.rotate(self.unAlteredImage, self.angle)
        self.hitBox = pygame.mask.from_surface(self.imageForDrawing)
        self.rectangle = self.imageForDrawing.get_rect(center=self.rectangle.center)
        if notPaused:
            self.rectangle[0] -= self.speed * float((cos(radians(float(self.angle)))))
            self.rectangle[1] += self.speed * float((sin(radians(float(self.angle)))))
        if self.rectangle[0] > 640:
            self.rectangle[0] = 0
        if self.rectangle[0] < 0:
            self.rectangle[0] = 640
        if self.rectangle[1] > 640:
            self.rectangle[1] = 0
        if self.rectangle[1] < 0:
            self.rectangle[1] = 640

        if self.currentHealth <= 0:
            self.alive = False
        return [self.imageForDrawing, self.rectangle]

    def calculateAngle(self, point):
        x = self.rectangle[0] - point[0]
        y = self.rectangle[1] - point[1]
        self.angle = 360 - degrees(atan2(float(radians(y)), float(radians(x))))
