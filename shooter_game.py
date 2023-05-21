#Створи власний Шутер!

from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image= transform.scale(image.load(player_image),(size_x,size_y))
        self.speed= player_speed
        self.rect= self.image.get_rect()
        self.rect.x =player_x
        self.rect.y =player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <450 :
            self.rect.y += self.speed
    def fire(self):
        bullet =Bullet('bullet.png',self.rect.x+15,self.rect.y,20,40,50)
        bullets.add(bullet)
lost=0
class Enemy(GameSprite):
   
    def update(self):
        global lost
        self.rect.y += 5
        if self.rect.y >500:
            self.rect.x = randint(80,600)
            self.rect.y =0
            lost+=1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 10
        if self.rect.y <0:
            self.kill()
window=display.set_mode((700,500))
display.set_caption("shyter")

background = transform.scale(image.load("galaxy.jpg"),(700,500))

font.init()
font1=font.SysFont('Arial',80)
win = font1.render('YOU WIN',True,(225,225,225))
win = font1.render('YOU LOSE',True,(180,0,0))
font2 = font.SysFont('Arial',36)
clock=time.Clock()
game = True

FPS = 60
finish = False

ship = Player("rocket.png",300, 400,60,100, 10)
monsters = sprite.Group()

for i in range (1,6):
    monster =Enemy("ufo.png",randint(80,600),-80,60,60,randint(1,5))
    monsters.add(monster)
bullets = sprite.Group()
score=0
lost=0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
    if finish!=True:
        window.blit(background,(0,0))
        text = font2.render('shet:' +str(score),1,(225,225,225))
        window.blit(text,(10,20))

        text_lose = font2.render('propusheno:'+str(lost),1,(225,225,225))




   
   
        monsters.draw(window)
        monsters.update()
        ship.reset()
        ship.update()
        bullets.draw(window)
        bullets.update()
        collides = sprite.groupcollide(monsters,bullets,True,True)
        for c in collides:
            monster = Enemy("ufo.png", randint(80,600),-40,60,60,randint(1,5)) 
            monsters.add(monster)
        if sprite.spritecollide(ship,monsters, False):
            finish=True




    display.update()
    time.delay(50)
    clock.tick(FPS)