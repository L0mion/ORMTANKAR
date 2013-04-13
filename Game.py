import random
import Train
import Tile
import pygame
import threading
import Mindmap

from random import *
from Train import *
from Tile import *
from pygame import *
from threading import *
from Mindmap import *

numPlayers = 2
trainStartLength = 3
tileDimX = 32
tileDimY = 22
offsetHUD = 90
tileImageWidth = 25
tileImageHeight = 25
mindmapLifetime = 3

class Game:
    def __init__(self):
        self.score = 0
        self.won = False
        self.numPlayers = numPlayers
        self.lvl = []
        self.mindmaps = []
        self.gameOver = False

        self.tileImage = pygame.image.load("img/tile.png")
        self.snake1Image = pygame.image.load("img/orm_red.png")
        self.snake2Image = pygame.image.load("img/orm_blue.png")
        self.debugImage = pygame.image.load("img/debug.png")
        self.mindmapImage = pygame.image.load("img/tileMindmap.png")
        self.inspirationImage = pygame.image.load("img/inspiration.png")

        self.hudTitleImage = pygame.image.load("img/hud_title.png")
        self.hudDividerImage = pygame.image.load("img/hud_divider.png")
        self.hudFont = pygame.font.SysFont("Calibri", 26)
        self.player1Image = pygame.image.load("img/player1.png")
        self.player2Image = pygame.image.load("img/player2.png")
        self.mult0Image = pygame.image.load("img/0.png")
        self.mult2Image = pygame.image.load("img/2.png")
        self.mult4Image = pygame.image.load("img/4.png")
        self.mult8Image = pygame.image.load("img/8.png")
        self.mult16Image = pygame.image.load("img/16.png")
        self.length = pygame.image.load("img/length.png")

    def start(self):
        self.mindmaps = []
        self.gameOver = False
        self.won = False
        self.startLvl()
        self.startPlayers()
        
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

    def renderPlayerMultiplier(self, train, pos, window):
        image = self.mult0Image
        if(train.brainstorming == 2):
            image = self.mult2Image
        if(train.brainstorming == 4):
            image = self.mult4Image
        if(train.brainstorming == 8):
            image = self.mult8Image
        if(train.brainstorming == 16):
            image = self.mult16Image
        window.blit(image, pos)


    def renderHud(self, window):
        window.blit(self.hudTitleImage, (0, 0))
        window.blit(self.player1Image, (200, 0))
        window.blit(self.player2Image, (200, 45))
        window.blit(self.hudDividerImage, (0, 88))
        score = 40
        label = self.hudFont.render("Score: " +str(score), 1, (255, 255, 255))
        window.blit(label, (400, 45))

        self.renderPlayerMultiplier(self.players[0], (340, 0), window)
        self.renderPlayerMultiplier(self.players[1], (340, 45), window)

    def updateTrain(self, train, othertrain):
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
            if tile.special == Special.SPECIAL:
                #BRAINSTORM
                if train.curMultiplier > 0:
                    train.curMultiplier = train.curMultiplier * 2
                else:
                    train.curMultiplier = 2 
                    train.brainstorming = train.brainstorming + 1
            else:
                train.kill()
                self.gameOver = True
        elif tile.status == Status.TRAINFOOD:
            train.addBitsOfTrain()
        
        train.move(trainPos, self.lvl, othertrain)

    def updatePlayers(self):
        t = threading.Timer(0.1, self.updatePlayers)
        t.daemon = True
        t.start()

        if self.gameOver == False:
            self.updateTrain(self.players[0], self.players[1])
            self.updateTrain(self.players[1], self.players[0])
    
    def spawnMindmaps(self):
        t = threading.Timer(2, self.spawnMindmaps)
        t.daemon = True
        t.start()

        if self.gameOver == False:
            #randomize a valid position
            valid = False
            randomPos = Vec2(0,0)
            while valid == False:
                randomPos = Vec2(randint(0, tileDimX - 1), randint(0, tileDimY - 1))
                if self.lvl[randomPos.X()][randomPos.Y()].Status() == Status.EMPTY:
                    valid = True
            
            self.mindmaps.append(Mindmap(randomPos, mindmapLifetime))
            self.lvl[randomPos.X()][randomPos.Y()].special = Special.SPECIAL
    
    def update(self, delta):
        for mindmap in self.mindmaps:
            mindmap.timeLeft = mindmap.timeLeft - delta
            if mindmap.timeLeft <= 0:
                if self.lvl[mindmap.Pos().X()][mindmap.Pos().Y()].status == Status.OCCUPIED: 
                    self.lvl[mindmap.Pos().X()][mindmap.Pos().Y()].special = Special.NA
                    self.mindmaps.pop(self.mindmaps.index(mindmap))

    def updateWorld(self):
        t = threading.Timer(1.5, self.updateWorld)
        t.daemon = True
        t.start()

        if self.gameOver == False:
            self.addInspiration()

    def render(self, window):
        self.renderHud(window)

        #render tiles
        for x in range(tileDimX):
            for y in range(tileDimY):
                spritePos = x * tileImageWidth, y * tileImageHeight + offsetHUD
                window.blit(self.tileImage, spritePos)
                if self.lvl[x][y].status == Status.TRAINFOOD:
                    window.blit(self.inspirationImage, spritePos)
                

        #render mindamps
        for i in range(len(self.mindmaps)):
            mindmapPos = self.mindmaps[i].Pos()
            window.blit(self.mindmapImage, (mindmapPos.X() * tileImageWidth, mindmapPos.Y() * tileImageHeight + offsetHUD))

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
