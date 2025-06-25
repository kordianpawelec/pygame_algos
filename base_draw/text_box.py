import pygame

from utils.constants import *


class TextBox:
    def __init__(self, game, button):
        self.text = ''
        self.screen = game.screen
        self.button = button
        self.colour = BUTTON_COLOUR
        self.rect = pygame.Rect(self.button.rect.right + 20, self.button.rect.top, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.font = pygame.font.SysFont(self.text, FONT_SIZE)


    def update(self):
        self.font_image = self.font.render(self.text, True, FONT_COLOUR, BUTTON_COLOUR)
        self.font_image_rect = self.font_image.get_rect()
        self.font_image_rect.center = self.rect.center
        self.screen.fill(self.colour, self.rect)
        self.screen.blit(self.font_image, self.font_image_rect)