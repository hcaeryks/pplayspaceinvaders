from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
import globals as gv

class Dificuldade(object):
    def __init__(self, janela):
        self.janela = janela
        self.janela.set_title(gv.GAME_TITLE + " - Seleção de Dificuldade")
        self.dificuldades = Sprite("./assets/dificuldades.png")
        self.btnFacil = Sprite("./assets/btnFacil.png")
        self.btnFacilLit = Sprite("./assets/btnFacil-lit.png")
        self.btnMedio = Sprite("./assets/btnMedio.png")
        self.btnMedioLit = Sprite("./assets/btnMedio-lit.png")
        self.btnDificil = Sprite("./assets/btnDificil.png")
        self.btnDificilLit = Sprite("./assets/btnDificil-lit.png")
        self.btnInsano = Sprite("./assets/btnInsano.png")
        self.btnInsanoLit = Sprite("./assets/btnInsano-lit.png")
        self.mouse = Mouse()

        self.section = gv.GAME_HEIGHT/8
        self.dificuldades.set_position(gv.GAME_WIDTH/2 - self.dificuldades.width/2, gv.GAME_HEIGHT/4 - self.dificuldades.height/2)
        self.btnFacil.set_position(self.section * 3, gv.GAME_HEIGHT/2 - self.btnFacil.height/2)
        self.btnFacilLit.set_position(self.section * 3 + 4, gv.GAME_HEIGHT/2 - self.btnFacilLit.height/2)
        self.btnMedio.set_position(gv.GAME_WIDTH - self.btnMedio.width - self.section * 3 - 6, gv.GAME_HEIGHT/2 - self.btnMedio.height/2)
        self.btnMedioLit.set_position(gv.GAME_WIDTH - self.btnMedioLit.width - self.section * 3 - 5 - 6, gv.GAME_HEIGHT/2 - self.btnMedioLit.height/2)
        self.btnDificil.set_position(self.section * 3, gv.GAME_HEIGHT/2 + self.btnDificil.height/2)
        self.btnDificilLit.set_position(self.section * 3, gv.GAME_HEIGHT/2 + self.btnDificilLit.height/2)
        self.btnInsano.set_position(gv.GAME_WIDTH - self.btnInsano.width - self.section * 3, gv.GAME_HEIGHT/2 + self.btnInsano.height/2)
        self.btnInsanoLit.set_position(gv.GAME_WIDTH - self.btnInsanoLit.width - self.section * 3, gv.GAME_HEIGHT/2 + self.btnInsanoLit.height/2)
        pass

    def update(self):
        self.dificuldades.draw()
        self.btnFacil.draw()
        self.btnMedio.draw()
        self.btnDificil.draw()
        self.btnInsano.draw()
        if self.mouse.is_over_object(self.btnFacil):
            self.btnFacilLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 1
                gv.GAME_DIFFICULTY = 0
        elif self.mouse.is_over_object(self.btnMedio):
            self.btnMedioLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 1
                gv.GAME_DIFFICULTY = 1
        elif self.mouse.is_over_object(self.btnDificil):
            self.btnDificilLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 1
                gv.GAME_DIFFICULTY = 2
        elif self.mouse.is_over_object(self.btnInsano):
            self.btnInsanoLit.draw()
            if self.mouse.is_button_pressed(1):
                gv.GAME_SCREEN = 1
                gv.GAME_DIFFICULTY = 3
        pass