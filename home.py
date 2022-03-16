import os
import sys

import pygame
from pygame.locals import *
pygame.init()


def screenDisplay(size, text, pos):
    font = pygame.font.SysFont("curlz", size)
    text = font.render(text, True, (125, 125, 125))
    textRect = text.get_rect()
    textRect.center = pos
    start_screen.blit(text, textRect)


circle_x = 505
circle_move = 0.5

while True:

    start_screen = pygame.display.set_mode((1000, 500))
    pygame.draw.rect(start_screen, (0, 255, 0), pygame.Rect(100, 50, 800, 120), 100)
    pygame.display.set_caption("Craig Pong")

    screenDisplay(100, "CRAIG PONG", (500, 100))

    starter = pygame.draw.rect(start_screen, (0, 255, 255), pygame.Rect(218, 350, 220, 60), 100)  # 295
    screenDisplay(50, "2 Players", (323, 380))
    level1 = pygame.draw.rect(start_screen, (0, 255, 255), pygame.Rect(562, 350, 220, 60), 100)  # 295
    screenDisplay(50, "1 Player", (677, 380))

    pygame.draw.rect(start_screen, (255, 0, 0), pygame.Rect(438, 250, 5, 40))
    pygame.draw.rect(start_screen, (255, 0, 0), pygame.Rect(557, 250, 5, 40))
    circle = pygame.draw.circle(start_screen, (100, 200, 100), (circle_x, 270), 10)
    circle_x += circle_move
    if circle_x == 453:
        circle_move = 0.5
    elif circle_x == 547:
        circle_move = -0.5

    for position in pygame.event.get():
        place = pygame.mouse.get_pos()
        if position.type == pygame.MOUSEBUTTONDOWN and starter.collidepoint(place):
            if position.button == 1:
                pygame.quit()
                os.system("python multiplayer.py")
                sys.exit()

        if position.type == pygame.MOUSEBUTTONDOWN and level1.collidepoint(place):
            if position.button == 1:
                pygame.quit()
                os.system("python level1.py")
                sys.exit()

        if position.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
