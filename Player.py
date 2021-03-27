import pygame
from math import degrees, atan2, radians, cos, sin
from misc import distance


class Player:

    def __init__(self, center):
        surface = pygame.Surface((20, 22))
        surface.fill((1, 1, 1))
        pygame.draw.lines(surface, (0, 0, 255), 1, [[0, 0], [0, 20], [20, 10]], 2)
        pygame.draw.rect(surface, (0, 255, 0), [18, 10, 2, 2], 1)
        self.originalImage = surface
        self.toDraw = surface.copy()
        self.originalImage.set_colorkey((255, 255, 255))
        self.toDraw.set_colorkey((255, 255, 255))
        self.rectangle = self.originalImage.get_rect(center=center)
        self.angle = 0
        self.maxHealth = 150
        self.currentHealth = self.maxHealth
        self.hitBox = pygame.mask.from_surface(self.originalImage)
        self.speed = 6.0
        self.fireCoolDown = 0
        self.fireCoolDownMax = 12

    def getAngle(self):
        return self.angle

    def xComp(self, speed):
        return speed * cos(radians(self.angle))

    def yComp(self, speed):
        return speed * sin(radians(self.angle))

    def update(self, notPaused, playerCenter):

        if notPaused and distance([self.rectangle[0], self.rectangle[1]], pygame.mouse.get_pos()) > 25:
            self.calculateAngle(pygame.mouse.get_pos())
        self.toDraw = pygame.transform.rotate(self.originalImage, 180+self.angle)
        self.rectangle = self.toDraw.get_rect(center=playerCenter)
        self.hitBox = pygame.mask.from_surface(self.toDraw)
        if self.rectangle[0] > 640:
            self.rectangle[0] = 0
        if self.rectangle[0] < 0:
            self.rectangle[0] = 640
        if self.rectangle[1] > 640:
            self.rectangle[1] = 0
        if self.rectangle[1] < 0:
            self.rectangle[1] = 640
        if self.fireCoolDown >= self.fireCoolDownMax:
            fireThisFrame = True
            self.fireCoolDown = 0
        else:
            fireThisFrame = False
            self.fireCoolDown += 1
        return [self.toDraw, self.rectangle, fireThisFrame]

    def calculateAngle(self, point):
        x = self.rectangle[0] - point[0]
        y = self.rectangle[1] - point[1]
        self.angle = 360 - degrees(atan2(float(radians(y)), float(radians(x))))
