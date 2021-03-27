from Baddie import Enemy
from math import sqrt
from random import randint


class Sprayer(Enemy):
    def __init__(self, position, offset=0, rateOfFire=85, bulletSpeed=6.0):
        Enemy.__init__(self, position=position)
        self.laserColors = [[0, 0, 255], [0, 255, 0], [255, 255, 0], [255, 0, 0]]
        self.fireCoolDownMax = 90
        self.currentFireFrame = 0

        self.fireCoolDownMax = rateOfFire
        self.offset = offset
        self.bulletSpeed = bulletSpeed

        self.movementOffset = randint(-50, 50)
        self.fireOffset = randint(-20,20)

        self.offset = 0

    def update(self, playerPosition, notPaused):
        self.calculateAngle(playerPosition)
        toShoot = []
        if self.alive:
            toReturn = toReturn = self.lowLevelUpdate(False)
            if notPaused:
                x = playerPosition[0] - self.rectangle.center[0]
                y = playerPosition[1] - self.rectangle.center[1]
                distanceToPlayer = int(sqrt(x ** 2 + y ** 2))
                if distanceToPlayer > 300 + self.movementOffset:
                    self.speed = 5
                    toShoot = False
                    toReturn = self.lowLevelUpdate(notPaused)
                elif self.currentFireFrame >= self.fireCoolDownMax + self.fireOffset:
                    #  Shoot
                    self.speed = 0
                    self.currentFireFrame = 0
                    toReturn = self.lowLevelUpdate(notPaused)
                    adjustedAim = [playerPosition[0], playerPosition[1]]
                    adjustedAim = [adjustedAim[0], adjustedAim[1], self.rectangle.center[0], self.rectangle.center[1]]
                    toShoot = [adjustedAim, self.bulletSpeed, False, [self.rectangle.center[0],self.rectangle.center[1]]]
                else:  # player in range but recharging
                    self.speed = 0
                    toShoot = False
                    toReturn = self.lowLevelUpdate(notPaused)
                self.currentFireFrame += 1
            return [toReturn, 0, toShoot]
        else:
            return False
