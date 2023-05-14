from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed  

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

class Ball(GameSprite):
    def balll(self):
        if self.rect.y < 0:
            self.rect.y +=  self.speed
        if self.rect.y < win_height - 25:
            self.rect.y -= self.speed

win_widht = 700
win_height = 500

window = display.set_mode((win_widht, win_height))
display.set_caption("Ping Pong")
background = transform.scale(image.load('b.jpg'), (700, 500))

player1 = Player('Palka.jpg', 25, 150, 4, 10, 150)
player2 = Player2('Palka.jpg', 650, 150, 4, 10, 150)
ball =  Ball('Ball.png', 350, 250, 5, 25, 25)


finish = False
game = True
clock = time.Clock()
FPS = 60

while game :
    for e in event.get():
        if e.type == QUIT:
            game = False  



    if not finish:
        window.blit(background, (0, 0))

        ball.balll()
        ball.update()
        ball.reset()

        player1.update()
        player1.reset()

        player2.update()
        player2.reset()

    clock.tick(FPS)
    display.update()
