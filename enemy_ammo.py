import pygame
import enemy
import window
import random
import player
import math
import life
import game_over

ammo = pygame.image.load("assets/enemy_ammo.png")

ammoX = []
ammoY = []
ammoDy = 0.5
ammoNum = 50
for i in range(ammoNum):
    ammoX.append(random.randint(0, window.winHeight - 8))
    ammoY.append(random.randint(-700, -50))

def shootAmmo():
    for x in range(ammoNum):
        # window.wn.blit(ammo, (ammoX[x],ammoY[x]))
        pygame.draw.rect(window.wn, (249, 79, 6), [ammoX[x], ammoY[x], 5, 7])

#Move the ammo

def moveAmmo():
    for x in range(ammoNum):
        ammoY[x] += ammoDy

#Restoring ammo
def restoreAmmo():
    for x in range(ammoNum):
        if ammoY[x] > window.winHeight + 10:
            ammoY[x] = random.randint(-700, -100)
            ammoX[x] = random.randint(0, window.winWidth -8)

#Ammo collision with player

def isAmmoCollision():
    for x in range(ammoNum):
        distance = math.sqrt(math.pow(ammoX[x] - player.playerX, 2) + math.pow(ammoY[x] - player.playerY, 2))
        if abs(ammoX[x] - player.playerX) < 50:
            if abs(ammoY[x] - player.playerY) < 5:
                ammoY[x] = random.randint(-700, -100)
                if life.lifeLevel > 0:
                    life.lifeLevel -= 10
                    if life.lifeLevel == 0:
                        game_over.GAME_OVER = True

