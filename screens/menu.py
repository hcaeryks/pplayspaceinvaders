from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import globals as gv

class Menu(object):
    def __init__(self, janela):
        self.janela = janela
        self.janela.set_title(gv.GAME_TITLE + " - Menu")
        self.logo = Sprite("./assets/logo.png")
        self.erro = Sprite("./assets/erro.png")
        self.btnJogar = Sprite("./assets/btnJogar.png")
        self.btnJogarLit = Sprite("./assets/btnJogar-lit.png")
        self.btnDificuldade = Sprite("./assets/btnDificuldade.png")
        self.btnDificuldadeLit = Sprite("./assets/btnDificuldade-lit.png")
        self.btnRanking = Sprite("./assets/btnRanking.png")
        self.btnRankingLit = Sprite("./assets/btnRanking-lit.png")
        self.btnSair = Sprite("./assets/btnSair.png")
        self.btnSairLit = Sprite("./assets/btnSair-lit.png")
        self.mouse = Mouse()

        self.logo.set_position(gv.GAME_WIDTH/2 - self.logo.width/2, gv.GAME_HEIGHT/4 - self.logo.height/2)
        self.erro.set_position(gv.GAME_WIDTH/2 - self.btnRanking.width/2, gv.GAME_HEIGHT/2 + 85 * 2)
        self.btnJogar.set_position(gv.GAME_WIDTH/2 - self.btnJogar.width/2, gv.GAME_HEIGHT/2 )
        self.btnJogarLit.set_position(gv.GAME_WIDTH/2 - self.btnJogarLit.width/2, gv.GAME_HEIGHT/2)
        self.btnDificuldade.set_position(gv.GAME_WIDTH/2 - self.btnDificuldade.width/2, gv.GAME_HEIGHT/2 + 85)
        self.btnDificuldadeLit.set_position(gv.GAME_WIDTH/2 - self.btnDificuldadeLit.width/2, gv.GAME_HEIGHT/2 + 85)
        self.btnRanking.set_position(gv.GAME_WIDTH/2 - self.btnRanking.width/2, gv.GAME_HEIGHT/2 + 85 * 2)
        self.btnRankingLit.set_position(gv.GAME_WIDTH/2 - self.btnRankingLit.width/2, gv.GAME_HEIGHT/2 + 85 * 2)
        self.btnSair.set_position(gv.GAME_WIDTH/2 - self.btnSair.width/2, gv.GAME_HEIGHT/2 + 85 * 3)
        self.btnSairLit.set_position(gv.GAME_WIDTH/2 - self.btnSairLit.width/2, gv.GAME_HEIGHT/2 + 85 * 3)
        pass

    def update(self):
        self.logo.draw()
        self.btnJogar.draw()
        self.btnDificuldade.draw()
        self.btnRanking.draw()
        self.btnSair.draw()
        if self.mouse.is_over_object(self.btnJogar):
            self.btnJogarLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 4
        elif self.mouse.is_over_object(self.btnDificuldade):
            self.btnDificuldadeLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 2
        elif self.mouse.is_over_object(self.btnRanking):
            self.btnRankingLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 3
        elif self.mouse.is_over_object(self.btnSair):
            self.btnSairLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 5
        pass