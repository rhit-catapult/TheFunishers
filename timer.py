import pygame
import time

class Timer:
    def __init__(self, screen):
        self.screen = screen
        self.start_time = time.time()

    def countdown(self):
        time_left = int(60 - (time.time() - self.start_time))
        if time_left > 10:
            self.font = pygame.font.SysFont("comicsansms", 20)
            caption = self.font.render(str(time_left), True, (0, 0, 0))
        else:
            self.font = pygame.font.SysFont("comicsansms", 50)
            caption = self.font.render(str(time_left), True, (255, 0, 0))
        self.screen.blit(caption, (25, 25))