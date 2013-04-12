import pygame
from pygame.locals import *
import sys

windowWidth = 800
windowHeight = 800
windowSize = windowWidth, windowHeight

blackColor = pygame.Color(0, 0, 0)

pygame.init()
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("ORMTANKAR - Snake of Thought - av mylingmygel.")

while True:
    window.fill(blackColor)

    for event in pygame.event.get():
        if event.type == QUIT:
               pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    fpsClock.tick(30)


