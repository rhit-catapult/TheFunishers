import pygame
import time

class Timer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsansms", 20)
        self.start_time = time.time()

    def countdown(self):
        time_left = int(60 - (time.time() - self.start_time))
        if time_left > 10:
            caption = self.font.render(str(time_left), True, (0, 0, 0))
        else:
            caption = self.font.render(str(time_left), True, (255, 0, 0))
        self.screen.blit(caption, (25, 25))