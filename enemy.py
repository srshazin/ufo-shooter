import pygame
import random
import window
import player
import math
import score


ufo = [
    pygame.image.load("assets/ufo0.png"),
    pygame.image.load("assets/ufo1.png"),
    pygame.image.load("assets/ufo2.png"),
]

spawnUfo = []
ufoX = []
ufoY = []
ufoNum = 15
sign = [-1, 1]
DirX = []
DirY = []
commonSpeed = 0.1
dUfoSpeedX = commonSpeed * random.choice(sign)
dUfoSpeedY = commonSpeed * random.choice(sign)

for x in range(ufoNum):
    DirX.append(random.choice(sign))
    DirY.append(random.choice(sign))
    spawnUfo.append(ufo[random.randint(0, len(ufo) - 1)])
    ufoX.append(random.randint(64, window.winWidth - 64))
    ufoY.append(random.randint(-50, 300))


# Draw Enemy
def drawUfo():
    for x in range(ufoNum):
        window.wn.blit(spawnUfo[x], (ufoX[x], ufoY[x]))


# Moving Enemy

def moveUfo():
    for x in range(ufoNum):
        ufoX[x] += dUfoSpeedX * DirX[x]
        ufoY[x] += dUfoSpeedY * DirY[x]

#Checking if Enemy is Going Out of Screen

def innerScreen():
    for x in range(ufoNum):
        if ufoX[x] > window.winWidth - 32 or ufoX[x] < 0:
            DirX[x] *= -1
        if ufoY[x] > window.winHeight -32 or ufoY[x] < 32:
            DirY[x] *= -1

#Checking for collsion

def checkBulletCollision():
    for x in range(ufoNum):
        for i in range(player.bulletNum):
            distance = math.sqrt(math.pow(ufoX[x] - player.bulletX[i] , 2) + math.pow(ufoY[x] - player.bulletY[i] , 2))
            if distance <= 32:
                ufoY[x] = random.randint(0, 100)
                ufoX[x] = random.randint(5, 1000-64)
                player.bulletX[i] = -10
                score.Playerscore += 5
