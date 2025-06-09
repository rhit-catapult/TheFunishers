import pygame
import sys
import my_character
import random
import time
from timer import Timer
import my_character

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((640, 480))
    # creates a Character from the my_character.py file
    character = my_character.Character(screen, 100, 100, 7)

    countdown = Timer(screen)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

            pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            character.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            character.y += 10
        if pressed_keys[pygame.K_LEFT]:
            character.x -= 10
        if pressed_keys[pygame.K_RIGHT]:
            character.x += 10
    # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))
        countdown.countdown()

        # draws the character every frame
        character.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()