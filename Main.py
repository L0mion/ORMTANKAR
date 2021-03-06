import pygame
import sys
from pygame.locals import *

import StartScreen
from StartScreen import *

import Game
import Train
from Train import *

from pygame.locals import *
from Game import *

def runGame(game, window, delta):
    game.update(delta)
    game.render(window)
    if game.isWon() == True:
        pygame.event.post(pygame.event.Event(QUIT))

def runMenu(startScreen, window):
    startScreen.display(window)

def main():
    #init pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    blackColor = pygame.Color(0, 0, 0)
    
    #init window
    windowWidth = 800
    windowHeight = 640
    windowSize = windowWidth, windowHeight
    window = pygame.display.set_mode(windowSize)
    pygame.display.set_caption("TAGTANKAR - Train of Thought - av mylingmygel.")

    startScreen = StartScreen()
    
    #init game
    blackColor = pygame.Color(0, 0, 0)
    game = Game()
    game.start()
    inGame = False
    
    #start multihreaded functions
    game.updatePlayers()
    game.spawnMindmaps()
    game.updateWorld()

    #main loop
    running = True
    while running:
        dt = fpsClock.tick(15)
        delta = 1 / float(dt) 

        window.fill(blackColor)
    
        player1 = 0
        player2 = 1
        for event in pygame.event.get():
            if event.type == QUIT:
                   running = False
            elif event.type == KEYDOWN:
                inGame = True

                if game.isGameOver() == True:
                    inGame = False
                    game.start() #restart

                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

                if event.key == K_w:
                    if game.players[player1].direction != Direction.DOWN:
                        game.players[player1].inputQueue.append(Direction.UP)
                if event.key == K_s :
                    if game.players[player1].direction != Direction.UP:
                        game.players[player1].inputQueue.append(Direction.DOWN)
                if event.key == K_a:
                    if game.players[player1].direction != Direction.RIGHT:
                        game.players[player1].inputQueue.append(Direction.LEFT)
                if event.key == K_d:
                    if game.players[player1].direction != Direction.LEFT:
                        game.players[player1].inputQueue.append(Direction.RIGHT)

                if event.key == K_UP:
                    if game.players[player2].direction != Direction.DOWN:
                        game.players[player2].inputQueue.append(Direction.UP)
                if event.key == K_DOWN :
                    if game.players[player2].direction != Direction.UP:
                        game.players[player2].inputQueue.append(Direction.DOWN)
                if event.key == K_LEFT:
                    if game.players[player2].direction != Direction.RIGHT:
                        game.players[player2].inputQueue.append(Direction.LEFT)
                if event.key == K_RIGHT:
                    if game.players[player2].direction != Direction.LEFT:
                        game.players[player2].inputQueue.append(Direction.RIGHT)
    
        if inGame == True:
            runGame(game, window, delta)
        else:
            runMenu(startScreen, window)
            
        pygame.display.update()
