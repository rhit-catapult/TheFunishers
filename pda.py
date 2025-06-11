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
        self.width = 40
        self.height = 40
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y

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
        self.width = 40
        self.height = 40
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.speed_x = 2
        self.speed_y = 2

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y

    def walk_x(self, end1, end2):
        if self.x < end1 or self.x > end2:
            self.speed_x *= -1
        self.x += self.speed_x

    def walk_y(self, end1, end2):
        if self.y < end1 or self.y > end2:
            self.speed_y *= -1
        self.y += self.speed_y

    def hit_by(self, player):
        walking_hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        player_hit_box = pygame.Rect(player.x, player.y, player.image.get_width(), player.image.get_height())
        return walking_hit_box.colliderect(player_hit_box)