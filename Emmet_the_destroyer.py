import pygame
import random
class Emmet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pygame.image.load("EmmetTheDestroyer.png")
        self.ammo = []
        self.image = pygame.transform.scale(self.image, (30, 30))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        new_rocket = Rocket(self.screen, self.x, self.y + self.image.get_height())
        self.ammo.append(new_rocket)
class Rocket:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 15
        self.image = pygame.draw.line(self.screen, (20,20,20), (self.x, self.y), (self.x, self.y - 10), 5)
        self.image = pygame.transform.scale(self.image, (30, 30))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= self.speed