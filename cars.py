x = 400
y = 40
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame, sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Car catcher")

FPS = 40
clock = pygame.time.Clock()

carSpeed = 12
carX, carY = 250, 0
playerSpeed = 6
playerX, playerY = 300, 600
isMovingLeft = None
timer = 300
level = 1
level_counter = 0
count = 0
health = 30
isRunning = True

life = pygame.image.load("resources/images/life.png")
road = pygame.image.load("resources/images/road3.png")
def displayHealth():
    global health
    x = health
    while x > 0:
       screen.blit(life, (30*x/10 - 10,15))
       x -= 10

player = pygame.image.load("resources/images/player.png")

class Car(object):
    carX = 0
    carY = 0
    position = 0
    car = pygame.image.load("resources/images/car.png")

def new_car(x,p):
    car = Car()
    car.carX = x
    car.carY = 0
    car.position = p
    return car

cars = []

while isRunning:
    screen.fill((0,0,0))
    screen.blit(road, (0,0))
    timer += 1
    displayHealth()
    
    if health == 0:
            pygame.display.flip()
            isRunning = False
            
    for x in cars:
        x.carY += carSpeed * level
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                isMovingLeft = True
            if event.key == K_RIGHT:
                isMovingLeft = False
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                isMovingLeft = None

    if isMovingLeft != None:
        if isMovingLeft == True:
            playerX -= playerSpeed
            if playerX < 0:
                playerX = 0
        if isMovingLeft == False:
            playerX += playerSpeed
            if playerX > 625:
                playerX = 625

    if timer > random.randint(20, 30):
        count += 1
        cars[0:0] = [new_car(random.randint(5, 650), count)]
        timer = 0
    for x in cars:
        screen.blit(x.car,(x.carX, x.carY) )

    
    if  pygame.Rect(playerX, playerY, player.get_width(), player.get_height()).colliderect( pygame.Rect(cars[len(cars)-1].carX, cars[len(cars)-1].carY, cars[len(cars)-1].car.get_width(), cars[len(cars)-1].car.get_height())):
        health -= 10
        cars.pop()
    elif len(cars)!=0 and cars[len(cars)-1].carY > 640:
            cars.pop()
            
    screen.blit(player, (playerX,playerY))
    pygame.display.flip()
    clock.tick(FPS)

fontObj = pygame.font.Font('freedom.ttf', 90)
textSurfaceObj = fontObj.render("GAME OVER" ,True,(255, 0,0))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (350, 350)
screen.blit(textSurfaceObj, textRectObj)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

    
