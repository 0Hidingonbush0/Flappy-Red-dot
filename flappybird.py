import pygame as pg
import sys

#Základní parametry
pg.init()
screen = pg.display.set_mode((350, 525))
pg.display.set_caption("My 1st game")



class Variables():
    font_69 = pg.font.Font("Font/UpheavalPro.ttf", 60)
    font_40 = pg.font.Font("Font/UpheavalPro.ttf", 60)

    red_dot = pg.image.load("Veci/red_dot.jpg").convert_alpha()
    red_dot_r = red_dot.get_rect(center=(50, 525/2))

    game_active=True
    skore=0


class Intro_or_Outro():
    
    def intro(font_intro):
        screen.fill("grey")
        screen.blit(Reddot.red_dot, Reddot.red_dot_r)
        font_intro = Variables.font_69.render("Red Dot", False, "red")
        font_intro_r = font_intro.get_rect(midtop=(175, 20))
        screen.blit(font_intro, font_intro_r)
        press_start = Variables.font_69.render("Pro spuštění stiskni libovolnou klávesu", False, "red")
        press_start_rect = press_start.get_rect(midtop=(175, 200))
        screen.blit(press_start, press_start_rect)


# class red dot
class Reddot():
    def gravitace():
        Variables.red_dot.y +=1
        if Variables.red_dot.y > 525:
            Variables.red_dot.y ==525
    
class main():
    def obraz():
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

                screen.fill("black")
                screen.blit(Variables.red_dot, Variables.red_dot_r)
        

            
            pg.display.update()
Reddot.obraz()