import pygame
import sys
from pygame.locals import *

pygame.init()
resolution = (1280, 720)
window = pygame.display.set_mode(resolution, DOUBLEBUF)
pygame.display.set_caption('Achtung die Kurve')
tlo=pygame.image.load('playnow.png')
wyjscie=pygame.image.load('exit.png')
# kappa
screen = pygame.display.get_surface()
screen.blit(tlo,(500,200))
screen.blit(wyjscie,(500,350))
pygame.display.flip()


def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print(event)
while True:
    input(pygame.event.get())
