

import pygame
import math
import random

RED = (255, 0, 0)
BLUE = (135,206,235)

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

pos_new_red = [random.randint(0,800),random.randint(0,600)]
pos_old_red = pos_new_red
pos_new_blue = [random.randint(0,800),random.randint(0,600)]
pos_old_blue = pos_new_blue

speed_red = 5.0
speed_blue = 5.0
angle_red = random.randint(0,360)
angle_blue = random.randint(0,360)

running = True

while running:

# events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        angle_red -= 10
    if keys[pygame.K_a]:
        angle_blue -=10
    if keys[pygame.K_RIGHT]:
        angle_red += 10
    if keys[pygame.K_d]:
        angle_blue += 10

# przekroczenie kąta

    if angle_red >= 360:
        angle_red -= 360
    elif angle_red < 0:
        angle_red += 360
    if angle_blue >= 360:
        angle_blue -= 360
    elif angle_blue < 0:
        angle_blue += 360

    print
    angle_red,angle_blue

    pos_new_red[0] += int(speed_red * math.cos(math.radians(angle_red)))
    pos_new_blue[0] += int(speed_blue * math.cos(math.radians(angle_blue)))
    pos_new_red[1] += int(speed_red * math.sin(math.radians(angle_red)))
    pos_new_blue[1] += int(speed_blue * math.sin(math.radians(angle_blue)))

# rysuje

    if pos_new_red != pos_old_red:
        pygame.draw.line(screen, RED, pos_new_red, pos_old_red)
    pos_old_red = pos_new_red[:]
    if pos_new_blue != pos_old_blue:
        pygame.draw.line(screen, BLUE, pos_new_blue, pos_old_blue)
    pos_old_blue = pos_new_blue[:]

    pygame.display.flip()

# FPS

    clock.tick(30)

pygame.quit()