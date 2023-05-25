from pygame import *
from random import *

mixer.init()
font.init()

init()

wind = display.set_mode((700,500))
display.set_caption('Шутер')

COLOR = (0,255,0)
lost = 0
tyu = 0

class GameS(sprite.Sprite):
    def __init__(self, cart, x, y, sx,sy,  speed):
        super().__init__()
        self.image = transform.scale(image.load(cart),(sx,sy))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        wind.blit(self.image,(self.rect.x, self.rect.y))

class Playr(GameS):
    def __init__(self, cart, x, y, sx,sy,  speed):
        super().__init__( cart, x, y, sx,sy,  speed)
    def update(self):
        keys = key.get_pressed()

        if keys[K_d] and self.rect.x < 615:
            self.rect.x +=7

        if keys[K_a] and self.rect.x > 5:
            self.rect.x -=7
    def fires(self):
        bull = Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20,8)
        bl.add(bull)
        

class Enemy(GameS):
    def __init__(self, cart, x, y, sx,sy,  speed):
        super().__init__( cart, x, y, sx,sy,  speed)
        self.speed = speed
        self.direction = 1
        self.q = 3

    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(70,630)
            lost = lost + 1

class Bullet(GameS):
    def update(self):
        global tyu
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
      

        
    
        


baru = transform.scale(image.load('galaxy.jpg'),(700,500))
pl = Playr('rocket.png',550,405,80,90,3)

bl = sprite.Group()

mots = sprite.Group()
for i in range(1,6):
    r = randint(70,630)
    q = randint(1, 2)
    mon = Enemy('ufo.png', r, 50,80,65, q)
    mots.add(mon)

clock = time.Clock()
FPS = 60

game = True
finish = False

mixer.music.load('space.ogg')
mixer.music.play()

fire = mixer.Sound('fire.ogg')

font = font.SysFont('Arial',30)
wer = font.render('YOU WIN',True,COLOR)
lor = font.render('YOU LOSE',True,COLOR)

game = True
finish = False

while game:
    keys = key.get_pressed()
    for i in event.get():
            if i.type == QUIT:
                game = False
            if keys[K_SPACE]:
                fire.play()
                pl.fires()
                
    if finish != True:
        wind.blit(baru,(0,0))
        pl.reset()
        mots.draw(wind)
        bl.draw(wind)

        lose = font.render('Пропущенно:' + str(lost),True,COLOR)
        wine = font.render('Убито:',True,COLOR)

        wind.blit(wine,(10,10))
        wind.blit(lose,(10,30))

        pl.update()
        mots.update()
        
        bl.update()

       
        
    clock.tick(FPS)

    display.update()
