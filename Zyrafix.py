import pygame
import sys
from pygame.locals import *

pygame.init()
resolution = (1280, 720)
window = pygame.display.set_mode(resolution, DOUBLEBUF)
pygame.display.set_caption('Achtung die Kurve')
# tlo=pygame.image.load()
# kappa
screen = pygame.display.get_surface()


def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print(event)
while True:
    input(pygame.event.get())
