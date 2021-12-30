import pygame as pg
import sys
import random

from pygame.constants import KEYDOWN

#Základní parametry
pg.init()
screen = pg.display.set_mode((350, 525))
pg.display.set_caption("My 1st game")
clock = pg.time.Clock()


class Variables():
    font_30 = pg.font.Font("Font/UpheavalPro.ttf", 30)
    font_40 = pg.font.Font("Font/UpheavalPro.ttf", 40)
    font_10 = pg.font.Font("Font/UpheavalPro.ttf", 15)

    red_dot = pg.image.load("Veci/red_dot.jpg").convert_alpha()
    red_dot_r = red_dot.get_rect(center=(75, 525/2))

    prekazka_bot =pg.image.load("Veci/prekazky/1.jpg").convert_alpha()

    prekazka_top = pg.image.load("Veci/prekazky/2.jpg").convert_alpha()
    prekazky_r_list=[]

    game_active=False
    skore=0
    gravitace=0


    jump_timer = pg.USEREVENT + 1
    pg.time.set_timer(jump_timer, 150)


    prekazky_timer=pg.USEREVENT + 2
    pg.time.set_timer(prekazky_timer,2750)

    score_timer= pg.USEREVENT + 3
    pg.time.set_timer(score_timer, 2262)
class Intro_or_Outro_and_Score():
    
    def intro():
        screen.fill("grey")
        redot_intro = Variables.red_dot.get_rect(center= (350/2, 525/2))
        screen.blit(Variables.red_dot, redot_intro)
        font_intro = Variables.font_40.render("Red Dot", False, "red")
        font_intro_r = font_intro.get_rect(midtop=(175, 20))
        screen.blit(font_intro, font_intro_r)
        press_start = Variables.font_10.render("Pro spuštění stiskni libovolnou klávesu", False, "red")
        press_start_rect = press_start.get_rect(midtop=(175, 300))
        screen.blit(press_start, press_start_rect)
    
    def score():
        skore = Variables.font_30.render(f"Skóre: {Variables.skore}", False, "red")
        skore_r = skore.get_rect(topleft= (20, 20))
        screen.blit(skore, skore_r)
        return skore



# class red dot
class Reddot():
    def gravitace():
            Variables.gravitace += 0.9
            Variables.red_dot_r.y += Variables.gravitace
            if Variables.red_dot_r.bottom >= 525:
                Variables.red_dot_r.bottom =525
            if Variables.red_dot_r.top <= 0:
                Variables.red_dot_r.top = 0
    
    def jump():
        keys= pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            Variables.gravitace = -7


    def update():
        Reddot.gravitace()
        Reddot.jump()

class Prekazky():
    def prekazka(prekazky_list):
        if prekazky_list:
            for prekazky in prekazky_list:
                prekazky.x -= 4.1
                screen.blit(Variables.prekazka_bot, prekazky)
                screen.blit(Variables.prekazka_top, prekazky)

            prekazky_list= [prekazky for prekazky in prekazky_list if prekazky.x <0 ]    
            return prekazky_list
        else:
            return []

    def dotyk(redot, prekazka):
        if prekazka:
            for x in prekazka:
                if redot.colliderect(x):
                    return False
        else:
            return True
    def update():
        Prekazky.prekazka(Variables.prekazky_r_list)

class main():
    def obraz():
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()


                if event.type == Variables.prekazky_timer:
                    y_pos = random.randint(700, 1000)
                    Variables.prekazky_r_list.append(Variables.prekazka_bot.get_rect(midbottom=(500, y_pos)))
                    Variables.prekazky_r_list.append(Variables.prekazka_top.get_rect(midbottom=(500, y_pos - 600)))

                if event.type == pg.KEYDOWN:
                    Variables.game_active = True
                
                if event.type == Variables.score_timer:
                    Variables.skore+=1
                if event.type == pg.MOUSEBUTTONDOWN:
                    Variables.gravitace = -10

            if Variables.game_active:
                screen.fill("black")
                screen.blit(Variables.red_dot, Variables.red_dot_r)
                Reddot.update()
                Prekazky.update()
                skore = Intro_or_Outro_and_Score.score()
            else:
                Variables.prekazky_r_list.clear()
                Intro_or_Outro_and_Score.intro()

            
            pg.display.update()
            clock.tick(60)
main.obraz()