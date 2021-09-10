from PPlay.sprite import Sprite
from math import log
from random import randint
from PPlay.keyboard import Keyboard
import globals as g
import time

class Jogo():
    def __init__(self, screen):
        self.screen = screen
        self.keyboard = Keyboard()
        self.ship = Sprite("./assets/ship.png")
        self.ship.set_position(self.screen.width / 2 - self.ship.width/2,
                               self.screen.height-self.screen.height/100-self.ship.height)
        self.relogio, self.frames, self.fps = 0, 0, "Calculando..."
        self.bullets = []
        self.abullets = []
        self.aliens = []
        self.points = 0
        self.lifes = 5
        self.invul = 0
        self.invflash = 0
        self.invbool = True
        self.next = True
        self.col = 0
        self.settings()
        self.setAlienPos()

    def update(self):
        self.relogio += self.screen.delta_time()
        self.frames += 1
        [[alien.draw() for alien in linha] for linha in self.aliens]
        self.lastshot += self.screen.delta_time()
        if self.invul > 0:
            self.invflash += self.screen.delta_time()
            self.invul -= self.screen.delta_time()
            if self.invflash >= 0.1:
                self.invflash = 0
                self.invbool = not self.invbool
        if self.invul <= 0 or self.invbool:
            self.ship.draw()

        if self.keyboard.key_pressed("SPACE") and self.cooldown == self.cooldownCurr:
            tiro = Sprite("./assets/bullet.png")
            tiro.x = self.ship.x + self.ship.width/2 - tiro.width/2
            tiro.y = self.ship.y
            self.bullets.append(tiro)
            self.cooldownCurr -= self.screen.delta_time()

        if self.keyboard.key_pressed("LEFT"):
            self.ship.x -= self.speed * self.screen.delta_time()
        elif self.keyboard.key_pressed("RIGHT"):
            self.ship.x += self.speed * self.screen.delta_time()

        self.checkBounds()

        if self.aMovCdCurr <= 0:
            self.aMovCdCurr = self.aMovCd
        if self.aMovCdCurr == self.aMovCd:
            for i in range(len(self.aliens)-1, -1, -1):
                for e in range(len(self.aliens[i])):
                    self.aliens[i][e].draw()
                    self.aliens[i][e].x += (self.aspeed / 10)
                    self.aliens[i][e].y += self.downspeed
            self.downspeed = 0
        self.aMovCdCurr -= self.screen.delta_time()

        if self.cooldownCurr < self.cooldown * 6:
            self.cooldownCurr -= self.screen.delta_time()
        if self.cooldownCurr <= 0:
            self.cooldownCurr = self.cooldown
        if self.aShootCdCurr < self.aShootCd and self.aShootCdCurr > 0 or self.aShootCdCurr > self.aShootCd:
            self.aShootCdCurr -= self.screen.delta_time()
        if self.aShootCdCurr <= 0:
            self.aShootCdCurr = self.aShootCd

        n = 0
        for i in range(len(self.bullets)):
            self.bullets[i+n].y -= self.bspeed * self.screen.delta_time()
            self.bullets[i+n].draw()
            if self.bullets[i+n].y < 0:
                self.bullets.pop(i+n)
                n -= 1

        n = 0
        for i in range(len(self.bullets)):
            br = False
            yt = self.aliens[0][0].y-30
            yb = 30+self.aliens[-1][0].y
            if self.bullets[i].y <= yb and self.bullets[i].y >= yt:
                for e in range(len(self.aliens)-1, -1, -1):
                    for a in range(len(self.aliens[e])):
                        if self.bullets[i-n].collided(self.aliens[e][a]):
                            self.aliens[e].pop(a)
                            self.bullets.pop(i-n)
                            if len(self.aliens[e]) == 0:
                                self.aliens.pop(e)
                            n += 1
                            br = True
                            multiplier = 0
                            if self.lastshot < self.cooldown * 2:
                                multiplier = 7
                            elif self.lastshot < self.cooldown * 4:
                                multiplier = 5
                            elif self.lastshot < self.cooldown * 6:
                                multiplier = 3
                            elif self.lastshot >= self.cooldown * 6:
                                multiplier = 2
                            self.points += int(10 * self.pointscalar * log(multiplier))
                            self.lastshot = 0
                            self.aspeed *= 1.1
                            self.aShootCd *= 0.95
                            break
                    if br:
                        break
                if br:
                    break

        if self.relogio >= 1:
            self.fps = self.frames
            self.relogio = 0
            self.frames = 0

        if len(self.aliens) == 0:
            #if self.aliencnt == 10: self.aliencnt = 21
            #elif self.aliencnt == 21: self.aliencnt = 32
            #elif self.aliencnt == 32: self.aliencnt = 45
            self.aliencnt += 4
            self.bspeed = 1300 - g.GAME_DIFFICULTY * 300 * 0.8
            self.aspeed = 20 * (3 ** g.GAME_DIFFICULTY) * 1.2
            self.cooldown = 0.25 * (2 ** g.GAME_DIFFICULTY) * 1.2
            self.pointscalar = log(g.GAME_DIFFICULTY + 2)
            self.aMovCd *= 0.90
            self.aShootCd *= 0.90
            self.aMovCdCurr = self.aMovCd
            self.aShootCdCurr = self.aShootCd
            #if g.GAME_DIFFICULTY != 3: g.GAME_DIFFICULTY += 1
            #self.settings()
            self.setAlienPos()

        if self.aShootCdCurr == self.aShootCd:
            m = randint(0, len(self.aliens)-1)
            n = randint(0, len(self.aliens[m])-1)
            tiro = Sprite("./assets/bullet.png")
            tiro.x = self.aliens[m][n].x
            tiro.y = self.aliens[m][n].y
            self.abullets.append(tiro)
            self.aShootCdCurr -= self.screen.delta_time()

        n = 0
        for i in range(len(self.abullets)):
            self.abullets[i+n].y += self.bspeed * self.screen.delta_time()
            self.abullets[i+n].draw()
            if self.abullets[i+n].collided(self.ship) and self.invul <= 0 and self.abullets[i+n].y > self.ship.y:
                self.abullets.pop(i+n)
                self.lifes -= 1
                self.ship.x = g.GAME_WIDTH/2 - self.ship.width/2
                self.invul = 2
                n -= 1
                if self.lifes == 0:
                    nome = input("Insira seu nome: ")
                    with open("scores.txt", 'a') as scores:
                        scores.write(f"{nome}#{self.points}\n")
                    g.GAME_SCREEN = 1
            elif self.abullets[i+n].y > g.GAME_HEIGHT:
                self.abullets.pop(i+n)
                n -= 1


        self.screen.draw_text(str(self.fps)+" FPS", 50,
                              170, 20, (255, 255, 255))
        self.screen.draw_text("PONTOS: "+str(self.points),
                              50, 50, 50, (255, 255, 255), "Impact")
        self.screen.draw_text("VIDAS: "+str(self.lifes),
                              50, 100, 50, (255, 255, 255), "Impact")


    def setAlienPos(self):
        self.col = int(self.aliencnt/4)
        self.aliens = [[Sprite("./assets/alien.png") for i in range(self.col)] for e in range(int(self.aliencnt/self.col))]
        for e in range(int(self.aliencnt/self.col)):
            for i in range(self.col):
                self.aliens[e][i].set_position(1600/2 - ((self.col * self.aliens[0][0].width * 2)/2) +
                                               self.aliens[0][0].width * 2 * i, 10 + 10 * e + self.aliens[0][0].height * e)
                self.aliens[e][i].draw()
                self.screen.update()
                time.sleep(0.1)

    def checkBounds(self):
        if self.ship.x > self.screen.width - self.ship.width:
            self.ship.x = self.screen.width - self.ship.width
        elif self.ship.x < 0:
            self.ship.x = 0

        for l in range(len(self.aliens)):
            first = self.aliens[l][0]
            last = self.aliens[l][-1]
            if self.next:
                if last.x + last.width >= self.screen.width:
                    print("wtf")
                    self.aspeed *= -1
                    self.downspeed = 50
                    self.next = not self.next
                    break
            else:
                if first.x <= 0:
                    print("wtf2")
                    self.aspeed *= -1
                    self.downspeed = 50
                    self.next = not self.next
                    break

    def settings(self):
        self.speed = 400 + g.GAME_DIFFICULTY * 300
        self.bspeed = 1300 - g.GAME_DIFFICULTY * 300
        self.aspeed = 20 * (3 ** g.GAME_DIFFICULTY)
        self.cooldown = 0.25 * (2 ** g.GAME_DIFFICULTY)
        self.pointscalar = log(g.GAME_DIFFICULTY + 2)
        if g.GAME_DIFFICULTY == 0:
            self.aliencnt = 12
        elif g.GAME_DIFFICULTY == 1:
            self.aliencnt = 20
        elif g.GAME_DIFFICULTY == 2:
            self.aliencnt = 28
        elif g.GAME_DIFFICULTY == 3:
            self.aliencnt = 36
        self.downspeed = 0
        self.lastshot = 0
        self.aMovCd = 0.25
        self.aShootCd = 1 * randint(1, 3)
        self.aMovCdCurr = self.aMovCd
        self.aShootCdCurr = self.aShootCd
        self.cooldownCurr = self.cooldown
