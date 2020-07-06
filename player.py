import random
import pygame
import window

player = pygame.image.load("assets/player.png")

#draw Player

playerX = (window.winWidth - 64) / 2
playerY = window.winHeight - 80

changeRate = 2.5
dplayerX = 0
dplayerY = 0


movePlayr = True

def drawPlayer():
    window.wn.blit(player, (playerX, playerY))

#Moving Player
def movePlayer():
    global playerX, playerY
    if movePlayr is True:
        playerX += dplayerX
        # playerY += dplayerY

#Limits
def playerPosLimit():
    global playerX, playerY
    if playerX >= window.winWidth - 64:
        playerX = window.winWidth - 64
    if playerX <= 0:
        playerX = 0
    if playerY >= window.winHeight - 64:
        playerY = window.winHeight - 64
    if playerY <= 0:
        playerY = 0

#Shooting Bullets

bullet = pygame.image.load("assets/bullet.png")

bulletNum = 25
bulletX = []
bulletY = []
bulletDistance = 0
for x in range(bulletNum):
    bulletX.append(playerX + 34)
    bulletDistance -= 35
    bulletY.append(playerY - 10 + bulletDistance)


#Drawing Bullet

def drawBullet():
    for x in range(bulletNum):
        # window.wn.blit(bullet, (bulletX[x], bulletY[x]))
        pygame.draw.rect(window.wn,(255, 255, 255), [bulletX[x], bulletY[x], 3, 8])

#Moving Bullets

bulletDy = 1.5
def moveBullet():
    for x in range(bulletNum):
        bulletY[x] -= bulletDy

#Restoring Bullets

def restoreBullet():
    for i in range(bulletNum):
        if bulletY[i] < -8:
            bulletX[i] = playerX + 32
            bulletY[i] = playerY - 10
