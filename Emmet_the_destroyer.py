import pygame
class Emmet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pygame.image.load("stick_character.png")
        #self.image = pygame.transform.scale(self.image, (30, 30))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
class Rocket:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 15
        self.image = pygame.image.load("ESTES.png")
        #self.image = pygame.transform.scale(self.image, (30, 30))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))