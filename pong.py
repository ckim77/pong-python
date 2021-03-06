import pygame, sys, random

#setup
pygame.init()
clock = pygame.time.Clock()


def ball_animation ():
    global ball_speed_x, ball_speed_y, player_score, cpu_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_restart()

    if ball.right >= screen_width:
        cpu_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1

def player_animation ():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def cpu_animation ():
    if cpu.top < ball.y:
        cpu.top += cpu_speed
    if cpu.bottom > ball.y:
        cpu.bottom -= cpu_speed
    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_height:
        cpu.bottom = screen_height

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

#setting up game board

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#setting up the rectangles for the game
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
cpu = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('blue')
light_grey = (200,200,200)

# game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
cpu_speed = 30

# text variables
player_score = 0
cpu_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Timer
current_time = 0
button_press_time = 0

while True and current_time < 10000:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            if event.key == pygame.K_DOWN:
                player_speed += 15
            if event.key == pygame.K_UP:
                player_speed -= 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 15
            if event.key == pygame.K_UP:
                player_speed += 15
        
    
        

    ball_animation()
    player_animation()
    cpu_animation()
    
    #timer
    current_time = pygame.time.get_ticks()


    #display code
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, cpu)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))

    cpu_text = game_font.render(f"{cpu_score}", False, light_grey)
    screen.blit(cpu_text,(600, 470))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(cpu_score)
