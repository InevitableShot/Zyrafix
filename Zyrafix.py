import pygame
import sys
from pygame.locals import *

pygame.init()
resolution = (1280, 720)
window = pygame.display.set_mode(resolution, DOUBLEBUF)
pygame.display.set_caption('Achtung die Kurve')
play=pygame.image.load('playnow.png')
wyjscie=pygame.image.load('exit.png')
#tlo
screen = pygame.display.get_surface()
screen.blit(play,(500,200))
screen.blit(wyjscie,(500,350))
pygame.display.flip()
play_pos = Rect(500,200,226,75)
wyjscie_pos = Rect(500,350,226,75)

def input(events):
    for event in events:
        #if event.type == EXIT:
            #sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if pygame.mouse.get_pressed()[0] and play_pos.collidepoint(mouse_pos):
                print("Hi")
            elif pygame.mouse.get_pressed()[0] and wyjscie_pos.collidepoint(mouse_pos):
                sys.exit(0)
        """else:
            print(event)"""
while True:
    input(pygame.event.get())


