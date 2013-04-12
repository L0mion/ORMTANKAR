import pygame
import sys
import Game

from pygame.locals import *
from Game import *

#init pygame
pygame.init()
fpsClock = pygame.time.Clock()

#init window
windowWidth = 800
windowHeight = 640
windowSize = windowWidth, windowHeight
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("TAGTANKAR - Train of Thought - av mylingmygel.")

#init game
blackColor = pygame.Color(0, 0, 0)
game = Game()
game.start()

#main loop
running = True
while running:
    window.fill(blackColor)

    for event in pygame.event.get():
        if event.type == QUIT:
               running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    game.update()
    if game.isWon() == True:
        pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    fpsClock.tick(30)


