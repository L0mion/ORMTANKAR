import random
import Train
import Tile
import pygame
import threading

from random import *
from Train import *
from Tile import *
from pygame import *
from threading import *

numPlayers = 2
trainStartLength = 3
tileDimX = 32
tileDimY = 22
offsetHUD = 90
tileImageWidth = 25
tileImageHeight = 25

class Game:
    def __init__(self):
        self.score = 0
        self.won = False
        self.numPlayers = numPlayers
        self.lvl = []
        self.gameOver = False

        self.tileImage = pygame.image.load("img/tile.png")
        self.snake1Image = pygame.image.load("img/orm_red.png")
        self.snake2Image = pygame.image.load("img/orm_blue.png")
        self.debugImage = pygame.image.load("img/debug.png")
        self.inspirationImage = pygame.image.load("img/inspiration.png")

        self.hudTitleImage = pygame.image.load("img/hud_title.png")
        self.hudDividerImage = pygame.image.load("img/hud_divider.png")
        self.hudFont = pygame.font.SysFont("Calibri", 26)

    def start(self):
        self.gameOver = False
        self.won = False
        self.startLvl()
        self.startPlayers()

        self.updateWorld()
        
    def startLvl(self): #initializes level
        #init lvl
        self.lvl = []
        for i in range(tileDimX):
            self.lvl.append([])
            for j in range(tileDimY):
                self.lvl[i].append(Tile(Status.EMPTY, Special.NA)) #all tiles are empty to begin with

    def startPlayers(self): #initializes players
        self.players = [] #clear if pre-existing players
       
        #randomize start positions on the board
        playerPositions = []
        playerPositions.append(Vec2(8, 12))
        playerPositions.append(Vec2(8, 13))
        playerPositions.append(Vec2(8, 14))
        self.players.append(Train(3, playerPositions))

        playerPositions = []
        playerPositions.append(Vec2(24, 12))
        playerPositions.append(Vec2(24, 13))
        playerPositions.append(Vec2(24, 14))
        self.players.append(Train(3, playerPositions))

    def renderHud(self, window):
        window.blit(self.hudTitleImage, (0, 0))
        window.blit(self.hudDividerImage, (0, 88))
        score = 40
        label = self.hudFont.render("Score: " +str(score), 1, (255, 255, 255))
        window.blit(label, (400, 45))


    def updatePlayers(self):
        t = threading.Timer(0.1, self.updatePlayers)
        t.daemon = True
        t.start()

        if self.gameOver == False:
            for i in range(self.numPlayers):
                train = self.players[i]

                direction = train.direction;
                if len(train.inputQueue) > 0:
                    direction = train.inputQueue.pop()
                    train.inputQueue.clear()

                if direction == Direction.UP:
                    if train.direction != Direction.DOWN:
                        train.direction = Direction.UP
                elif direction == Direction.DOWN:
                    if train.direction != Direction.UP:
                        train.direction = Direction.DOWN
                elif direction == Direction.LEFT:
                    if train.direction != Direction.RIGHT:
                        train.direction = Direction.LEFT
                elif direction == Direction.RIGHT:
                    if train.direction != Direction.LEFT:
                        train.direction = Direction.RIGHT


                trainBody = train.Body()
                trainPos = Vec2(trainBody[0].X(), trainBody[0].Y())
                if train.Direction() == Direction.UP:
                    trainPos.y = trainBody[0].Y() - 1
                elif train.Direction() == Direction.DOWN:
                    trainPos.y = trainBody[0].Y() + 1
                elif train.Direction() == Direction.RIGHT:
                    trainPos.x = trainBody[0].X() + 1
                elif train.Direction() == Direction.LEFT:
                    trainPos.x = trainBody[0].X() - 1

                #loop
                if trainPos.X() >= tileDimX:
                    trainPos.x = 0
                elif trainPos.X() < 0:
                    trainPos.x = tileDimX - 1
                elif trainPos.Y() >= tileDimY:
                    trainPos.y = 0
                elif trainPos.Y() < 0:
                    trainPos.y = tileDimY - 1

                tile = self.lvl[trainPos.X()][trainPos.Y()]
                if tile.status == Status.OCCUPIED:
                    train.kill()
                    self.gameOver = True
                if tile.status == Status.TRAINFOOD:
                    train.addBitsOfTrain()

                train.move(trainPos, self.lvl)

    def updateWorld(self):
        t = threading.Timer(0.5, self.updateWorld)
        t.daemon = True
        t.start()

        self.addInspiration()

    #def update(self):
    #    self.updatePlayers()

    def render(self, window):
        self.renderHud(window)

        for x in range(tileDimX):
            for y in range(tileDimY):
                #tile = self.lvl[x][y]
                spritePos = x * tileImageWidth, y * tileImageHeight + offsetHUD
                window.blit(self.tileImage, spritePos)

                if self.lvl[x][y].status == Status.TRAINFOOD:
                    window.blit(self.inspirationImage, spritePos)

        #render first player
        train = self.players[0]
        for j in range(train.length):
            window.blit(self.snake1Image, (train.body[j].X() * tileImageWidth, train.body[j].Y() * tileImageHeight + offsetHUD))

        #render second player
        train = self.players[1]
        for j in range(train.length):
            window.blit(self.snake2Image, (train.body[j].X() * tileImageWidth, train.body[j].Y() * tileImageHeight + offsetHUD))

    def isWon(self):
        return self.won

    def isGameOver(self):
        return self.gameOver

    def addInspiration(self):
        x = randrange(0, tileDimX, 1)
        y = randrange(0, tileDimY, 1)
    
        if self.lvl[x][y].status == Status.EMPTY:
            self.lvl[x][y].status = Status.TRAINFOOD
        else:
            self.addInspiration()
