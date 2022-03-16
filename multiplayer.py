import pygame
from pygame.locals import *
import definitions
import sys
import os

pygame.init()


def screenDisplay(size, text, pos):
    font = pygame.font.SysFont("curlz", size, True)
    text = font.render(text, True, (255, 0, 255))
    textRect = text.get_rect()
    textRect.center = pos
    multi_screen.blit(text, textRect)


def finish():
    screenDisplay(50, "REPLAY", (323, 380))
    screenDisplay(50, "HOME", (677, 380))


plank_left_x = 108
plank_left_y = 200

plank_right_x = 872
plank_right_y = 200

ball_x = 500
ball_y = 250

plank_speed = 1
ball_speed_y = definitions.ball_movement()
ball_speed_x = definitions.ball_movement()

red_point = 0
blue_point = 0

countdown = 3

while True:
    multi_screen = pygame.display.set_mode((1000, 500))
    multi_screen.fill((59, 161, 52))
    middle_line = pygame.Rect(495, 0, 10, 500)
    pygame.draw.rect(multi_screen, (255, 255, 255), middle_line)

    screenDisplay(40, str(red_point), (460, 25))
    screenDisplay(40, str(blue_point), (540, 25))

    pygame.draw.line(multi_screen, (255, 255, 255), (44, 50), (956, 50), 14)
    pygame.draw.line(multi_screen, (255, 255, 255), (44, 450), (956, 450), 14)
    pygame.draw.line(multi_screen, (150, 255, 150), (950, 44), (950, 456), 14)
    pygame.draw.line(multi_screen, (150, 255, 150), (50, 44), (50, 456), 14)

    plank_left = pygame.Rect(plank_left_x, plank_left_y, 20, 100)
    pygame.draw.rect(multi_screen, (200, 0, 0), plank_left)

    plank_right = pygame.Rect(plank_right_x, plank_right_y, 20, 100)
    pygame.draw.rect(multi_screen, (0, 0, 200), plank_right)

    ball = pygame.draw.circle(multi_screen, (100, 100, 100), (ball_x, ball_y), 25)

    if blue_point == 0 and red_point == 0:
        while countdown > 0:
            screenDisplay(100, str(countdown), (500, 100))
            countdown -= 1
            pygame.display.update()
            pygame.time.delay(1000)
            multi_screen = pygame.display.set_mode((1000, 500))
            multi_screen.fill((59, 161, 52))
            middle_line = pygame.Rect(495, 0, 10, 500)
            pygame.draw.rect(multi_screen, (255, 255, 255), middle_line)

            screenDisplay(40, str(red_point), (460, 25))
            screenDisplay(40, str(blue_point), (540, 25))

            pygame.draw.line(multi_screen, (255, 255, 255), (44, 50), (956, 50), 14)
            pygame.draw.line(multi_screen, (255, 255, 255), (44, 450), (956, 450), 14)
            pygame.draw.line(multi_screen, (150, 255, 150), (950, 44), (950, 456), 14)
            pygame.draw.line(multi_screen, (150, 255, 150), (50, 44), (50, 456), 14)

            plank_left = pygame.Rect(plank_left_x, plank_left_y, 20, 100)
            pygame.draw.rect(multi_screen, (200, 0, 0), plank_left)

            plank_right = pygame.Rect(plank_right_x, plank_right_y, 20, 100)
            pygame.draw.rect(multi_screen, (0, 0, 200), plank_right)

            ball = pygame.draw.circle(multi_screen, (100, 100, 100), (ball_x, ball_y), 25)

    move = pygame.key.get_pressed()

    if move[K_d] and plank_left_x < 475:
        plank_left_x += plank_speed
    if move[K_a] and plank_left_x > 58:
        plank_left_x -= plank_speed
    if move[K_w] and plank_left_y > 58:
        plank_left_y -= plank_speed
    if move[K_s] and plank_left_y < 344:
        plank_left_y += plank_speed

    if move[K_RIGHT] and plank_right_x < 923:
        plank_right_x += plank_speed
    if move[K_LEFT] and plank_right_x > 505:
        plank_right_x -= plank_speed
    if move[K_UP] and plank_right_y > 58:
        plank_right_y -= plank_speed
    if move[K_DOWN] and plank_right_y < 344:
        plank_right_y += plank_speed

    ball_y += ball_speed_y
    ball_x += ball_speed_x

    if ball_y < 80:
        if ball_speed_y < 0:
            ball_speed_y *= -1
    if ball_y > 422:
        if ball_speed_y > 0:
            ball_speed_y *= -1

    if ball_x < 35:
        blue_point += 1
        if blue_point < 5:
            plank_left_x = 108
            plank_left_y = 200

            plank_right_x = 872
            plank_right_y = 200

            ball_x = 500
            ball_y = 250

            plank_speed = 1
            ball_speed_y = definitions.ball_movement()
            ball_speed_x = definitions.ball_movement()

    elif ball_x > 965:
        red_point += 1
        if red_point < 5:
            plank_left_x = 108
            plank_left_y = 200

            plank_right_x = 872
            plank_right_y = 200

            ball_x = 500
            ball_y = 250

            plank_speed = 1
            ball_speed_y = definitions.ball_movement()
            ball_speed_x = definitions.ball_movement()

    if blue_point == 5:
        if red_point == 0:
            screenDisplay(60, "BLUE WINS", (500, 180))
            screenDisplay(60, "WHITEWASH", (500, 250))
        else:
            screenDisplay(60, "BLUE WINS", (500, 250))
        replay = pygame.draw.rect(multi_screen, (100, 100, 100), pygame.Rect(215, 350, 220, 60))
        home = pygame.draw.rect(multi_screen, (100, 100, 100), pygame.Rect(560, 350, 220, 60))
        finish()
        plank_left_x = 108
        plank_left_y = 200

        plank_right_x = 872
        plank_right_y = 200

        ball_x = 500
        ball_y = 250

        plank_speed = 0
        ball_speed_x = 0
        ball_speed_y = 0

    elif red_point == 5:
        if blue_point == 0:
            screenDisplay(60, "RED WINS", (500, 180))
            screenDisplay(60, "WHITEWASH", (500, 250))
        else:
            screenDisplay(60, "RED WINS", (500, 250))
        replay = pygame.draw.rect(multi_screen, (100, 100, 100), pygame.Rect(215, 350, 220, 60))
        home = pygame.draw.rect(multi_screen, (100, 100, 100), pygame.Rect(560, 350, 220, 60))
        finish()
        plank_left_x = 108
        plank_left_y = 200

        plank_right_x = 872
        plank_right_y = 200

        ball_x = 500
        ball_y = 250

        plank_speed = 0
        ball_speed_x = 0
        ball_speed_y = 0

    ball_speed_x *= 1.0001
    ball_speed_y *= 1.0001

    if plank_left_y < ball_y < plank_left_y + 100 and 0 < ball_x - plank_left_x - 20 < 25:
        if ball_speed_x < 0:
            ball_speed_x *= -1
    if plank_right_y < ball_y < plank_right_y + 100 and 0 < plank_right_x - ball_x < 25:
        if ball_speed_x > 0:
            ball_speed_x *= -1

    if plank_left_x < ball_x < plank_left_x + 20 and 0 < plank_left_y - ball_y < 25:
        if ball_speed_y > 0:
            ball_speed_y *= -1
    if plank_left_x < ball_x < plank_left_x + 20 and 0 < ball_y - plank_left_y < 25:
        if ball_speed_y < 0:
            ball_speed_y *= -1

    if plank_right_x < ball_x < plank_right_x + 20 and 0 < plank_right_y - ball_y < 25:
        if ball_speed_y > 0:
            ball_speed_y *= -1
    if plank_right_x < ball_x < plank_right_x + 20 and 0 < ball_y - plank_right_y < 25:
        if ball_speed_y < 0:
            ball_speed_y *= -1

    if 0 < definitions.distance(plank_left.topright[0], ball_x, plank_left.topright[1], ball_y) < 25:
        ball_speed_x *= -1
        if ball_speed_y > 0:
            ball_speed_y *= -1
    if 0 < definitions.distance(plank_left.bottomright[0], ball_x, plank_left.bottomright[1], ball_y) < 25:
        ball_speed_x *= -1
        if ball_speed_y < 0:
            ball_speed_y *= -1

    if 0 < definitions.distance(plank_right.topright[0], ball_x, plank_right.topright[1], ball_y) < 25:
        ball_speed_x *= -1
        if ball_speed_y > 0:
            ball_speed_y *= -1
    if 0 < definitions.distance(plank_right.bottomright[0], ball_x, plank_right.bottomright[1], ball_y) < 25:
        ball_speed_x *= -1
        if ball_speed_y < 0:
            ball_speed_y *= -1

    if red_point < 5 and blue_point < 5:
        red_quit = pygame.draw.rect(multi_screen, (100, 100, 100), pygame.Rect(2, 2, 60, 40))
        blue_quit = pygame.draw.rect(multi_screen, (100, 100, 100), pygame.Rect(938, 2, 60, 40))
        screenDisplay(18, "RED", (32, 12))
        screenDisplay(18, "QUIT", (32, 32))
        screenDisplay(18, "BLUE", (970, 12))
        screenDisplay(18, "QUIT", (970, 32))

    for position in pygame.event.get():
        place = pygame.mouse.get_pos()
        if red_point == 5 or blue_point == 5:
            # noinspection PyUnboundLocalVariable
            if position.type == pygame.MOUSEBUTTONDOWN and home.collidepoint(place):
                if position.button == 1:
                    pygame.quit()
                    os.system("python play.py")
                    sys.exit()

            # noinspection PyUnboundLocalVariable
            if position.type == pygame.MOUSEBUTTONDOWN and replay.collidepoint(place):
                plank_speed = 1
                ball_speed_y = definitions.ball_movement()
                ball_speed_x = definitions.ball_movement()

                red_point = 0
                blue_point = 0

                countdown = 3

        if red_point < 5 and blue_point < 5:
            # noinspection PyUnboundLocalVariable
            if position.type == pygame.MOUSEBUTTONDOWN and red_quit.collidepoint(place):
                blue_point = 5

            elif position.type == pygame.MOUSEBUTTONDOWN and blue_quit.collidepoint(place):
                red_point = 5

        if position.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
