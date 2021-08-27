from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import globals as gv
import pygame

class Ranking(object):
    def __init__(self, janela):
        self.janela = janela
        self.rankingtitle = Sprite("./assets/btnRanking-lit.png")
        self.rankingtitle.set_position(gv.GAME_WIDTH/2 - self.rankingtitle.width/2, gv.GAME_HEIGHT/6 - self.rankingtitle.height)

        self.ranking = None
        self.twidth = [50, 50, 50, 50, 50]
        with open("scores.txt", 'r') as scores:
            self.ranking = scores.read().split('\n')
            self.ranking.pop(-1)

        self.ranking = [(e.split('#')[0], e.split('#')[1]) for e in self.ranking]
        self.ranking.sort(key=lambda x: int(x[1]), reverse=True)
        for i in range(5 if len(self.ranking) >= 5 else len(self.ranking)):
            text = f"{self.ranking[i][0]} - {self.ranking[i][1]}"
            font = pygame.font.Font("./assets/space_invaders.ttf", 50)
            self.ranking[i] = font.render(text, True, (255, 255, 255))
            self.twidth[i] = font.size(text)[0]
        pass

    def update(self):
        self.rankingtitle.draw()
        for i in range(5 if len(self.ranking) >= 5 else len(self.ranking)):
            self.janela.screen.blit(self.ranking[i], [gv.GAME_WIDTH/2-(self.twidth[i])/2, gv.GAME_HEIGHT/6 + 50 + (i*100)])
        pass