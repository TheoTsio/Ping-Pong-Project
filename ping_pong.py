from typing import Any
from pygame import *

window = display.set_mode((700, 500))
window.fill((190, 20, 70))

#parent class for sprites
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Racket_L(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += self.speed 


class Racket_R(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed 


racket_l = Racket_L('racket.png', 30, 200, 4, 50, 150)
racket_r = Racket_R('racket.png', 620, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)




font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

game = True
clock = time.Clock()
FPS = 60 # Frames Per Second

speed_x = 3 
speed_y = 3
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    window.fill((190, 20, 70))
    if finish != True:
        racket_l.reset()
        racket_l.update()

        racket_r.reset()
        racket_r.update()

        ball.reset()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y

    if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
        speed_x = speed_x * (-1)

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y = speed_y * (-1) # speed_y *= -1

    if ball.rect.x < 0:
        finish = True 
        window.blit(lose1, (200, 200))

    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))

    clock.tick(FPS)
    display.update()