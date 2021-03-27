import pygame
from os import path
from sys import argv


class Button:
    def __init__(self, position, value, label):
        filePath = path.dirname(argv[0])
        self.buttonSound = pygame.mixer.Sound(filePath+"/resources/audio/button.wav")
        self.buttonSound.set_volume(.25)
        self.buttonSoundChannel = pygame.mixer.Channel(5)
        buttonFont = pygame.font.SysFont('krungthep', 25)
        baseButtonImage = pygame.image.load(filePath + "/resources/images/button.png").convert()
        activeButtonImage = pygame.image.load(filePath + "/resources/images/activeButton.png").convert()
        self.unPressedImage = baseButtonImage.copy()
        self.pressedImage = activeButtonImage.copy()
        self.collisionArea = self.unPressedImage.get_rect(center=position)

        """Jesus Christ this is a Mess"""
        textToRender = buttonFont.render(label, 1, (255, 0, 0))
        textSize = buttonFont.size(label)
        txS2 = [textSize[0] / 2.0, textSize[1] / 2.0]
        adjustedCollisionArea = [self.collisionArea[2] / 2.0, self.collisionArea[3] / 2.0]
        textLocation = [adjustedCollisionArea[0] - txS2[0], adjustedCollisionArea[1] - txS2[1],
                        textSize[0], textSize[1]]
        self.unPressedImage.blit(textToRender, textLocation)
        self.pressedImage.blit(textToRender, textLocation)
        self.value = value
        self.playPressedSound = False
        self.pressedImage.set_colorkey((255, 255, 255))
        self.unPressedImage.set_colorkey((255, 255, 255))

    def draw(self):
        mousePoint = pygame.mouse.get_pos()
        if self.collisionArea.collidepoint(mousePoint[0], mousePoint[1]):
            if self.playPressedSound:
                self.buttonSoundChannel.play(self.buttonSound)
                self.playPressedSound = False
            return self.pressedImage
        else:
            self.playPressedSound = True
            return self.unPressedImage

    def testMouseCollision(self):
        mousePoint = pygame.mouse.get_pos()
        if self.collisionArea.collidepoint(mousePoint[0], mousePoint[1]):
            return self.value
        else:
            return 0
