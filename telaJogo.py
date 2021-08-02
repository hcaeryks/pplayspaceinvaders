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
        self.ship.set_position(janela.width/2-self.ship.width/2, janela.height-janela.height/12-self.ship.height)
        self.bullets = []

        if gv.GAME_DIFFICULTY == 0:
            self.speed = 400
            self.bspeed = 1300
            self.cooldown = 0.25
            self.cooldownCurr = 0.25
        elif gv.GAME_DIFFICULTY == 1:
            self.speed = 700
            self.bspeed = 1000
            self.cooldown = 0.5
            self.cooldownCurr = 0.5
        elif gv.GAME_DIFFICULTY == 2:
            self.speed = 1000
            self.bspeed = 700
            self.cooldown = 1.0
            self.cooldownCurr = 1.0
        elif gv.GAME_DIFFICULTY == 3:
            self.speed = 1300
            self.bspeed = 400
            self.cooldown = 2
            self.cooldownCurr = 2

    def update(self):
        self.ship.draw()
        print(self.cooldown)
        
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

        n = 0
        for i in range(len(self.bullets)):
            self.bullets[i+n].y -= self.bspeed * self.janela.delta_time()
            self.bullets[i+n].draw()
            if self.bullets[i+n].y < 0:
                self.bullets.pop(i+n)
                n -= 1