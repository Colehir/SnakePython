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
        self.list = []
        self.food = {}


def ball(x, y, color):
    pygame.draw.circle(display, color, (int(x*20), y*20), 10)
    pygame.display.update()

s = Snake()

def query():
    response = requests.get("http://127.0.0.1:5000/snake")
    s.list = response.json()
    response = requests.get("http://127.0.0.1:5000/food")
    s.food = response.json()

def printer():
    while True:
        query()
        for point in s.list:
            ball(point["x"], point["x"], red)
        ball(s.food["x"], s.food["y"], blue)
        pygame.display.update()
        clock.tick(FPS)


def main():
    printer()


if __name__ == "__main__":
    main()


