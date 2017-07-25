import pygame
import time
import threading
import random

from flask import json
from pip._vendor import requests

pygame.init()

screen_width = 800
screen_height = 600

pygame.display.set_caption("Snake")
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

red = (255, 0, 0)
dark_red = (139, 0, 0)
green = (0, 255, 0)
dark_green = (0, 139, 50)
blue = (0, 0, 255)
dark_blue = (0, 0, 139)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
FPS = 10

clock = pygame.time.Clock()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.list = []
        self.direction = 0
        self.dict = {}


def ball(x, y, color):
    pygame.draw.circle(display, color, (int(x*20), y*20), 10)
    pygame.display.update()

s = Snake()
food = Point(random.randrange(1, 40), random.randrange(1, 30))
run = True


def collision():
    global run
    for point in s.list:
        if s.x == point.x and s.y == point.y:
            pygame.quit()
            run = False
            quit(0)
    if s.x < 0 or s.x > 40:
        pygame.quit()
        run = False
        quit(0)
    if s.y < 0 or s.y > 30:
        pygame.quit()
        run = False
        quit(0)


def query():
    snakeTemp =[]
    for p in s.list:
        snakeTemp.append({'x': p.x, 'y': p.y})
    requests.post("https://hiraparac2014.mybluemix.net/snake", json={'list': snakeTemp})
    requests.post("https://hiraparac2014.mybluemix.net/food", json={'food': {'x': food.x, 'y': food.y}})

def printer():
    ball(s.x, s.y, red)
    s.list.append(Point(s.x, s.y))
    s.x += 1
    ball(s.x, s.y, red)
    s.list.append(Point(s.x, s.y))
    s.x += 1
    ball(food.x, food.y, blue)
    while run:
        ball(s.x, s.y, red)
        s.list.append(Point(s.x, s.y))

        if s.direction == 0:
            s.x += 1
        elif s.direction == 1:
            s.y += 1
        elif s.direction == 2:
            s.x -= 1
        elif s.direction == 3:
            s.y -= 1

        if s.x == food.x and s.y == food.y:
            food.x = random.randrange(1, 40)
            food.y = random.randrange(1, 30)
            ball(food.x, food.y, blue)
        else:
            last = s.list.pop(0)
            ball(last.x, last.y, black)
        collision()
        pygame.display.update()
        threading.Thread(target=query).start()
        clock.tick(FPS)


def main():
    threading.Thread(target=printer).start()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if s.direction != 2:
                        s.direction = 0
                elif event.key == pygame.K_DOWN:
                    if s.direction != 3:
                        s.direction = 1
                elif event.key == pygame.K_LEFT:
                    if s.direction != 0:
                        s.direction = 2
                elif event.key == pygame.K_UP:
                    if s.direction != 1:
                        s.direction = 3


if __name__ == "__main__":
    main()


