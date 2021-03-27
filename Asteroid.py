import pygame
from math import cos, radians, sin
from misc import convexHull, dft
from random import randint


class Asteroid:
    def __init__(self, position, initialAngle):
        surface = pygame.Surface((33, 33))
        points = convexHull([(randint(0, 32), randint(0, 32)) for _ in range(30)])
        pygame.draw.polygon(surface, (255, 255, 0), points, 1)

        self.image = surface.copy()
        self.image.set_colorkey((0, 0, 0))
        self.rectangle = self.image.get_rect(center=position)
        self.originalPosition = [position[0], position[1]]
        self.hitBox = pygame.mask.from_surface(self.image)
        self.angle = initialAngle
        self.speed = 5
        self.center = [position[0], position[1]]

    def draw(self, notPaused, listOfEnemies, playerPosition, listOfOtherAsteroids, playerHitBox):
        hitThePlayer = 0
        if notPaused:
            #  Sloppy hit detection
            hitDetectionCoordinates = [self.rectangle.center[0], self.rectangle.center[1]]
            for increment in range(0, 4):
                hitDetectionCoordinates[0] += float((self.speed/4.0)*(cos(radians(self.angle))))
                hitDetectionCoordinates[1] -= float((self.speed/4.0)*(sin(radians(self.angle))))
                for enemy in listOfEnemies:
                    dx = int(hitDetectionCoordinates[0] - enemy.rectangle.center[0])
                    dy = int(hitDetectionCoordinates[1] - enemy.rectangle.center[1])
                    if self.hitBox.overlap(enemy.hitBox, [dx, dy]):
                        #  Hit an enemy
                        self.angle = 180 - self.angle
                        enemy.currentHealth -= 1
                        hitDetectionCoordinates[0] += float((self.speed / 4.0) * (cos(radians(self.angle))))
                        hitDetectionCoordinates[1] -= float((self.speed / 4.0) * (sin(radians(self.angle))))
                        break
                for otherAsteroid in listOfOtherAsteroids:
                    dx = int(hitDetectionCoordinates[0] - otherAsteroid.rectangle.center[0])
                    dy = int(hitDetectionCoordinates[1] - otherAsteroid.rectangle.center[1])
                    if self.hitBox.overlap(otherAsteroid.hitBox, [dx, dy]) and \
                            self.originalPosition != otherAsteroid.originalPosition:
                        self.angle = 180 - self.angle
                        hitDetectionCoordinates[0] += float((self.speed / 4.0) * (cos(radians(self.angle))))
                        hitDetectionCoordinates[1] -= float((self.speed / 4.0) * (sin(radians(self.angle))))
                dx = int(hitDetectionCoordinates[0] - playerPosition[0])
                dy = int(hitDetectionCoordinates[1] - playerPosition[1])
                if self.hitBox.overlap(playerHitBox, [dx, dy]):
                    self.angle = 180 - self.angle
                    hitThePlayer = 3
                    hitDetectionCoordinates[0] += float((self.speed / 4.0) * (cos(radians(self.angle))))
                    hitDetectionCoordinates[1] -= float((self.speed / 4.0) * (sin(radians(self.angle))))
            self.center = [hitDetectionCoordinates[0], hitDetectionCoordinates[1]]
            if self.center[0] > 640:
                self.center[0] -= 640
            if self.center[0] < 0:
                self.center[0] += 640
            if self.center[1] < 0:
                self.center[1] += 640
            if self.center[1] > 640:
                self.center[1] -= 640
            self.rectangle = self.image.get_rect(center=self.center)
        return [self.image, self.rectangle, hitThePlayer]
