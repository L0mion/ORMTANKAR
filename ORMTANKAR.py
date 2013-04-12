import pygame
import sys
from pygame.locals import *

import StartScreen
from StartScreen import *

windowWidth = 800
windowHeight = 640
windowSize = windowWidth, windowHeight

pygame.init()
fpsClock = pygame.time.Clock()
blackColor = pygame.Color(0, 0, 0)

window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("ORMTANKAR - Snake of Thought - av mylingmygel.")

startScreen = StartScreen()

running = True
while running:
    window.fill(blackColor)

    startScreen.display(window)

    for event in pygame.event.get():
        if event.type == QUIT:
               running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    fpsClock.tick(30)
    


