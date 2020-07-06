import pygame
import random
import window
# Starts
starX = []
starY = []
starRad = []
MinR = 1
MaxR = 1
starNum = 180
starColor = []
dStarSpeedX = random.random()
dStarSpeedY = random.random()
for x in range(starNum):
    starColor.append((217, 242, 255))
    starX.append(random.randint(0, window.winWidth))
    starY.append(random.randint(0, window.winHeight))
    starRad.append(random.randint(MinR, MaxR))


# Drawing Stars

def drawStars():
    for i in range(starNum):
        pygame.draw.circle(window.wn, starColor[i], [starX[i], starY[i]], starRad[i])

#Blinking Stars
def blinkStars():
    Blink = random.randint(0, 1)
    if Blink == 0:
        starColor[random.randint(0, starNum - 1)] = (9, 29, 46 )
    elif Blink == 1:
        starColor[random.randint(0, starNum - 1)] = (217, 242, 255)

