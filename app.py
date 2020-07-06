import pygame
import random
import stars
import window
import enemy
import player
import enemy_ammo
import life
import game_over
import explosion
import increaseLife
import score

pygame.init()



# Main Game Loop
running = True

while running:
    # Window Background
    window.wn.fill((9, 29, 46))
    stars.drawStars()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.dplayerX = -player.changeRate
            if event.key == pygame.K_RIGHT:
                player.dplayerX = player.changeRate
            if event.key == pygame.K_UP:
                player.dplayerY = -player.changeRate
            if event.key == pygame.K_DOWN:
                player.dplayerY = player.changeRate



        if event.type == pygame.KEYUP:
            player.dplayerX = 0
            player.dplayerY = 0
    # Blinking Stars
    stars.blinkStars()
    # Drawing Enemey
    enemy.drawUfo()
    # Moving Enemy
    enemy.moveUfo()
    # Checking
    enemy.innerScreen()
    # Drawing Player
    player.drawPlayer()
    # Moving Player
    player.movePlayer()
    #Limiting Player's Position
    player.playerPosLimit()
    #Shooting Enemy Ammos
    enemy_ammo.shootAmmo()
    #Moving ufo ammos
    enemy_ammo.moveAmmo()
    #Restoring Ammo
    enemy_ammo.restoreAmmo()
    #Detect Ammo Collision
    enemy_ammo.isAmmoCollision()
    #Life Container
    life.drawLifeContainer()
    #Draw Life Level
    life.drawLifeLevel()
    #Drawing Bullet
    player.drawBullet()
    #Moving Bullets
    player.moveBullet()
    #Restore Bullets
    player.restoreBullet()
    #Checking if bullet collision with ufo
    enemy.checkBulletCollision()
    #Detect if explosion
    explosion.blastDetection()
    #Increasing Life
    #Drawing Heart
    increaseLife.drawheart()
    #Move Heart
    increaseLife.moveHeart()
    #Restoring Heart
    increaseLife.restoreHeart()
    #Checking Heart Collision
    increaseLife.heartCollision()
    #rendering Scre
    score.renderFont()
    #Exploding player if life = 0
    game_over.explodePlayer()
    #GAME OVER
    if life.lifeLevel == 0:
        game_over.gameOver()
        game_over.explodePlayer()

    # Updating Game Screen
    pygame.display.update()
