import pygame
import random


class Wire:
    def __init__(self, x: int, y: int, angle: int, format: str):
        self.x = x
        self.y = y
        if format == "line":
            self.image = random.randint(1, 2)
            self.surf_light = pygame.image.load(f'assets/sell-{self.image}-l.png')
            self.surf_no_light = pygame.image.load(f'assets/sell-{self.image}.png')
        elif format == "angle":
            self.image = random.randint(3, 6)
            self.surf_light = pygame.image.load(f'assets/sell-{self.image}-l.png')
            self.surf_no_light = pygame.image.load(f'assets/sell-{self.image}.png')
        self.surf = self.surf_no_light
        self.rect = self.surf.get_rect()
        if self.image == 1:
            self.angle = 0
        if self.image == 2:
            self.angle = -90
        if self.image == 3:
            self.angle = 90
        if self.image == 4:
            self.angle = 180
        if self.image == 5:
            self.angle = 270
        if self.image == 6:
            self.angle = 360
        self.right_angle = angle

    def get_coordinates(self):
        return self.x, self.y

    def change_angle(self):
        if self.angle == 0:
            self.angle = -90
        elif self.angle == -90:
            self.angle = 0
        else:
            if self.angle+90 <= 360:
                self.angle += 90
            else:
                self.angle = 90

    def rotate(self):
        self.change_angle()
        self.surf_light = pygame.transform.rotate(self.surf_light, -90)
        self.surf_no_light = pygame.transform.rotate(self.surf_no_light, -90)
        if self.angle == self.right_angle:
            self.surf = self.surf_light
        else:
            self.surf = self.surf_no_light