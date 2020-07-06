import pygame
import random
import window
import math
import player
import life

heart = pygame.image.load("assets/heart.png")
heartX = random.randint(0, window.winWidth -35)
heartY = random.randint(-2500, -2000)
heartSpeed = 1

def drawheart():
    window.wn.blit(heart, (heartX, heartY))

def moveHeart():
    global heartX, heartY
    heartY += heartSpeed

#Restoring Heart

def restoreHeart():
    global heartY, heartX
    if heartY >= window.winHeight + random.randint(1000, 1500):
        heartX = random.randint(0, window.winWidth -35)
        heartY = random.randint(-2500, -2000)

#Checking if Heart Collsion

def heartCollision():
    global heartY
    distance = math.sqrt(math.pow(heartX - player.playerX , 2)+ math.pow(heartY - player.playerY , 2))
    if distance <= 32:
        if life.lifeLevel != 100:
            life.lifeLevel = 100
            heartY = random.randint(-2500, -2000)