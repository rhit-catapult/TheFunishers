import pygame
import sys
import time
from timer import Timer
from my_character import Character
from GRASS import Grass
from pda import Still
from pda import Walking

def main():
    pygame.init()
    pygame.mixer.init()
    font = pygame.font.SysFont("comicsansms", 30)

    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((640, 480))
    character = Character(screen, 100, 0)
    character.x = 250
    character.y = (screen.get_height() - character.image.get_height()) // 2
    clock = pygame.time.Clock()
    pygame.mixer.music.load("alarm_clock.mp3")
    pygame.mixer.music.play(-1)
    emmet_jumpscare = pygame.image.load("emmet_jumpscare.png")
    emmet_jumpscare = pygame.transform.scale(emmet_jumpscare, (screen.get_width(), screen.get_height()))

    message_text = ""
    screen_one_done = False
    screen_two_done = False
    screen_three_done = False
    screen_four_done = False
    screen_five_done = False
    screen_six_done = False
    end_num = 0

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
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            break
        caption = font.render(message_text, True, (255, 255, 255))
        screen.blit(caption, ((screen.get_width() - caption.get_width()) / 2, screen.get_height() - 55))
        pygame.display.update()

    pygame.mixer.music.stop()
    countdown = Timer(screen)
    pygame.mixer.music.load("game_music.mp3")
    pygame.mixer.music.play(-1)

    bsb = pygame.image.load("BSB.png")
    bsb = pygame.transform.scale(bsb, (243, 345))
    grass1 = Grass(screen, 300, 0, 340, 200)
    grass2 = Grass(screen, 300, 280, 340, 200)
    grass3 = Grass(screen, 300, 0, 340, 200)
    grass4 = Grass(screen, 300, 0, 340, 200)
    grass5 = Grass(screen, 300, 0, 340, 200)
    grass6 = Grass(screen, 300, 0, 340, 200)


    """Screen 1 (BSB)"""
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            if character.y < 0:
                character.y -= character.y
            else:
                character.y -= 3
        if pressed_keys[pygame.K_DOWN]:
            if character.y + character.image.get_height() > screen.get_height():
                character.y += screen.get_height() - character.y - character.image.get_height()
            else:
                character.y += 3
        if pressed_keys[pygame.K_LEFT]:
            if character.x < 0:
                character.x -= character.x
            else:
                character.x -= 3
        if pressed_keys[pygame.K_RIGHT]:
            if character.x + character.image.get_width() > screen.get_width():
                character.x += screen.get_width() - character.x - character.image.get_width()
            else:
                character.x += 3
        screen.fill((160, 160, 160))

        grass1.draw()
        grass2.draw()
        #grass3.draw()
        #grass4.draw()
        #grass5.draw()
        #grass6.draw()
        screen.blit(bsb,(0, (screen.get_height() - bsb.get_height()) // 2))
        character.draw()

        if countdown.countdown() or pressed_keys[pygame.K_e]:
            end_num = 0
            break

        if grass1.hit_by(character) or grass2.hit_by(character) or grass3.hit_by(character) or grass4.hit_by(character) or grass5.hit_by(character) or grass6.hit_by(character):
            end_num = 1
            break

        #if spda1.hit_by(character):
        #    end_num = 2
        #    break

        if pressed_keys[pygame.K_w]:
            end_num = 3
            break

        if pressed_keys[pygame.K_1]:
            screen_one_done = True
            break

        if character.x == screen.get_width() - character.image.get_width() and character.y > 200 and character.y < 280:
            screen_one_done = True
            break


        pygame.display.update()

    spda1 = Still(screen, 0, 400)
    spda2 = Still(screen, 0, 400)
    spda3 = Still(screen, 0, 400)
    spda4 = Still(screen, 0, 400)
    spda5 = Still(screen, 0, 400)

    """Screen 2 (Level 1)"""
    if screen_one_done:
        character.x = 0
        grass1.move(0, 0, 100, 200)
        grass2.move(0, 280, 180, 200)
        grass3.move(100, 0, 300, 50)
        grass4.move(180, 130, 80, 350)
        grass5.move(500, 300, 10, 10)
        grass6.move(520, 300, 10, 10)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_UP]:
                if character.y < 0:
                    character.y -= character.y
                else:
                    character.y -= 3
            if pressed_keys[pygame.K_DOWN]:
                if character.y + character.image.get_height() > screen.get_height():
                    character.y += screen.get_height() - character.y - character.image.get_height()
                else:
                    character.y += 3
            if pressed_keys[pygame.K_LEFT]:
                if character.x < 0:
                    character.x -= character.x
                else:
                    character.x -= 3
            if pressed_keys[pygame.K_RIGHT]:
                if character.x + character.image.get_width() > screen.get_width():
                    character.x += screen.get_width() - character.x - character.image.get_width()
                else:
                    character.x += 3
            screen.fill((160, 160, 160))

            grass1.draw()
            grass2.draw()
            grass3.draw()
            grass4.draw()
            grass5.draw()
            grass6.draw()
            spda1.draw()
            character.draw()

            if countdown.countdown() or pressed_keys[pygame.K_e]:
                end_num = 0
                break

            if grass1.hit_by(character) or grass2.hit_by(character) or grass3.hit_by(character) or grass4.hit_by(character) or grass5.hit_by(character) or grass6.hit_by(character):
                end_num = 1
                break

            if spda1.hit_by(character) or spda2.hit_by(character) or spda3.hit_by(character) or spda4.hit_by(character) or spda5.hit_by(character):
                end_num = 2
                break

            if pressed_keys[pygame.K_w]:
                end_num = 3
                break


            pygame.display.update()

    pygame.mixer.music.stop()
    end_time = time.time()

    if end_num == 0:
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
            screen.blit(emmet_jumpscare, (0, 0))
            pygame.display.update()

    if end_num == 2:
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            screen.blit(emmet_jumpscare, (0, 0))
            pygame.display.update()

    if end_num == 3:
        pygame.mixer.music.load("good_end_music.mp3")
        pygame.mixer.music.play(-1)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            if time.time() - 5 < end_time:
                message_text = "You made it on time! Good job!"
            elif time.time() - 10 < end_time:
                message_text = "Now grab a seat before we start."
            else:
                message_text = ""
            end_caption = font.render(message_text, True, (255, 255, 255))
            screen.blit(end_caption, ((screen.get_width() - end_caption.get_width()) / 2, screen.get_height() - 55))
            pygame.display.update()


main()