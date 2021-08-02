from PPlay.sprite import Sprite
from random import randint

class FlyingAlien(Sprite):
    def __init__(self):
        Sprite.__init__(self, "./assets/alien.png")
        self.xspeed = randint(-150, -20) if randint(0, 1) else randint(20, 150)
        self.yspeed = randint(-150, -20) if randint(0, 1) else randint(20, 150)
        

    def update(self, time):
        self.x += self.xspeed * time
        self.y += self.yspeed * time