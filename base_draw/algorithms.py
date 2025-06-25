import pygame
import sys

from utils.constants import *
from base_draw.button import Button
from base_draw.text_box import TextBox 


class AlgorithmsUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
        self.clock = pygame.time.Clock()
        self.buttons = pygame.sprite.Group()
        self.menu_buttons()
        self.range = None
        self.algo = None


    def run(self):
        while True:

            self.events()            
            self.render()
            self.clock.tick(30)
        

    def events(self):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            self.button_action(mouse_pos, event.type)
        
        
        if keys[pygame.K_q]:
                sys.exit()
        
                
    def button_action(self, mouse_pos, event_type):
        for button in self.buttons.sprites():
            if button.rect.collidepoint(mouse_pos):
                button.colour = (200,200,200)
                if event_type == pygame.MOUSEBUTTONDOWN:
                    match button.text:
                        case 'Start':
                            if self.range and self.algo:
                                self.run_drawing()
                            print('Start')
                            pass
                        case 'Range':
                            text_box = TextBox(self, button)
                            self.get_range(text_box)
                            pass
                        case 'Select sort':
                            print('Select sort')
                            pass
            else:
                button.colour = BUTTON_COLOUR
  

    def get_range(self, text_box: TextBox):
        key = 0
        while key != 13:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    text_box.text += chr(event.key)
                    key = event.key

            self.screen.fill('purple')
            text_box.update()
            pygame.display.flip()
            self.clock.tick(30)

        self.range = int(text_box.text)
        del text_box
            
            


    def render(self):
        self.screen.fill('purple')
        self.buttons.update()
        pygame.display.flip()


    def menu_buttons(self):
        self.buttons.empty()
        start_button = Button(self, 'Start',)
        range_button = Button(self, 'Range')
        range_button.rect.top = start_button.rect.bottom + 10
        select_algo_button = Button(self, 'Select sort')
        select_algo_button.rect.top = range_button.rect.bottom + 10

        
        


        self.buttons.add(start_button, range_button, select_algo_button)
        



if __name__ == '__main__':
    a = AlgorithmsUI
    a.run()