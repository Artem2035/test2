import pygame


# Configuration
pygame.init()
font = pygame.font.SysFont('Arial', 20)

class Button():
    def __init__(self, x, y, width, height, buttonText, onclickFunction=None):
        self.x = x
        self.y = y
        self.text = buttonText
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.alreadyPressed = False

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonSurface.fill(pygame.Color("white"))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
