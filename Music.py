import pygame
from pygame.locals import *

# This makes sure that you're not importing the module.
def play_music(L=[]):
    for i in L:
        pygame.mixer.init()
        pygame.mixer.music.load(i)
        pygame.mixer.music.play()
