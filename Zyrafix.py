import random
import sys
import time
import pygame
import pygame.gfxdraw

from math import *
from pygame.locals import *

#Block of CONST

FPS = 20
WINWIDTH = 1280
WINHEIGHT = 720
RADIUS = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
P1COLOUR = BLUE
P2COLOUR = GREEN
P3COLOUR = RED

def main():
    global FPS_CLOCK, SCREEN, DISPLAY, exite_pos, play_pos
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WINWIDTH,WINHEIGHT),DOUBLEBUF)
    DISPLAY = pygame.display.get_surface()
    pygame.display.set_caption('Achtung die Kurve')
    play = pygame.image.load('playnow.png')
    exite = pygame.image.load('exit.png')
    DISPLAY.blit(play, (500, 200))
    DISPLAY.blit(exite, (500, 350))
    pygame.display.flip()
    play_pos = Rect(500, 200, 226, 75)
    exite_pos = Rect(500, 350, 226, 75)
    
    while True:
        input(pygame.event.get())
        
def input(events):
    for event in events:
        #if event.type == pygame.quit():
            #sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if pygame.mouse.get_pressed()[0] and play_pos.collidepoint(mouse_pos):
                 print("Hi")
            elif pygame.mouse.get_pressed()[0] and exite_pos.collidepoint(mouse_pos):
                sys.exit(0)
        
        
class Player(object):
    def __init__(self):
        self.running = True
        self.colour = None
        self.score = 0

    def gen(self):
        self.x = random.randrange(50, WINWIDTH - 165)
        self.y = random.randrange(50, WINHEIGHT - 50)
        self.angle = random.randrange(0, 360)

    def move(self):
        self.x += int(RADIUS * 2 * cos(radians(self.angle)))
        self.y += int(RADIUS * 2 * sin(radians(self.angle)))

    def draw(self):
        pygame.gfxdraw.aacircle(DISPLAYSURF, self.x, self.y, RADIUS, self.colour)
        pygame.gfxdraw.filled_circle(DISPLAYSURF, self.x, self.y, RADIUS, self.colour)

main()
