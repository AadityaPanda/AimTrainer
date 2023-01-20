import pygame
import random
import sys
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 211, 67)
GREEN = (0, 100, 0)
DEEPSKYEBLUE = (0, 191, 255)
DARKBLUE = (0, 0, 40)

WINDOWHEIGHT = 720
WINDOWWIDTH = 1280

FONT = pygame.font.SysFont(None, 48)


def terminate():
    pygame.quit()
    sys.exit()


def Menu():
    timer = 0
    color = BLUE
    switch = False
    while True:
        windowSurface.fill(DARKBLUE)
        nameRects = []
        difficultyRects = []

        nameRects.append(pygame.Rect(393, 630, 463, 60))
        nameRects.append(pygame.Rect(20, 130, 1240, 20))
        difficultyRects.append(pygame.Rect(255, 370, 240, 100))
        difficultyRects.append(pygame.Rect(520, 370, 240, 100))
        difficultyRects.append(pygame.Rect(785, 370, 240, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            if event.type == MOUSEBUTTONDOWN:
                if difficultyRects[0].collidepoint(pygame.mouse.get_pos()):
                    game("easy")
                if difficultyRects[1].collidepoint(pygame.mouse.get_pos()):
                    game("medium")
                if difficultyRects[2].collidepoint(pygame.mouse.get_pos()):
                    game("hard")
        for rect in difficultyRects:
            pygame.draw.rect(windowSurface, RED, rect)
        for rect in nameRects:
            pygame.draw.rect(windowSurface, DEEPSKYEBLUE, rect)
        drawText("WELCOME TO AIM TRAINER", windowSurface, 20, 60, pygame.font.SysFont(None, 112, True, True), YELLOW)
        drawText("PICK A DIFFICULTY", windowSurface, 345, 260, pygame.font.SysFont(None, 95), color)
        drawText("EASY", windowSurface, 332, 400, FONT, WHITE)
        drawText("MEDIUM", windowSurface, 575, 400, FONT, WHITE)
        drawText("HARD", windowSurface, 855, 400, FONT, WHITE)
        drawText("-Aaditya Panda, CSE(IOT)-A", windowSurface, 400, 641, FONT, WHITE)
        mainClock.tick(50)
        timer += 1
        if timer % 100 == 0:
            color = BLUE
        elif timer % 50 == 0:
            color = RED
        pygame.display.update()


def drawText(text, surface, x, y, font=FONT, color=RED):
    textObject = font.render(text, 1, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)


def gameOver(totalShots, hitShots, difficulty, score):
    pygame.mouse.set_visible(True)
    if totalShots != 0 and hitShots != 0:
        accuracy = round(hitShots / totalShots * 100)
    else:
        accuracy = 0
    windowSurface.fill(DARKBLUE)
    drawText("GAME OVER", windowSurface, 420, 125, pygame.font.SysFont(None, 95, True))
    drawText("Click anywhere to restart", windowSurface, 500, 650, pygame.font.SysFont(None, 30, True))
    drawText("Accuracy: " + str(accuracy) + "%", windowSurface, 540, 235)
    drawText("Score: " + str(score), windowSurface, 580, 270)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                windowSurface.fill(WHITE)
                Menu()
            if event.type == KEYDOWN:
                terminate()


def populateConfig(difficulty):
    global targetImage, difficultyFile
    targetImage = pygame.image.load("targetblue.jpg")
    config = {}
    if difficulty == "easy":
        difficultyFile = open("easy.txt", "r")
    elif difficulty == "medium":
        difficultyFile = open("medium.txt", "r")
    elif difficulty == "hard":
        difficultyFile = open("hard.txt", "r")
    for line in difficultyFile:
        splitLine = line.split(":")
        splitLine[1] = splitLine[1].strip("\n")
        config[splitLine[0]] = int(splitLine[1])
    targetImage = pygame.transform.scale(targetImage, (config["enemySize"], config["enemySize"]))
    difficultyFile.close()
    return config


mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("sniper")

shootSound = pygame.mixer.Sound("snipersound.wav")
hitSound = pygame.mixer.Sound("metalHit.wav")
shootSound.set_volume(0.1)
hitSound.set_volume(0.1)

enemies = []


def game(difficulty):
    config = populateConfig(difficulty)

    pygame.mouse.set_visible(False)

    mouseY = (round(WINDOWHEIGHT / 2))
    mouseX = (round(WINDOWWIDTH / 2))

    tickCounter = 0
    enemies = []
    amountOfEnemies = 0
    score = 0
    FPS = 75
    hitShots = 0
    totalShots = 0
    STARTINGTIME = config.get("time")
    CIRCLERADIUS = 50
    while True:
        if config.get("time") <= 0:
            gameOver(totalShots, hitShots, difficulty, score)
        tickCounter += 1
        if tickCounter % FPS == 0:
            config["time"] -= 1
        windowSurface.fill(WHITE)

        if amountOfEnemies == 0:
            config["time"] = STARTINGTIME
            while amountOfEnemies != config.get("maxAmountOfEnemies"):
                enemies.append(pygame.Rect((random.randint(0, WINDOWWIDTH - config.get("enemySize"))),
                                           (random.randint(0, WINDOWHEIGHT - config.get("enemySize"))),
                                           config.get("enemySize"), config.get("enemySize")))
                if enemies[amountOfEnemies].topleft[0] < 135 and enemies[amountOfEnemies].topleft[1] < 65:
                    enemies.pop(amountOfEnemies)
                else:
                    amountOfEnemies += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                pass
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
            if event.type == MOUSEMOTION:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                pygame.mixer.Channel(0).play(shootSound)
                totalShots += 1
                for enemy in enemies[:]:
                    if mouseX > enemy.topleft[0] and mouseX < enemy.bottomright[0] \
                            and mouseY > enemy.topleft[1] and mouseY < enemy.bottomright[1]:
                        pygame.mixer.Channel(1).play(hitSound)
                        enemies.remove(enemy)
                        amountOfEnemies -= 1
                        score += 1
                        hitShots += 1
        for enemy in enemies:
            windowSurface.blit(targetImage, enemy)
        pygame.draw.circle(windowSurface, GREEN, (mouseX, mouseY),
                           CIRCLERADIUS + 1, 3)
        pygame.draw.line(windowSurface, GREEN, (mouseX, mouseY + 50),
                         (mouseX, mouseY - 50), 2)
        pygame.draw.line(windowSurface, GREEN, (mouseX + 50, mouseY),
                         (mouseX - 50, mouseY), 2)
        drawText("Time: " + str(config.get("time")), windowSurface, 8, 8)
        drawText("Score: " + str(score), windowSurface, 8, 38)
        pygame.display.update()
        mainClock.tick(FPS)


Menu()