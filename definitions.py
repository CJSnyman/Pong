import pygame
from pygame.locals import *
import sys
import math
import random


def end():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def distance(x1, x2, y1, y2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


def ball_movement():
    if random.randint(1, 2) == 1:
        return 1
    else:
        return -1
