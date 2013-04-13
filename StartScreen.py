import pygame
from pygame.locals import *

class StartScreen:

    def __init__(self):
        self.titleImg = pygame.image.load("img/title.png")
        self.player1Img = pygame.image.load("img/player1.png")
        self.player2Img = pygame.image.load("img/player2.png")
        self.controlsPlayer1Img = pygame.image.load("img/controls_player1.png")
        self.controlsPlayer2Img = pygame.image.load("img/controls_player2.png")
        self.gameDescriptionImg = pygame.image.load("img/guide.png")
        self.pressAnyKeyImg = pygame.image.load("img/pressAnyKey.png")
        self.wasdImg = pygame.image.load("img/wasd.png")
        self.arrowsImg = pygame.image.load("img/arrows.png")
        

    def display(self, window):
        window.blit(self.titleImg, (180,0))
        
        playerInfoPosY = 20
        playerInfoSpacingY = 55;

        #window.blit(self.gameDescriptionImg, (180, 350))

        window.blit(self.gameDescriptionImg, (110, 200))

        window.blit(self.player1Img, (30, playerInfoPosY))
        window.blit(self.wasdImg, (20, playerInfoPosY + playerInfoSpacingY))
        #window.blit(self.controlsPlayer1Img, (170, playerInfoPosY+playerInfoSpacingY))

        window.blit(self.player2Img, (640, playerInfoPosY))
        window.blit(self.arrowsImg, (630, playerInfoPosY+playerInfoSpacingY))
        #window.blit(self.controlsPlayer2Img, (450, playerInfoPosY+playerInfoSpacingY)) 

        window.blit(self.pressAnyKeyImg, (265, 560))
