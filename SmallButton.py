from Button import Button
import pygame


class SmallButton(Button):
    def __init__(self, position, value, label):
        Button.__init__(self, position, value, label)
        self.unPressedImage = pygame.transform.smoothscale(self.unPressedImage, (104, 32))
        self.pressedImage = pygame.transform.smoothscale(self.pressedImage, (104, 32))
        self.collisionArea = self.pressedImage.get_rect(topleft=position)
