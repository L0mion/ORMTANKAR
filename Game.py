import random
import Train
import Tile

from random import *
from Train import *
from Tile import *

numPlayers = 2
trainStartLength = 3
tileDimX = 25
tileDimY = 25

class Game:
    def __init__(self):
        self.score = 0
        self.won = False
        self.numPlayers = numPlayers
        self.lvl = []

        self.temp = "temp"

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
        self.temp = "break"

    def startPlayers(self): #initializes players
        self.players = [] #clear if pre-existing players
        i = 0
        while(i < self.numPlayers):
            #randomize start positions on the board
            randomPositions = []
            
            randomPos = Vec2(randint(0, tileDimX), randint(0, tileDimY)) #start pos of train
            #if randompos valid...
            randomPositions.append(randomPos)
            randomPositions.append(Vec2(0, 0)) #TEMP
            randomPositions.append(Vec2(0, 0)) #TEMP

            #add player
            self.players.append(Train(trainStartLength, randomPositions))
            i = i + 1

    def update(self):
        return 'update game'
    def isWon(self):
        return self.won