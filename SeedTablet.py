from Tablet import Tablet
from os import path
from sys import argv
import pygame


class SeedTablet(Tablet):

    def __init__(self, center, seed, difficulty, title):
        updatedInfo = seed + "|" + str("{:4}".format(difficulty)) + "|" + ""
        Tablet.__init__(self, center, updatedInfo)

        filepath = path.dirname(argv[0])
        self.passiveImage = pygame.image.load(filepath + "/resources/images/tabletActive.png").convert()
        self.passiveImage.set_colorkey((255, 255, 255))
        self.activeImage = pygame.image.load(filepath + "/resources/images/tabletPassive.png").convert()
        self.activeImage.set_colorkey((255, 255, 255))
        self.rectangle = self.passiveImage.get_rect(center=center)

        trueInfo = ["-------------", str(seed), str(difficulty)]

        labels = [title, "Seed", "Difficulty"]
        centerX = self.rectangle.width / 2
        startingY = 20
        index = 0
        for text in labels:
            textLabel = self.largeTabletFont.render(text, 1, [255, 15, 15])
            textLabelDark = self.largeTabletFont.render(text, 1, (158, 28, 25))
            self.drawTextOnBoth(textLabel, textLabelDark, self.largeTabletFont.size(text), [centerX, startingY])
            infoText = self.smallTabletFont.render(trueInfo[index], 1, [255, 0, 0])
            infoTextDark = self.smallTabletFont.render(trueInfo[index], 1, [140, 0, 0])
            self.drawTextOnBoth(infoText, infoTextDark, self.smallTabletFont.size(trueInfo[index]),
                                [centerX, startingY + 30])
            startingY += 60
            index += 1
        self.toReturnUponClick = seed
