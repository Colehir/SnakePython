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

class Snake:
    def __init__(self):
        self.list = []
        self.food = {}

    def query(self):
        response = requests.get("https://hiraparac2014.mybluemix.net/snake")
        self.list = response.json()
        response = requests.get("https://hiraparac2014.mybluemix.net/food")
        self.food = response.json()


def ball(x, y, color):
    pygame.draw.circle(display, color, (int(x*20)+10, y*20+10), 10)
    pygame.display.update()

s = Snake()


def printer():
    while True:
        s.query()
        display.fill((0, 0, 0))
        for point in s.list:
            ball(point["x"], point["y"], red)
        ball(s.food["x"], s.food["y"], blue)
        pygame.display.update()


def main():
    threading.Thread(target=printer).start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()


