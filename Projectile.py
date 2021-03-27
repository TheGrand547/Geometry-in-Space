import pygame
from math import sin, cos, radians, degrees, atan2
from misc import moves, angle, calculateAngle, range2
from random import choice
import os
from sys import argv


class Bullet:
    def __init__(self, angle, isPlayerProjectile, bulletSpeed=6.0):
        filePath = os.path.dirname(argv[0])
        self.image = pygame.image.load(filePath+"/resources/images/bullet.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.a = angle
        self.rect = self.image.get_rect(center=[angle[2], angle[3]])
        self.center = [self.rect.center[0], self.rect.center[1]]
        self.hitBox = pygame.mask.from_surface(self.image)
        self.alive = True
        self.speed = bulletSpeed
        self.isPlayerProjectile = isPlayerProjectile
        self.bulletTimeOutMax = 240
        self.currentBulletTime = 0
        bulletSpeed = bulletSpeed

        vectors = calculateAngle([angle[0], angle[1]], [angle[2], angle[3]])
        self.ch = [float(bulletSpeed*float(cos(radians(vectors)))), -float(bulletSpeed*sin(radians(vectors)))]
        self.ch[0] += choice(range2(-3, 3, .125))*.125
        self.ch[0] += choice(range2(-3, 3, .125))*.125
        self.og = [float(bulletSpeed*float(cos(radians(vectors)))), -float(bulletSpeed*sin(radians(vectors)))]

    def update(self, playerRect, playerHitBox, enemies, asteroids, notPaused):
        # hit detection
        damageToPlayer = 0
        if self.alive:
            if notPaused:
                k = [self.rect.center[0], self.rect.center[1]]
                if self.isPlayerProjectile:
                    # player
                    # shots fired, baddies hit, asteroids hit, baddies killed, deaths
                    # wins, time spent playing (in levels)
                    for i in range(0, 5):
                        k[0] += float(self.ch[0] / 5.0)
                        k[1] += float(self.ch[1] / 5.0)
                        for enemy in enemies:
                            if enemy.alive:
                                dx = int(enemy.rectangle.topleft[0] - k[0])
                                dy = int(enemy.rectangle.topleft[1] - k[1])
                                if self.hitBox.overlap(enemy.hitBox, [dx, dy]):
                                    enemy.currentHealth -= 10
                                    self.alive = False
                                    break
                        for asteroid in asteroids:
                            dx = int(asteroid.rectangle.topleft[0] - k[0])
                            dy = int(asteroid.rectangle.topleft[1] - k[1])
                            if self.hitBox.overlap(asteroid.hitBox, [dx, dy]):
                                k = [asteroid.speed * cos(radians(asteroid.angle)), asteroid.speed *
                                     sin(radians(asteroid.angle))]
                                asteroid.angle += 180
                                self.alive = False
                                break
                        if not self.alive:
                            break
                else:
                    # non-player
                    maxCount = 5
                    for i in range(0, maxCount):
                        k[0] += float(self.ch[0] / float(maxCount))
                        k[1] += float(self.ch[1] / float(maxCount))
                        dx = int(playerRect.center[0] - k[0])
                        dy = int(playerRect.center[1] - k[1])
                        if self.hitBox.overlap(playerHitBox, [dx, dy]):
                            damageToPlayer = 7
                            self.alive = False
                # drawing and stuff
                if self.center[0] > 640:
                    self.center[0] -= 640
                if self.center[0] < 0:
                    self.center[0] += 640
                if self.center[1] < 0:
                    self.center[1] += 640
                if self.center[1] > 640:
                    self.center[1] -= 640

                self.rect = self.image.get_rect(center=[k[0], k[1]])
                self.currentBulletTime += 1
                if self.currentBulletTime >= self.bulletTimeOutMax:
                    self.alive = False
            return [self.image, self.rect, damageToPlayer]
        else:
            return False
