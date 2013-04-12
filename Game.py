import random
import Train
import Tile
import pygame

from random import *
from Train import *
from Tile import *
from pygame import *

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

        self.tileImage = pygame.image.load("img/tile.png")
        self.snake1Image = pygame.image.load("img/orm_red.png")

        self.hudTitleImage = pygame.image.load("img/hud_title.png")
        self.hudDividerImage = pygame.image.load("img/hud_divider.png")
        self.hudFont = pygame.font.SysFont("Calibri", 26)

    def start(self):
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

    def renderHud(self, window):
        window.blit(self.hudTitleImage, (0, 0))
        window.blit(self.hudDividerImage, (0, 88))
        score = 40
        label = self.hudFont.render("Score: " +str(score), 1, (255, 255, 255))
        window.blit(label, (400, 45))

    def update(self, window):
        self.renderHud(window)

        for x in range(tileDimX):
            for y in range(tileDimY):
                #tile = self.lvl[x][y]
                spritePos = x * tileImageWidth, y * tileImageHeight + offsetHUD
                window.blit(self.tileImage, spritePos)

        for i in range(self.numPlayers):
            train = self.players[i]
            for j in range(train.length):
                window.blit(self.snake1Image, (train.body[j].X() * tileImageWidth, train.body[j].Y() * tileImageHeight + offsetHUD))

        return 'update game'
    def isWon(self):
        return self.won
   