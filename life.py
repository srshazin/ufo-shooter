import pygame
import random
import window

#Drawing Life Container

def drawLifeContainer():
    pygame.draw.rect(window.wn, (255, 255, 255), [20, 50 , 100, 10])

#Draw Level

lifeLevel = 100


def drawLifeLevel():
    pygame.draw.rect(window.wn, (16, 180, 0), [20, 50 , lifeLevel, 10])

