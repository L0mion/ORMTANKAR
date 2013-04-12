import pygame
import sys
from pygame.locals import *

import StartScreen
from StartScreen import *

import Game

from pygame.locals import *
from Game import *

def runGame(game, window):
    game.update()
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
    
    #main loop
    running = True
    while running:
        window.fill(blackColor)
    
        for event in pygame.event.get():
            if event.type == QUIT:
                   running = False
            elif event.type == KEYDOWN:
                inGame = True
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
    
        if inGame == True:
            runGame(game, window)
        else:
            runMenu(startScreen, window)
            
        pygame.display.update()
        fpsClock.tick(30)