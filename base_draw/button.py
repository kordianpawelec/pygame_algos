from pygame.sprite import Sprite
import pygame
from pygame.font import Font
from utils.constants import *

class Button(Sprite):
    def __init__(self, game, text):
        super().__init__()
        self.text = text
        self.colour = BUTTON_COLOUR
        self.screen = game.screen
        self.rect = pygame.Rect(20,20,BUTTON_WIDTH, BUTTON_HEIGHT)
        self.font = pygame.font.SysFont(None,FONT_SIZE)
        # self.prep_button()
        
    
    # def prep_button(self):
        
    
    def update(self):
        self.font_image = self.font.render(self.text, True, FONT_COLOUR, self.colour)
        self.image_rect = self.font_image.get_rect()
        self.image_rect.center = self.rect.center
        self.screen.fill(self.colour, self.rect)
        self.screen.blit(self.font_image, self.image_rect)

