import pygame
import sys
import random
import time

from pygame.examples.scrap_clipboard import screen


class player:
    def __init__(self, screen: pygame.surface, x, y, image_filename):

        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 7
        self.image = pygame.image.load(image_filename)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
