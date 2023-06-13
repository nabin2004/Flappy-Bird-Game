import random 
#Randomnesss is always used in Game
import sys
import pygame
from pygame.locals import *   #Imports basic pygame

# Global variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAMES_SPRITES = {}
GAMES_SOUNDS = {}
PLAYER = 'main-character.png'
BACKGROUND = 'background.png'
PIPE = ''



#start

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird")
    GAMES_SPRITES['numbers'] = (
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
        pygame.image.load('').convert_alpha(),
    )

    GAMES_SPRITES['message'] = pygame.image.load('').convert_alpha()
    GAMES_SPRITES['base'] = pygame.image.load('').convert_alpha()
    GAMES_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
    pygame.image.load(PIPE).convert_alpha())
    GAMES_SPRITES['background'] = pygame.image.load(BACKGROUND).cconvert()
    GAMES_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    #GAME SOUNDS
    GAMES_SOUNDS['die'] = pygame.mixer.Sound('')
    GAMES_SOUNDS['hit'] = pygame.mixer.Sound('')
    GAMES_SOUNDS['point'] = pygame.mixer.Sound('')
    GAMES_SOUNDS['swoosh'] = pygame.mixer.Sound('')
    GAMES_SOUNDS['wing'] = pygame.mixer.Sound('')

def welcomeScreen():
    """Shows Welcome Screen"""
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT- GAMES_SPRITES['player'].get_height())/2
    messagex = int(SCREENHEIGHT- GAMES_SPRITES['message'].get_width())/2
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            
            else:
                SCREEN.blit(GAMES_SPRITES['background'], (0, 0))
                SCREEN.blit(GAMES_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAMES_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAMES_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)



    while True:
        welcomeScreen()
        mainGame() #This is the main game function
