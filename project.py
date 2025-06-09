import pygame
import sys
import time
from timer import Timer
import my_character
from GRASS import Grass
from pda import Still
from pda import Walking

def main():
    pygame.init()
    pygame.mixer.init()
    font = pygame.font.SysFont("comicsansms", 30)

    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((640, 480))
    character = my_character.Character(screen, 100, 100)
    clock = pygame.time.Clock()

    message_text = ""
    start_time = time.time()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        if time.time()-3 < start_time:
            message_text = "Wake up sleepyhead!"
        elif time.time()-6 < start_time:
            message_text = "You slept in until 8:29!"
        elif time.time()-10 < start_time:
            message_text = "You have one minute to get to Hatfield Hall."
        elif time.time()-12 < start_time:
            message_text = "And remember..."
        elif time.time()-15 < start_time:
            message_text = "FOLLOW THE RULES"
        else:
            break
        caption = font.render(message_text, True, (255, 255, 255))
        screen.blit(caption, ((screen.get_width() - caption.get_width()) / 2, screen.get_height() - 55))
        pygame.display.update()

    countdown = Timer(screen)
    pygame.mixer.music.load("game_music.mp3")
    pygame.mixer.music.play(-1)

    grass1 = Grass(screen, 300, 200, 50, 50)

    spda1 = Still(screen, 200, 300)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            character.y -= 3
        if pressed_keys[pygame.K_DOWN]:
            character.y += 3
        if pressed_keys[pygame.K_LEFT]:
            character.x -= 3
        if pressed_keys[pygame.K_RIGHT]:
            character.x += 3
        screen.fill((160, 160, 160))
        if countdown.countdown() or pressed_keys[pygame.K_e]:
            end_num = 0
            break

        grass1.draw()
        spda1.draw()
        character.draw()

        if grass1.hit_by(character):
            end_num = 1
            break

        if spda1.hit_by(character):
            end_num = 2
            break


        pygame.display.update()

    pygame.mixer.music.stop()

    if end_num == 0:
        end_time = time.time()
        pygame.mixer.music.load("timer_end_music.mp3")
        pygame.mixer.music.play(-1)
        message_text = ""
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            if time.time()-5 < end_time:
                message_text = "You were late for the morning meeting."
            elif time.time()-10 < end_time:
                message_text = "You know what happens now..."
            else:
                message_text = ""
                pygame.mixer.music.fadeout(2000)
            end_caption = font.render(message_text, True, (255, 255, 255))
            screen.blit(end_caption, ((screen.get_width() - end_caption.get_width())/2, screen.get_height() - 55))
            pygame.display.update()

    if end_num == 1:
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            print("Grass")
            pygame.display.update()

    if end_num == 2:
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            print("PDA")
            pygame.display.update()


main()