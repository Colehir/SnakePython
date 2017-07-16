from sense_hat import SenseHat
import pygame
import time
import threading
import random
sense = SenseHat()

pygame.init()

clock = pygame.time.Clock()

FPS = 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.list = []
        self.direction = 0
        self.dict = {}

s = Snake()
food = Point(random.randrange(3, 7), random.randrange(3, 7))
run = True
colors = [[0,0,0], [255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]

def draw_dot(x, y, color):
    sense.set_pixel(x,y, colors[color]) 

def collision():
    global run
    for point in s.list:
        if s.x == point.x and s.y == point.y:
            pygame.quit()
            run = False
            quit(0)
    if s.x < 0 or s.x > 7:
        pygame.quit()
        run = False
        quit(0)
    if s.y < 0 or s.y > 7:
        pygame.quit()
        run = False
        quit(0)

def getFood():
    food.x = random.randrange(0, 7)
    food.y = random.randrange(0, 7)
    for point in s.list:
        if point.x == food.x and point.y == food.y:
            getFood()

def printer():
    global FPS
    draw_dot(s.x, s.y, 1)
    s.list.append(Point(s.x, s.y))
    s.x += 1
    draw_dot(s.x, s.y, 1)
    s.list.append(Point(s.x, s.y))
    s.x += 1
    draw_dot(food.x, food.y, 2)
    while run:

        if s.direction == 0:
            s.x += 1
        elif s.direction == 1:
            s.y += 1
        elif s.direction == 2:
            s.x -= 1
        elif s.direction == 3:
            s.y -= 1

        if s.x == food.x and s.y == food.y:
            getFood()
            draw_dot(food.x, food.y, 2)
            FPS = FPS + .2
        else:
            last = s.list.pop(0)
            draw_dot(last.x, last.y, 0)

        collision()
        draw_dot(s.x, s.y, 1)
        s.list.append(Point(s.x, s.y))

        clock.tick(FPS)
 

def main():
    global run
    global s
    global food
    global FPS
    sense.clear()
    while True:
        threading.Thread(target=printer).start()
        while run:
            for event in sense.stick.get_events():
                if event.action == 'pressed' and event.direction == 'up':
                        s.direction = 3
                if event.action == 'pressed' and event.direction == 'down':
                        s.direction = 1
                if event.action == 'pressed' and event.direction == 'right':
                        s.direction = 0
                if event.action == 'pressed' and event.direction == 'left':
                        s.direction = 2
                if event.action == 'pressed' and event.direction == 'middle':
                    run = False
        sense.show_message("Game Over :(", text_colour = colors[3])
        sense.clear()
        while True:
            for event in sense.stick.get_events():
                if event.action == 'pressed' and event.direction == 'middle':
                    break
            else:
                continue
            break
        s = Snake()
        food = Point(random.randrange(3, 7), random.randrange(3, 7))
        run = True
        FPS = 1
    


if __name__ == "__main__":
    main()
