GAME_OVER = False
import pygame
import life
import window
import enemy_ammo
import enemy
import player
import increaseLife
import explosion
game_over_image = pygame.image.load("assets/game_over.png")
import score

font = pygame.font.SysFont("Ubuntu Bold", 40)

def gameOver():
    window.wn.blit(game_over_image, ((window.winWidth - 400)/2, (window.winHeight)/2))
    render_final_score = font.render("Final Score: " + str(score.Playerscore) , True, (255, 255, 255))
    window.wn.blit(render_final_score, (400, 400))
    for x in range(enemy.ufoNum):
        enemy.dUfoSpeedX = 0
        enemy.DirX[x] = 0
        enemy.DirY[x] = 0
        enemy.dUfoSpeedY = 0
        for i in range(player.bulletNum):
            player.bulletY[i] = 0
        player.movePlayr = False
        enemy_ammo.ammoDy = 0
        increaseLife.heartSpeed = 0

#blast Playeer
def explodePlayer():
    if life.lifeLevel == 0:
        window.wn.blit(explosion.fireball , (player.playerX + 16, player.playerY))

