import pygame
import sys
import random
import time


class Still:

    def __init__(self, screen: pygame.surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("person.png")
        self.width = 80
        self.height = 50
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, player):
        still_hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        player_hit_box = pygame.Rect(player.x, player.y, player.image.get_width(), player.image.get_height())
        return still_hit_box.colliderect(player_hit_box)

class Walking:

    def __init__(self, screen: pygame.surface, x, y):

        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("person_walking.png")

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, player):
        walking_hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        player_hit_box = pygame.Rect(player.x, player.y, player.image.get_width(), player.image.get_height())
        return walking_hit_box.colliderect(player_hit_box)