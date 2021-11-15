import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# create game loop

run = True
while run: