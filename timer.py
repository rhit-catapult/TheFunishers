import pygame
import time

class Timer:
    def __init__(self, screen):
        self.screen = screen
        self.x = 25
        self.y = 25
        self.font = pygame.font.SysFont("comicsansms", 20)
        self.start_time = time.time()

    def countdown(self):
        time_left = int(60 - (time.time() - start_time))
        print(time_left)
