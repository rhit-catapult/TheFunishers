import pygame
class Emmet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load("EmmetTheDestroyer.png")
        self.ammo = []
        self.image = pygame.transform.scale(self.image, (50, 50))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def fire(self):
        new_rocket = Rocket(self.screen, self.x, self.y + self.image.get_height(), (self.image.get_width() / 4), self.image.get_height)
        self.ammo.append(new_rocket)

    def move(self, end1, end2):
        if self.x < end1 or self.x > end2:
            self.speed *= -1
        self.x += self.speed
class Rocket:
    def __init__(self, screen, x, y, width, length):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 15
        self.image = pygame.image.load("ESTES.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.width = width
        self.length = length

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.speed

#def main():
#    pygame.init()
#    pygame.mixer.init()
#    end_font = pygame.font.SysFont("comicsansms", 30)
#
#    pygame.display.set_caption("Cool Project")
#    screen = pygame.display.set_mode((640, 480))
#    death = Emmet(screen, 100, 100)
#    boom = Rocket(screen, 50, 100, 10, 20)
#    while True:
#        screen.fill((160, 160, 160))
#        death.draw()
#        boom.draw()
#        pygame.display.update()
#main()
