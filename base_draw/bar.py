from pygame.sprite import Sprite
from utils.constants import *
import pygame


class Bar(Sprite):
    def __init__(self, game, width, height):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(0, SCREEN_HIGHT - height, width, height)
        self.ht = height
        self.colour = RED

    def update(self):
        self.screen.fill(self.colour, self.rect)
    

