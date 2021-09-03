from PPlay import window, keyboard
from screens import menu, dificuldade, ranking, jogonew
import globals as g
import os.path

screen = window.Window(g.GAME_WIDTH, g.GAME_HEIGHT)
screen.set_title(g.GAME_TITLE)

scrdificuldades = dificuldade.Dificuldade(screen)
scrranking = None
scrmenu = menu.Menu(screen)
scrjogo = None

kb = keyboard.Keyboard()
currGme = 0

if not os.path.isfile("scores.txt"):
    f = open("scores.txt", "x")
    f.close()

while g.GAME_SCREEN > 0 and g.GAME_SCREEN < 5:
    screen.set_background_color(g.GAME_BACKGROUNDCOLOR)
    if currGme == 0 and g.GAME_SCREEN == 4:
        currGme = 4
        scrjogo = jogonew.Jogo(screen)
    elif currGme == 4 and g.GAME_SCREEN != 4:
        currGme = 0

    if currGme == 0 and g.GAME_SCREEN == 3:
        currGme = 3
        scrranking = ranking.Ranking(screen)
    elif currGme == 3 and g.GAME_SCREEN != 3:
        currGme = 0

    if g.GAME_SCREEN == 1:
        scrmenu.update()
    elif g.GAME_SCREEN == 2:
        scrdificuldades.update()
    elif g.GAME_SCREEN == 3:
        scrranking.update()
    elif g.GAME_SCREEN == 4:
        scrjogo.update()

    if kb.key_pressed("ESC"):
        g.GAME_SCREEN = 1

    screen.update()