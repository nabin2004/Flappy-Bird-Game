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
    GAMES_SPRITES['pipe'] = pygame.image.load('').convert_alpha()

    pygame.image.load('').convert_alpha()
    pygame.image.load('').convert_alpha()