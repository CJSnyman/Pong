import os
import pygame
import sys
from pygame.locals import *
import definitions
import random

pygame.init()


def display(size, text, pos):
    font = pygame.font.SysFont("curlz", size, True)
    text = font.render(text, True, (255, 0, 255))
    textRect = text.get_rect()
    textRect.center = pos
    level1_display.blit(text, textRect)


def finish():
    display(50, "REPLAY", (125, 400))
    display(50, "HOME", (375, 400))


def next_stage():
    display(50, "CONTINUE", (250, 400))
    display(50, "HOME", (250, 500))


block_x = [100, 200, 300, 400]  # [51, 51, 51, 51, 101, 151, 201, 251, 301, 351, 401, 401, 401, 401]
block_y = [100, 200, 200, 100]  # [251, 201, 151, 101, 51, 51, 51, 51, 51, 51, 101, 151, 201, 251]

ball_x, ball_y = 250, 540
ball_speed_x = definitions.ball_movement()
ball_speed_y = random.randint(5, 15) / 10
plank_x, plank_y = 200, 565
plank_speed = 1
i = 0
countdown = 3
pause = False

while True:
    level1_display = pygame.display.set_mode((500, 650))
    level1_display.fill((0, 150, 255))
    pygame.draw.line(level1_display, (200, 200, 200), (0, 500), (500, 500), 5)
    pygame.draw.rect(level1_display, (235, 109, 0), pygame.Rect(plank_x, plank_y, 100, 20))
    ball = pygame.draw.circle(level1_display, (255, 0, 0), (ball_x, ball_y), 25)

    for event in pygame.event.get():
        place = pygame.mouse.get_pos()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not pause:
                    pause = True
                else:
                    pause = False

        if ball_y > 675 or pause:
            if event.type == MOUSEBUTTONDOWN and home.collidepoint(place):
                pygame.quit()
                os.system("python play.py")
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and replay.collidepoint(place):
                block_x = [100, 200, 300, 400]
                block_y = [100, 200, 200, 100]
                ball_x, ball_y = 250, 540
                ball_speed_x = definitions.ball_movement()
                ball_speed_y = random.randint(5, 15) / 10
                plank_x, plank_y = 200, 565
                plank_speed = 1
                i = 0
                countdown = 3
                pause = False

        if len(block_x) == 0:
            if event.type == MOUSEBUTTONDOWN and main_menu.collidepoint(place):
                pygame.quit()
                os.system("python play.py")
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and next_stage_button.collidepoint(place):
                pygame.quit()
                os.system("python level2.py")
                sys.exit()

    if pause and ball_speed_y != 0:
        for i in range(len(block_x)):
            j = len(block_x) - i - 1
            square = pygame.draw.rect(level1_display, (0, 0, 0), pygame.Rect(block_x[j], block_y[j], 48, 48))
        display(100, "PAUSED", (250, 255))
        display(30, "(CONTINUE PRESS 'P')", (250, 325))
        replay = pygame.draw.rect(level1_display, (100, 100, 100), pygame.Rect(10, 370, 230, 70))
        home = pygame.draw.rect(level1_display, (100, 100, 100), pygame.Rect(260, 370, 230, 70))
        finish()

    else:
        display(30, "PAUSE PRESS 'P'", (130, 630))
        if countdown == 3:
            while countdown > 0:
                level1_display.fill((0, 150, 255))
                pygame.draw.line(level1_display, (200, 200, 200), (0, 500), (500, 500), 5)
                pygame.draw.rect(level1_display, (235, 109, 0), pygame.Rect(plank_x, plank_y, 100, 20))
                ball = pygame.draw.circle(level1_display, (255, 0, 0), (ball_x, ball_y), 25)
                for i in range(len(block_x)):
                    j = len(block_x) - i - 1
                    square = pygame.draw.rect(level1_display, (0, 0, 0), pygame.Rect(block_x[j], block_y[j], 48, 48))
                display(100, str(countdown), (250, 325))
                pygame.display.update()
                pygame.time.delay(1000)
                countdown -= 1

        for i in range(len(block_x)):
            j = len(block_x) - i - 1
            square = pygame.draw.rect(level1_display, (0, 0, 0), pygame.Rect(block_x[j], block_y[j], 48, 48))
            if block_x[j] < ball_x < block_x[j] + 48:
                if 0 < block_y[j] - ball_y < 25 and ball_speed_y > 0:
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
                elif 0 < ball_y - square.bottomleft[1] < 25 and ball_speed_y < 0:
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
            elif block_y[j] < ball_y < block_y[j] + 48:
                if 0 < block_x[j] - ball_x < 25 and ball_speed_x > 0:
                    ball_speed_x *= -1
                    del block_x[j]
                    del block_y[j]
                elif 0 < ball_x - square.topright[0] < 25 and ball_speed_x < 0:
                    ball_speed_x *= -1
                    del block_x[j]
                    del block_y[j]
            elif 0 < definitions.distance(ball_x, square.topleft[0], ball_y, square.topleft[1]) < 25:
                if ball_speed_x < 0 and ball_speed_y > 0:
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x > 0 and ball_speed_y > 0:
                    ball_speed_x *= -1
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x > 0 and ball_speed_y < 0:
                    ball_speed_x *= -1
                    del block_x[j]
                    del block_y[j]
            elif 0 < definitions.distance(ball_x, square.topright[0], ball_y, square.topright[1]) < 25:
                if ball_speed_x < 0 and ball_speed_y > 0:
                    ball_speed_x *= -1
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x > 0 and ball_speed_y > 0:
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x < 0 and ball_speed_y < 0:
                    ball_speed_x *= -1
                    del block_x[j]
                    del block_y[j]
            elif 0 < definitions.distance(ball_x, square.bottomleft[0], ball_y, square.bottomleft[1]) < 25:
                if ball_speed_x < 0 and ball_speed_y < 0:
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x > 0 and ball_speed_y > 0:
                    ball_speed_x *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x > 0 and ball_speed_y < 0:
                    ball_speed_x *= -1
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
            elif 0 < definitions.distance(ball_x, square.bottomright[0], ball_y, square.bottomright[1]) < 25:
                if ball_speed_x < 0 and ball_speed_y > 0:
                    ball_speed_x *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x < 0 and ball_speed_y < 0:
                    ball_speed_x *= -1
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
                elif ball_speed_x > 0 and ball_speed_y < 0:
                    ball_speed_y *= -1
                    del block_x[j]
                    del block_y[j]
            i += 1

        move = pygame.key.get_pressed()
        if move[K_UP] and plank_y > 503:
            plank_y -= plank_speed
        if move[K_DOWN] and plank_y < 630:
            plank_y += plank_speed
        if move[K_LEFT] and plank_x > 0:
            plank_x -= plank_speed
        if move[K_RIGHT] and plank_x < 400:
            plank_x += plank_speed

        ball_y += ball_speed_y
        ball_x += ball_speed_x
        if ball_x < 0 + 25 and ball_speed_x < 0:
            ball_speed_x *= -1
        elif ball_x > 500 - 25 and ball_speed_x > 0:
            ball_speed_x *= -1
        if ball_y < 0 + 25 and ball_speed_y < 0:
            ball_speed_y *= -1

        if plank_x < ball_x < plank_x + 100 and 20 < plank_y - ball_y < 25:
            if ball_speed_y > 0:
                ball_speed_y *= -1

        if plank_y < ball_y < plank_y + 20 and 20 < plank_x - ball_x < 25:
            if ball_speed_x > 0:
                ball_speed_x *= -1
        if plank_y < ball_y < plank_y + 20 and 20 < ball_x - plank_x + 100 < 25:
            if ball_speed_x < 0:
                ball_speed_x *= -1

        if 20 < definitions.distance(ball_x, plank_x, ball_y, plank_y) < 25 and ball_speed_y > 0:
            ball_speed_y *= -1
            if ball_speed_x > 0:
                ball_speed_x *= -1
        if 20 < definitions.distance(ball_x, plank_x + 100, ball_y, plank_y) < 25 and ball_speed_y > 0:
            ball_speed_y *= -1
            if ball_speed_x < 0:
                ball_speed_x *= -1

    if ball_y > 675:
        ball_speed_x = 0
        ball_speed_y = 0
        plank_speed = 0
        display(80, "GAME OVER", (250, 310))
        pygame.draw.rect(level1_display, (0, 150, 255), pygame.Rect(0, 610, 260, 40))
        replay = pygame.draw.rect(level1_display, (100, 100, 100), pygame.Rect(10, 370, 230, 70))
        home = pygame.draw.rect(level1_display, (100, 100, 100), pygame.Rect(260, 370, 230, 70))
        finish()

    if len(block_x) == 0:
        ball_speed_x = 0
        ball_speed_y = 0
        plank_speed = 0
        level1_display.fill((0, 150, 255))
        pygame.draw.line(level1_display, (200, 200, 200), (0, 500), (500, 500), 5)
        pygame.draw.rect(level1_display, (235, 109, 0), pygame.Rect(plank_x, plank_y, 100, 20))
        ball = pygame.draw.circle(level1_display, (255, 0, 0), (ball_x, ball_y), 25)
        display(50, "LEVEL 1 COMPLETE", (250, 325))
        next_stage_button = pygame.draw.rect(level1_display, (100, 100, 100), pygame.Rect(100, 370, 300, 70))
        main_menu = pygame.draw.rect(level1_display, (100, 100, 100), pygame.Rect(100, 470, 300, 70))
        next_stage()
        pygame.display.update()

    pygame.display.update()
