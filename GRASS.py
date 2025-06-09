import pygame
class Grass:
    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("grass.png")
        self.width = width
        self.height = height
    def draw (self):
        self.screen.blit(self.image, (self.x, self.y))
    def hit_by(self, player):
        grass_hit_box = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        player_hit_box = pygame.Rect(player.x, player.y, player.image.get_width(), player.image.get_height())
        return grass_hit_box.colliderect(player_hit_box)

