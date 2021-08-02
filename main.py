from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from random import randint

from telaMenu import Menu
from telaDificuldade import Dificuldade
from telaRanking import Ranking
from telaJogo import Jogo
from alien import FlyingAlien

import globalVars as gv

janela = Window(gv.GAME_WIDTH, gv.GAME_HEIGHT)
janela.set_title(gv.GAME_TITLE)

dificuldades = Dificuldade(janela)
ranking = Ranking(janela)
menu = Menu(janela)
jogo = None
currGme = 0

background = Sprite("./assets/bg.png")
#aliens = [FlyingAlien() for i in range(2**4)]
#[alien.set_position(randint(100, gv.GAME_WIDTH-100), randint(100, gv.GAME_HEIGHT-100)) for alien in aliens]
keyboard = Keyboard()

while gv.GAME_SCREEN > 0 and gv.GAME_SCREEN < 5:
    janela.set_background_color(gv.GAME_BACKGROUNDCOLOR)
    #[alien.update(janela.delta_time()) for alien in aliens]
    #[alien.draw() for alien in aliens]
    if gv.GAME_SCREEN >= 1 and gv.GAME_SCREEN <= 3:
        pass

    
    if currGme == 0 and gv.GAME_SCREEN == 4:
        currGme = 4
        jogo = Jogo(janela)
    elif currGme == 4 and gv.GAME_SCREEN != 4:
        currGme = 0

    if gv.GAME_SCREEN == 1:
        menu.update()
    elif gv.GAME_SCREEN == 2:
        dificuldades.update()
    elif gv.GAME_SCREEN == 3:
        ranking.update()
    elif gv.GAME_SCREEN == 4:
        jogo.update()

    if keyboard.key_pressed("ESC"):
        gv.GAME_SCREEN = 1

    janela.update()