# import pygame
# from pygame.locals import *

# pygame.init()

# screen_width = 600
# screen_height = 500


# fpsClock = pygame.time.Clock()
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Pong")

# # define font
# font = pygame.font.SysFont("Constantia", 30)


# #game variables
# margin = 50
# cpu_score = 0
# player_score = 0
# fps = 60
# live_ball = False


# #coding colors
# bg = (50,25,50)
# white = (255, 255, 255)

# def draw_board():
#     screen.fill(bg)
#     pygame.draw.line(screen, white, (0, margin), (screen_width, margin), 2)


# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     screen.blit(img, (x, y))

# class paddle():
#     def __init__ (self, x, y):
#         self.x = x
#         self.y = y
#         self.rect = Rect(x, y, 20, 100)
#         self.speed = 5
#         self.ai_speed = 5

#     def move(self): 
#         key = pygame.key.get_pressed()
#         if key[pygame.K_UP] and self.rect.top > margin:
#             self.rect.move_ip(0, -1 * self.speed)
#         if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
#             self.rect.move_ip(0, 1 * self.speed)
        
#     def draw(self):
#         pygame.draw.rect(screen, white, self.rect)

# class ball ():
#     def __init__ (self, x, y):
#         self.reset(x, y)
#         self.x = x
#         self.y = y
#         self.ball_rad = 8
#         self.rect = Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
#         self.speed_x = -4
#         self.speed_y = 4
#         self.winner = 0
    
#     def move(self):

#         #check collision with borders
#         if self.rect.top < margin:
#             self.speed_y *= -1
        
#         if self.rect.bottom > margin:
#             self.speed_y *= -1
        
#         if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
#             self.speed_x *= -1
        
#         #check for out of bounds
#         if self.rect.left < 0:
#             self.winner = 1
#         if self.rect.left > screen_width:
#             self.winner = 1


#         self.rect.x += self.speed_x
#         self.rect.y += self.speed_y

#         return self.winner
    
#     def draw(self):
#         pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
    
#     def reset(self, x, y):
#         self.x = x
#         self.y = y
#         self.ball_rad = 8
#         self.rect = Rect(x, y, self.ball_rad * 2, self.ball_rad * 2)
#         self.speed_x = -4
#         self.speed_y = 4
#         self.winner = 0

# # create paddles
# player_paddle = paddle(screen_width - 40, screen_height // 2)
# cpu_paddle = paddle(20, screen_height // 2)

# # create pong ball
# pong = ball(screen_width - 60, screen_height // 2 + 50)

# # initialize game loop

# run = True
# while run:

#     fpsClock.tick(fps)

#     draw_board()
#     draw_text("CPU: " + str(cpu_score), font, white, 20, 15)
#     draw_text("P1: " + str(player_score), font, white, screen_width - 100, 15)

#     # ball display
#     pong.move()
#     pong.draw()

#     # paddles display
#     player_paddle.draw()
#     cpu_paddle.draw()

#     # move paddles
#     player_paddle.move()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
#             live_ball = True
#             pong.reset(screen_width -60, screen_height //2 + 50)
    

    
#     pygame.display.update()
    
# pygame.quit()

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((750, 500))

pygame.display.set_caption("Pong")

white = (255, 255, 255)
black = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.score = 0

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
    pygame.time.delay(100)

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

    # bounds collision
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
    
    # paddle collide code
    if paddle1.rect.colliderect(ball.rect):
        ball.dx = 1
    
    if paddle2.rect.colliderect(ball.rect):
        ball.dx = -1


    reset()
    
pygame.quit()