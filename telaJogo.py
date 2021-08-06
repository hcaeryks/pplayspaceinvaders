from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
import globalVars as gv

class Jogo(object):
    def __init__(self, janela):
        self.janela = janela
        self.keyboard = Keyboard()
        self.ship = Sprite("./assets/ship.png")
        self.ship.set_position(janela.width/2-self.ship.width/2, janela.height-janela.height/100-self.ship.height)
        self.bullets = []
        self.downspeed = 200

        if gv.GAME_DIFFICULTY == 0:
            self.speed = 400
            self.bspeed = 1300
            self.aspeed = 20
            self.cooldown = 0.25
            self.cooldownCurr = 0.25
            self.aliencnt = 10
        elif gv.GAME_DIFFICULTY == 1:
            self.speed = 700
            self.bspeed = 1000
            self.aspeed = 60
            self.cooldown = 0.5
            self.cooldownCurr = 0.5
            self.aliencnt = 21
        elif gv.GAME_DIFFICULTY == 2:
            self.speed = 1000
            self.bspeed = 700
            self.aspeed = 180
            self.cooldown = 1.0
            self.cooldownCurr = 1.0
            self.aliencnt = 32
        elif gv.GAME_DIFFICULTY == 3:
            self.speed = 1300
            self.bspeed = 400
            self.aspeed = 540
            self.cooldown = 2
            self.cooldownCurr = 2
            self.aliencnt = 45

        self.aliens = [Sprite("./assets/alien.png") for i in range(self.aliencnt)]
        self.downspeed = 0
        self.setAlienPos()

    def update(self):
        self.ship.draw()
        [e.draw() for e in self.aliens]
        
        if self.keyboard.key_pressed("SPACE") and self.cooldown == self.cooldownCurr:
            tiro = Sprite("./assets/bullet.png")
            tiro.x = self.ship.x + self.ship.width/2 - tiro.width/2
            tiro.y = self.ship.y
            self.bullets.append(tiro)
            self.cooldownCurr -= self.janela.delta_time()

        if self.cooldownCurr < self.cooldown and self.cooldownCurr > 0:
            self.cooldownCurr -= self.janela.delta_time()

        if self.cooldownCurr <= 0:
            if gv.GAME_DIFFICULTY == 0:
                self.cooldownCurr = 0.25
            elif gv.GAME_DIFFICULTY == 1:
                self.cooldownCurr = 0.5
            elif gv.GAME_DIFFICULTY == 2:
                self.cooldownCurr = 1
            elif gv.GAME_DIFFICULTY == 3:
                self.cooldownCurr = 2

        if self.keyboard.key_pressed("LEFT"):
            self.ship.x -= self.speed * self.janela.delta_time()
        elif self.keyboard.key_pressed("RIGHT"):
            self.ship.x += self.speed * self.janela.delta_time()

        if self.ship.x > self.janela.width - self.ship.width:
            self.ship.x = self.janela.width - self.ship.width
        elif self.ship.x < 0:
            self.ship.x = 0

        n, changed = 0, False
        for i in range(len(self.aliens)):
            self.aliens[i].draw()
            self.aliens[i].x += self.aspeed * self.janela.delta_time()
            self.aliens[i].y += abs(self.downspeed) * self.janela.delta_time()
            if not changed and (self.aliens[i].x + self.aliens[i].width > self.janela.width or self.aliens[i].x < 0):
                self.aspeed *= -1
                self.downspeed = 30
                changed = True
            if self.aliens[i].x + self.aliens[i].width > self.janela.width: self.aliens[i].x = self.janela.width - self.aliens[i].width
            elif self.aliens[i].x < 0: self.aliens[i].x = 0

        self.downspeed -= abs(self.downspeed) * self.janela.delta_time()
        if self.downspeed <= 0: self.downspeed = 0
        n = 0
        for i in range(len(self.bullets)):
            self.bullets[i+n].y -= self.bspeed * self.janela.delta_time()
            self.bullets[i+n].draw()
            if self.bullets[i+n].y < 0:
                self.bullets.pop(i+n)
                n -= 1

    def setAlienPos(self):
        col = 0
        if self.aliencnt == 10: col = 5
        elif self.aliencnt == 21: col = 7
        elif self.aliencnt == 32: col = 8
        elif self.aliencnt == 45: col = 9
        ypos = 0
        print(self.aliencnt/col)
        for i in range(int(self.aliencnt/col)):
            ypos = i * 100
            for e in range(0, col*100, 100):
                self.aliens[int((e/100) + (i*col))].set_position((1600/2) - ((col * 100)/2) - (self.aliens[0].width/2) + e, 50 + ypos)