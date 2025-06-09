import pygame
import sys
import my_character
import random
import time
from timer import Timer
import my_character
from GRASS import Grass

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((640, 480))
    # creates a Character from the my_character.py file
    character = my_character.Character(screen, 100, 100)

    countdown = Timer(screen)

    grass1 = Grass(screen, 300, 200, 50, 50)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            character.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            character.y += 5
        if pressed_keys[pygame.K_LEFT]:
            character.x -= 5
        if pressed_keys[pygame.K_RIGHT]:
            character.x += 5
        screen.fill((160, 160, 160))
        if countdown.countdown():
            end_num = 0
            break

        # draws the character every frame
        grass1.draw()
        character.draw()

        if grass1.hit_by(character):
            end_num = 1
            break


        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

    if end_num == 0:
        while True:
            clock.tick(60)  # this sets the framerate of your game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            print("Timer")
            pygame.display.update()

    if end_num == 1:
        while True:
            clock.tick(60)  # this sets the framerate of your game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            print("Grass")
            pygame.display.update()

main()