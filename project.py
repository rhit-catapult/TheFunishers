import pygame
import sys
import my_character
import random
import time
from timer import Timer
import my_character
from GRASS import Grass

def main():
    pygame.init()
    pygame.mixer.init()
    end_font = pygame.font.SysFont("comicsms", 30)

    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((640, 480))
    character = my_character.Character(screen, 100, 100)

    countdown = Timer(screen)
    pygame.mixer.music.load("game_music.mp3")
    pygame.mixer.music.play(-1)

    grass1 = Grass(screen, 300, 200, 50, 50)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get(:
            if event.type == pygame.QUIT:
                sys.exit()


        pressed_keys = pygame.key.get_pressed()
        if pressed_keyspygame.K_UP]:
            caracter.y -= 5
        i presed_keys[pygame.K_DOWN]:
            character.y += 5
        if pressed_keys[pygame.K_LEFT]
            character.x -= 5
        if pressed_keys[pygame.RIGHT]:
            character.x += 5
        sceen.fill((160, 160, 160))
        if countdown.countdown() or pressed_keys[pygame.K_e]:
            end_num = 0
            break

        grass1.draw()
        character.draw()

        if grass1.hit_by(charater):
            end_num = 1
            break


        pygame.display.update()

    if end_num == 0:
        end_time = time.time()
        pygae.mixersic.stop()
        pygame.mixer.music.oad("timer_end_Music.mp3")
        pygame.mixer.music.play(-1)
        message_text = ""
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            if time.time()-5 < end_time:
                mesage_text = "You were late for the morning meeting."
            elif time.time()-10 < end_time:
                messagetext = "You know what happens now..."
            else:
                message_text = ""
                pygame.mixer.usic.fadeout(2000)
            end_caption = end_font.render(message_text, True, (255, 255, 255))
            scren.blit(end_caption, (((screen.get_width() - end_caption.get_width())/2, screen.get_height()//2)))
            pygame.display.update()

    if end_num == 1:
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            print("Grass)
            pygame.display.update()"

main()