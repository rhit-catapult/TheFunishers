import pygame
import sys
import time
from timer import Timer
from my_character import Character
from sounds.GRASS import Grass
from pda import Still
from pda import Walking
from Emmet_the_destroyer import Emmet
from Emmet_the_destroyer import Rocket

def main():
    pygame.init()
    pygame.mixer.init()
    font = pygame.font.SysFont("comicsansms", 30)
    instructions_font = pygame.font.SysFont("comicsansms", 15)
    ui_font = pygame.font.SysFont("impact", 20)

    pygame.display.set_caption("Cool Project")
    screen = pygame.display.set_mode((640, 480))
    character = Character(screen, 100, 0)
    character.x = 250
    character.y = (screen.get_height() - character.image.get_height()) // 2
    clock = pygame.time.Clock()
    pygame.mixer.music.load("alarm_clock.mp3")
    pygame.mixer.music.play(0)
    emmet_jumpscare = pygame.image.load("emmet_jumpscare.png")
    emmet_jumpscare = pygame.transform.scale(emmet_jumpscare, (screen.get_width(), screen.get_height()))
    eathan_happy = pygame.image.load("eathan_happy.png")
    eathan_happy = pygame.transform.scale(eathan_happy, (screen.get_width(), screen.get_height() - 80))
    eathan_angry = pygame.image.load("eathan_angry.png")
    eathan_angry = pygame.transform.scale(eathan_angry, (screen.get_width(), screen.get_height() - 80))
    dirty_van = pygame.image.load("dirty_van.png")
    dirty_van = pygame.transform.scale(dirty_van, (screen.get_width(), screen.get_height() - 80))

    message_text = ""
    instructions = ""
    screen_one_done = False
    screen_two_done = False
    screen_three_done = False
    screen_four_done = False
    end_num = 5

    start_time = time.time()
    """Start Screen"""
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        if time.time()-3 < start_time:
            message_text = "Wake up sleepyhead!"
            instructions = "(Press SPACE to skip)"
        elif time.time()-6 < start_time:
            message_text = "You slept in until 8:29!"
            instructions = ""
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
        instruct_caption = instructions_font.render(instructions, True, (180, 180, 180))
        screen.blit(instruct_caption, (screen.get_width() - instruct_caption.get_width() - 5, screen.get_height() - 20))
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
    grass7 = Grass(screen, 300, 0, 340, 200)
    instructions = "Press ARROW KEYS to move"

    level_text = "1. BSB"
    level = ui_font.render(level_text, True, (255, 255, 255))


    """Screen 1 (Level 1: BSB)"""
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
        instruct_caption = instructions_font.render(instructions, True, (255, 255, 255))
        screen.blit(instruct_caption, (screen.get_width() - instruct_caption.get_width() - 5, screen.get_height() - 20))
        screen.blit(level, ((screen.get_width() - level.get_width()) // 2, 0))
        character.draw()

        if countdown.countdown():
            end_num = 0
            break

        if grass1.hit_by(character) or grass2.hit_by(character) or grass3.hit_by(character) or grass4.hit_by(character) or grass5.hit_by(character) or grass6.hit_by(character):
            end_num = 1
            break

        #if spda1.hit_by(character):
        #    end_num = 2
        #    break

        if character.x == screen.get_width() - character.image.get_width():
            screen_one_done = True
            break


        pygame.display.update()

    spda1 = Still(screen, 0, 400)
    spda2 = Still(screen, 0, 400)
    spda3 = Still(screen, 0, 400)
    spda4 = Still(screen, 0, 400)
    spda5 = Still(screen, 0, 400)
    spda6 = Still(screen, 0, 400)
    spda7 = Still(screen, 0, 400)
    spda8 = Still(screen, 0, 400)

    level_text = "2. Beginning"
    level = ui_font.render(level_text, True, (255, 255, 255))


    """Screen 2 (Level 2: Beginning)"""
    if screen_one_done:
        character.x = 0
        character.y = 230
        grass1 = Grass(screen, 0, 0, 100, 200)
        grass2 = Grass(screen, 0, 280, 180, 200)
        grass3 = Grass(screen, 100, 0, 300, 50)
        grass4 = Grass(screen, 180, 130, 80, 350)
        grass5 = Grass(screen, 400, 0, 80, 350)
        grass6 = Grass(screen, 260, 430, 380, 50)
        grass7 = Grass(screen, 560, 0, 80, 430)
        spda1.move(355, 130)
        spda2.move(265, 220)
        spda3.move(355, 310)
        #spda4.move(0, 0)
        #spda5.move(0, 0)
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
            grass7.draw()
            spda1.draw()
            spda2.draw()
            spda3.draw()
            #spda4.draw()
            #spda5.draw()
            #spda6.draw()
            #spda7.draw()
            #spda8.draw()
            screen.blit(level, ((screen.get_width() - level.get_width()) // 2, 0))
            character.draw()

            if countdown.countdown():
                end_num = 0
                break

            if grass1.hit_by(character) or grass2.hit_by(character) or grass3.hit_by(character) or grass4.hit_by(character) or grass5.hit_by(character) or grass6.hit_by(character) or grass7.hit_by(character):
                end_num = 1
                break

            if spda1.hit_by(character) or spda2.hit_by(character) or spda3.hit_by(character) or spda4.hit_by(character) or spda5.hit_by(character) or spda6.hit_by(character) or spda7.hit_by(character) or spda8.hit_by(character):
                end_num = 2
                break

            if character.y == 0:
                screen_two_done = True
                break


            pygame.display.update()

    wpda1 = Walking(screen, 200, 100)
    wpda2 = Walking(screen, 150, 340)

    level_text = "3. Road"
    level = ui_font.render(level_text, True, (255, 255, 255))


    """Screen 3 (Level 3: Road)"""
    if screen_two_done:
        character.x = 510
        character.y = screen.get_height() - character.image.get_height()
        grass1 = Grass(screen, 0, 0, 480, 80)
        grass2 = Grass(screen, 560, 0, 80, 80)
        grass3 = Grass(screen, 0, 400, 480, 80)
        grass4 = Grass(screen, 560, 400, 80, 80)
        grass5 = Grass(screen, 560, 400, 80, 80)
        grass6 = Grass(screen, 560, 400, 80, 80)
        grass7 = Grass(screen, 560, 400, 80, 80)
        spda1.move(450, 110)
        spda2.move(480, 150)
        spda3.move(525, 360)
        spda4.move(491, 310)
        spda5.move(430, 270)
        spda6.move(370, 240)
        spda7.move(310, 220)
        spda8.move(250, 210)
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

            pygame.draw.rect(screen, (60, 60, 60), (0, 100, 640, 280))
            wpda1.walk_y(100, 340)
            wpda2.walk_y(100, 340)
            grass1.draw()
            grass2.draw()
            grass3.draw()
            grass4.draw()
            grass5.draw()
            grass6.draw()
            grass7.draw()
            spda1.draw()
            spda2.draw()
            spda3.draw()
            spda4.draw()
            spda5.draw()
            spda6.draw()
            spda7.draw()
            spda8.draw()
            wpda1.draw()
            wpda2.draw()
            screen.blit(level, ((screen.get_width() - level.get_width()) // 2, 0))
            character.draw()

            if countdown.countdown():
                end_num = 0
                break

            if grass1.hit_by(character) or grass2.hit_by(character) or grass3.hit_by(
                    character) or grass4.hit_by(character) or grass5.hit_by(character) or grass6.hit_by(
                    character):
                end_num = 1
                break

            if spda1.hit_by(character) or spda2.hit_by(character) or spda3.hit_by(character) or spda4.hit_by(
                    character) or spda5.hit_by(character) or spda6.hit_by(character) or spda7.hit_by(
                    character) or spda8.hit_by(character) or wpda1.hit_by(character) or wpda2.hit_by(character):
                end_num = 2
                break

            if character.y == 0:
                screen_three_done = True
                break

            pygame.display.update()

    level_text = "4. Tight Squeeze"
    level = ui_font.render(level_text, True, (255, 255, 255))


    """Screen 4 (Level 4: Wraparound)"""
    if screen_three_done:
        character.x = 510
        character.y = screen.get_height() - character.image.get_height()
        grass1 = Grass(screen, 0, 0, 80, 400)
        grass2 = Grass(screen, 120, 120, 400, 240)
        grass3 = Grass(screen, 0, 400, 480, 80)
        grass4 = Grass(screen, 560, 360, 80, 120)
        grass5 = Grass(screen, 80, 0, 560, 80)
        grass6 = Grass(screen, 520, 320, 120, 40)
        grass7 = Grass(screen, 560, 80, 80, 200)
        spda1.move(450, 110)
        spda2.move(480, 150)
        spda3.move(525, 360)
        spda4.move(491, 310)
        spda5.move(430, 270)
        spda6.move(370, 240)
        spda7.move(310, 220)
        spda8.move(250, 210)
        wpda1.move(275, 300)
        wpda2.move(275, 140)
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

            wpda1.walk_y(300, 420 )
            wpda2.walk_y(20, 140)
            grass1.draw()
            grass2.draw()
            grass3.draw()
            grass4.draw()
            grass5.draw()
            grass6.draw()
            grass7.draw()
            #spda1.draw()
            #spda2.draw()
            #spda3.draw()
            #spda4.draw()
            #spda5.draw()
            #spda6.draw()
            #spda7.draw()
            #spda8.draw()
            wpda1.draw()
            wpda2.draw()
            screen.blit(level, ((screen.get_width() - level.get_width()) // 2, 0))
            character.draw()

            if countdown.countdown():
                end_num = 0
                break

            if grass1.hit_by(character) or grass2.hit_by(character) or grass3.hit_by(
                    character) or grass4.hit_by(character) or grass5.hit_by(character) or grass6.hit_by(
                    character) or grass7.hit_by(character):
                end_num = 1
                break

            #if spda1.hit_by(character) or spda2.hit_by(character) or spda3.hit_by(character) or spda4.hit_by(
            #        character) or spda5.hit_by(character) or spda6.hit_by(character) or spda7.hit_by(
            #        character) or spda8.hit_by(character) or wpda1.hit_by(character) or wpda2.hit_by(character):
            #    end_num = 2
            #    break

            if wpda1.hit_by(character) or wpda2.hit_by(character):
                end_num = 2
                break

            if character.x == screen.get_width() - character.image.get_width():
                screen_four_done = True
                break

            pygame.display.update()

    level_text = "5. EMMET"
    level = ui_font.render(level_text, True, (255, 255, 255))


    """Screen 5 (Level 5: EMMET)"""
    if screen_four_done:
        character.x = 0
        character.y = 290
        emmet_sound = pygame.mixer.Sound("emmetrocket.mp3")
        emmet_sound.play()
        fire_time = time.time()
        grass1 = Grass(screen, 0, 0, 640, 80)
        grass2 = Grass(screen, 0, 400, 640, 80)
        grass3 = Grass(screen, 0, 80, 80, 200)
        grass4 = Grass(screen, 0, 320, 120, 80)
        grass5 = Grass(screen, 120, 120, 100, 280)
        grass6 = Grass(screen, 260, 80, 100, 280)
        grass7 = Grass(screen, 400, 120, 100, 280)
        grass8 = Grass(screen, 540, 80, 100, 160)
        grass9 = Grass(screen, 500, 280, 140, 120)
        spda1.move(450, 110)
        spda2.move(480, 150)
        spda3.move(525, 360)
        spda4.move(491, 310)
        spda5.move(430, 270)
        spda6.move(370, 240)
        spda7.move(310, 220)
        spda8.move(250, 210)
        wpda1.move(150, 180)
        wpda2.move(430, 240)
        emmet = Emmet(screen, 200, 10)
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

            wpda1.walk_x(150, 430)
            wpda2.walk_x(150, 430)
            emmet.move(50, 540)
            grass1.draw()
            grass2.draw()
            grass3.draw()
            grass4.draw()
            grass5.draw()
            grass6.draw()
            grass7.draw()
            grass8.draw()
            grass9.draw()
            #spda1.draw()
            #spda2.draw()
            #spda3.draw()
            #spda4.draw()
            #spda5.draw()
            #spda6.draw()
            #spda7.draw()
            #spda8.draw()
            wpda1.draw()
            wpda2.draw()
            if int(time.time() - fire_time) % 2 == 0:
                new_rocket = Rocket(emmet.screen, emmet.x + 28, emmet.y + emmet.image.get_height() - 15, (emmet.image.get_width() / 4),
                                    emmet.image.get_height)
            if time.time() - fire_time > 2:
                new_rocket.draw()
                new_rocket.move()
            emmet.draw()
            screen.blit(level, ((screen.get_width() - level.get_width()) // 2, 0))
            character.draw()

            if countdown.countdown():
                end_num = 0
                break

            if grass1.hit_by(character) or grass2.hit_by(character) or grass3.hit_by(
                    character) or grass4.hit_by(character) or grass5.hit_by(character) or grass6.hit_by(
                    character) or grass7.hit_by(character) or grass8.hit_by(character) or grass9.hit_by(character):
                end_num = 1
                break

            #if spda1.hit_by(character) or spda2.hit_by(character) or spda3.hit_by(character) or spda4.hit_by(
            #        character) or spda5.hit_by(character) or spda6.hit_by(character) or spda7.hit_by(
            #        character) or spda8.hit_by(character)
            #    end_num = 2
            #    break

            if wpda1.hit_by(character) or wpda2.hit_by(character):
                end_num = 2
                break

            if new_rocket.hit_by(character):
                end_num = 4
                break

            if character.x == screen.get_width() - character.image.get_width():
                end_num = 3
                break

            pygame.display.update()

    pygame.mixer.music.stop()
    end_time = time.time()

    if end_num == 0:
        pygame.mixer.music.load("timer_end_music.mp3")
        pygame.mixer.music.play(0)
        message_text = ""
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            if time.time()-5 < end_time:
                message_text = "You were late for the morning meeting."
                screen.blit(eathan_angry, (0, 0))
            elif time.time()-10 < end_time:
                message_text = "You know what happens now..."
                screen.blit(eathan_angry, (0, 0))
            elif time.time()-15 < end_time:
                message_text = ""
                pygame.mixer.music.fadeout(2000)
            else:
                message_text = "VAN CLEANUP!!!"
                screen.blit(dirty_van, (0, 0))
            end_caption = font.render(message_text, True, (255, 255, 255))
            screen.blit(end_caption, ((screen.get_width() - end_caption.get_width())/2, screen.get_height() - 55))
            pygame.display.update()

    if end_num == 1:
        pygame.mixer.music.load("grasshole.mp3")
        pygame.mixer.music.play(0)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))
            screen.blit(emmet_jumpscare, (0, 0))
            pygame.display.update()

    if end_num == 2:
        pygame.mixer.music.load("nopda.mp3")
        pygame.mixer.music.play(0)
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
        pygame.mixer.music.play(0)
        finish_time = int(end_time - start_time)
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
                message_text = f"You made it in {finish_time} seconds"
            screen.blit(eathan_happy, (0, 0))
            end_caption = font.render(message_text, True, (255, 255, 255))
            screen.blit(end_caption, ((screen.get_width() - end_caption.get_width()) / 2, screen.get_height() - 55))
            pygame.display.update()

    if end_num == 4:
        pygame.mixer.music.load("death_sound.mp3")
        pygame.mixer.music.play(0)
        wasted = pygame.image.load("wasted.png")
        wasted = pygame.transform.scale(wasted, (screen.get_width(), screen.get_height()))
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.blit(wasted, (0, 0))

            pygame.display.update()

    if end_num == 5:
        print("Something went wrong")

main()