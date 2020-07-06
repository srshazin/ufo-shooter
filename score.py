import pygame
import window

Playerscore = 0
pygame.font.init()
font = pygame.font.SysFont("Ubuntu", 20)

scoreX = 20
scoreY = 10

def renderFont():
    global font
    render = font.render("Score: "+ str(Playerscore), True, (255, 255, 255))
    window.wn.blit(render, (scoreX , scoreY))