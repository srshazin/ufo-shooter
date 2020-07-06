import pygame
import enemy
import player
import life
import math
import window
import enemy_ammo
import game_over

#Load The Image
fireball = pygame.image.load("assets/explosion.png")

#detect the collision

def blastDetection():
    for x in range(enemy.ufoNum):
        distance = math.sqrt(math.pow(enemy.ufoX[x] - player.playerX, 2) + math.pow(enemy.ufoY[x] - player.playerY, 2))
        if distance <= 32:
            window.wn.blit(fireball, (player.playerX +16, player.playerY))
            game_over.gameOver()
