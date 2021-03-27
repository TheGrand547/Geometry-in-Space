import pygame
from os import path
from sys import argv
from misc import getCoordinatesToCenterTextMiddle


class Tablet:
    def __init__(self, center, info):
        filepath = path.dirname(argv[0])
        self.smallTabletFont = pygame.font.SysFont('krungthep', 18)
        self.largeTabletFont = pygame.font.SysFont('krungthep', 20)

        self.buttonSound = pygame.mixer.Sound(filepath + "/resources/audio/button.wav")
        self.buttonSound.set_volume(.45)
        self.buttonSoundChannel = pygame.mixer.Channel(5)

        self.passiveImage = pygame.image.load(filepath+"/resources/images/tabletActive.png").convert()
        self.passiveImage.set_colorkey((255, 255, 255))
        self.activeImage = pygame.image.load(filepath+"/resources/images/tabletPassive.png").convert()
        self.activeImage.set_colorkey((255, 255, 255))
        self.rectangle = self.passiveImage.get_rect(center=center)
        self.trueInfo = info.replace("\n", "").split('|')
        labels = ["Seed", "Difficulty", "Score"]
        self.trueInfo[1] = str(round(float(self.trueInfo[1]), 3))

        centerX = self.rectangle.width / 2
        startingY = 20
        index = 0
        for text in labels:
            textLabel = self.largeTabletFont.render(text, 1, [255, 15, 15])
            textLabelDark = self.largeTabletFont.render(text, 1, (158, 28, 25))
            self.drawTextOnBoth(textLabel, textLabelDark, self.largeTabletFont.size(text), [centerX, startingY])
            infoText = self.smallTabletFont.render(self.trueInfo[index], 1, [255, 0, 0])
            infoTextDark = self.smallTabletFont.render(self.trueInfo[index], 1, [140, 0, 0])
            self.drawTextOnBoth(infoText, infoTextDark, self.smallTabletFont.size(self.trueInfo[index]),
                                [centerX, startingY+30])
            startingY += 60
            index += 1
        self.toReturnUponClick = self.trueInfo[0]
        self.pressedLast = False

    def update(self):
        mousePosition = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mousePosition):
            if self.pressedLast:
                self.buttonSoundChannel.play(self.buttonSound)
                self.pressedLast = False
            return self.activeImage
        else:
            self.pressedLast = True
            return self.passiveImage

    def drawTextOnBoth(self, renderedText, renderedTextDark, textSize, position):
        placeToDraw = getCoordinatesToCenterTextMiddle(textSize, position)
        self.passiveImage.blit(renderedText, placeToDraw)
        self.activeImage.blit(renderedTextDark, placeToDraw)


