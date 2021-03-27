import pygame
from Baddie import Enemy
from math import sqrt


class Laser(Enemy):
    def __init__(self, position):
        Enemy.__init__(self, position)
        self.laserColors = [[0, 0, 255], [0, 255, 0], [255, 255, 0],
                            [255, 0, 0]]
        self.laserColorsCount = self.laserColors[0]
        self.laserTimerMax = 20
        self.laserTimerCurrent = 0
        self.lasersActive = False
        self.laserRechargeTimer = 31
        self.laserRechargeTimerMax = 30
        self.laserMaxDistance = 50
        self.currentLaserPhase = 0

    def update(self, playerPosition, notPaused):
        playerHit = 0
        inRange = False
        if self.alive:
            """
            I forgot how these guys were written so I'm rewriting them
            New? rule they will keep moving to try and stay within reach of the player, due to the players increased
            mobility
            """
            if notPaused:
                x = playerPosition[0] - self.rectangle.center[0]
                y = playerPosition[1] - self.rectangle.center[1]
                distanceToPlayer = int(sqrt(x ** 2 + y ** 2))
                if distanceToPlayer <= 100 and self.laserRechargeTimerMax < self.laserRechargeTimer:
                    #  This means that the player is within range of the laser beam attack
                    if self.laserTimerCurrent == 0:
                        #  This means the player has just moved within range of the attack
                        self.laserTimerCurrent += 1
                        self.laserColorsCount = self.laserColors[0]
                    elif self.laserTimerCurrent >= self.laserTimerMax and self.laserColorsCount != self.laserColors[3]:
                        #  Color Changes now
                        self.laserColorsCount = self.laserColors[self.currentLaserPhase+1]
                        self.currentLaserPhase += 1
                        self.laserTimerCurrent = 1
                    elif self.laserTimerCurrent >= self.laserTimerMax and self.currentLaserPhase == 3:
                        #  Player is hit
                        playerHit = 25
                        self.laserColorsCount = 0
                        self.laserTimerCurrent = 0
                        self.laserRechargeTimer = 1
                        self.currentLaserPhase = 0
                    else:
                        #  Laser is currently firing
                        self.laserTimerCurrent += 1
                    inRange = True

                elif distanceToPlayer > 100:
                    self.laserTimerCurrent = 0
                    self.currentLaserPhase = 0
                if self.laserRechargeTimer > 0:
                    #  Laser is recharging
                    self.laserRechargeTimer += 1
                if distanceToPlayer < 80:
                    self.speed = 0
                else:
                    self.speed = 5

                #  They will move no matter what so it doesn't need to be within the if block
            self.calculateAngle(playerPosition)
            return [self.lowLevelUpdate(notPaused), playerHit, None, self.laserColorsCount, inRange]
        return False
