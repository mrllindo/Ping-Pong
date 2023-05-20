import pygame
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((900,500))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()
game_status = "Game"
font = pygame.freetype.Font(None, 30)

player = pygame.rect.Rect(10, 200, 5, 100)
player2 = pygame.rect.Rect(885, 200, 5, 100)
ball = pygame.rect.Rect(425, 225, 25, 25)

ball_speed_x = 5
ball_speed_y = 5
score = [0, 0]

def ball_respawn():
    global game_status
    ball.center = (450, 250)

def ball_check():
    global ball_speed_y
    global ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
    if ball.bottom >= 500:
        ball_speed_y = - ball_speed_y
    if ball.colliderect(player2) or ball.colliderect(player):
        ball_speed_x = -ball_speed_x
    if ball.right < 0:
        score[1] += 1
        ball_respawn()
    if ball.left > 900:
        score[0] += 1
        ball_respawn()

game = True
FPS = 90

player_y= 0
player2_y = 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_y -=  4
            if event.key == pygame.K_s:
                player_y +=  4
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_y +=  4
            if event.key == pygame.K_s:
                player_y -=  4

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_y -=  4
            if event.key == pygame.K_DOWN:
                player2_y +=  4
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player2_y +=  4
            if event.key == pygame.K_DOWN:
                player2_y -=  4



    player.y += player_y
    player2.y += player2_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    ball_check()
    screen.fill((0, 0, 0))

    font.render_to(screen, (440, 20), str(score[0])+ ':' +str(score[1]), (255,255,255))

    pygame.draw.rect(screen, (20, 200, 20), player)
    pygame.draw.rect(screen, (200, 20, 20), player2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    pygame.display.flip()
    clock.tick(FPS)
