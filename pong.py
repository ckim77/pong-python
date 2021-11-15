import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((750, 500))

pygame.display.set_caption("Pong")

white = (255, 255, 255)
black = (0, 0, 0)
fpsClock = pygame.time.Clock()
fps = 30



class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.score = 0
        self.dx = 1
        self.dy = 1

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1

paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

paddle_speed = 25

ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

def reset():
    window.fill(black)
    
    # font render
    font = pygame.font.SysFont("Constantia", 30)
    text = font.render("Pong", False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    
    #render on screen
    window.blit(text, textRect)

    #scores
    p1_score = font.render(str(paddle1.score), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    window.blit(p1_score, p1Rect)

    p2_score = font.render(str(paddle2.score), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    window.blit(p2_score, p2Rect)


    all_sprites.draw(window)
    pygame.display.update()



run = True

while run:
    fpsClock.tick(fps)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y -= paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y -= paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle_speed

    ball.rect.x += ball.speed * ball.dx
    ball.rect.y += ball.speed * ball.dy

    # bounds collision for ball
    if ball.rect.y > 490:
        ball.dy = -1
    
    if ball.rect.x > 740:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = -1
        paddle1.score += 1
    
    if ball.rect.y < 10:
        ball.dy = 1
    
    if ball.rect.x < 10:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = 1
        paddle2.score += 1
    
    if paddle1.rect.y > 490:
        paddle1.dy = -1
    
    
    # paddle collide code
    if paddle1.rect.colliderect(ball.rect):
        ball.dx = 1
    
    if paddle2.rect.colliderect(ball.rect):
        ball.dx = -1

    reset()
    
pygame.quit()