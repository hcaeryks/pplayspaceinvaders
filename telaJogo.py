from PPlay.animation import Animation
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sound import *
import globalVars as gv

class Jogo(object):
    def __init__(self, janela):
        self.janela = janela
        self.keyboard = Keyboard()
        self.ship = Sprite("./assets/ship.png")
        self.ship.set_position(janela.width/2-self.ship.width/2, janela.height-janela.height/100-self.ship.height)
        self.laser = Animation("./assets/laser.png", 12, False)
        self.laser.set_total_duration(2000)
        self.laser.stop()
        self.laserSound = Sound("./assets/explosion.ogg")
        self.bullets = []
        self.downspeed = 0
        self.aMovCd = 0.25
        self.aMovCdCurr = self.aMovCd
        if gv.GAME_DIFFICULTY == 0:
            self.speed = 400
            self.bspeed = 1300
            self.aspeed = 20
            self.cooldown = 0.25
            self.aliencnt = 10
        elif gv.GAME_DIFFICULTY == 1:
            self.speed = 700
            self.bspeed = 1000
            self.aspeed = 60
            self.cooldown = 0.5
            self.aliencnt = 21
        elif gv.GAME_DIFFICULTY == 2:
            self.speed = 1000
            self.bspeed = 700
            self.aspeed = 180
            self.cooldown = 1.0
            self.aliencnt = 32
        elif gv.GAME_DIFFICULTY == 3:
            self.speed = 1300
            self.bspeed = 400
            self.aspeed = 540
            self.cooldown = 2
            self.aliencnt = 45
        self.spCdCurr = self.cooldown * 6
        self.cooldownCurr = self.cooldown
        self.aliens = [Sprite("./assets/alien.png") for i in range(self.aliencnt)]
        self.setAlienPos()
        self.next = True

    def update(self):
        self.ship.draw()
        [e.draw() for e in self.aliens]
        
        if self.keyboard.key_pressed("SPACE") and self.cooldown == self.cooldownCurr:
            tiro = Sprite("./assets/bullet.png")
            tiro.x = self.ship.x + self.ship.width/2 - tiro.width/2
            tiro.y = self.ship.y
            self.bullets.append(tiro)
            self.cooldownCurr -= self.janela.delta_time()
        elif self.keyboard.key_pressed("LEFT_SHIFT") and self.spCdCurr == self.cooldown * 6:
            self.laser.stop()
            self.laser.play()
            self.laserSound.play()
            self.spCdCurr -= self.janela.delta_time()


        if self.cooldownCurr < self.cooldown * 6 and self.spCdCurr > 0:
            self.cooldownCurr -= self.janela.delta_time()
        if self.spCdCurr < self.cooldown * 6 and self.spCdCurr > 0:
            self.spCdCurr -= self.janela.delta_time()

        if self.cooldownCurr <= 0:
            self.cooldownCurr = self.cooldown
        if self.spCdCurr <= 0:
            self.spCdCurr = self.cooldown * 6

        if self.keyboard.key_pressed("LEFT"):
            self.ship.x -= self.speed * self.janela.delta_time()
        elif self.keyboard.key_pressed("RIGHT"):
            self.ship.x += self.speed * self.janela.delta_time()

        if self.ship.x > self.janela.width - self.ship.width:
            self.ship.x = self.janela.width - self.ship.width
        elif self.ship.x < 0:
            self.ship.x = 0
        
        for alien in self.aliens:
            if self.next:
                if alien.x + alien.width >= self.janela.width:
                    self.aspeed *= -1
                    self.downspeed = 50
                    self.next = False
                    break
            else:
                if alien.x <= 0:
                    self.aspeed *= -1
                    self.downspeed = 50
                    self.next = True
                    break
        
        if self.aMovCdCurr <= 0: self.aMovCdCurr = self.aMovCd
        if self.aMovCdCurr == self.aMovCd:
            for i in range(len(self.aliens)):
                self.aliens[i].draw()
                self.aliens[i].x += (self.aspeed / 10)
                self.aliens[i].y += self.downspeed
            self.downspeed = 0
        self.aMovCdCurr -= self.janela.delta_time()

        n = 0
        for i in range(len(self.bullets)):
            self.bullets[i+n].y -= self.bspeed * self.janela.delta_time()
            self.bullets[i+n].draw()
            if self.bullets[i+n].y < 0:
                self.bullets.pop(i+n)
                n -= 1

        self.laser.draw()
        self.laser.set_position(self.ship.x + self.ship.width/2 - 150/2, self.ship.y - 1000)
        if self.laser.is_playing(): self.laser.update()

    def setAlienPos(self):
        col = 0
        if self.aliencnt == 10: col = 5
        elif self.aliencnt == 21: col = 7
        elif self.aliencnt == 32: col = 8
        elif self.aliencnt == 45: col = 9
        for i in range(int(self.aliencnt/col)):
            ypos = i * self.aliens[0].width
            for e in range(0, int(col*self.aliens[0].width)*2, int(self.aliens[0].width)*2):
                self.aliens[int((e/(self.aliens[0].width * 2)) + (i*col))].set_position((1600/2) - ((col * (self.aliens[0].width * 2))/2) - (self.aliens[0].width/2) + e, 50 + ypos)