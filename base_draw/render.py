from utils.constants import *
from base_draw.bar import Bar
import pygame

class Render:
    def __init__(self, game):
        self.game = game
        self.screen = game
        self.arr_size = game.range
        self.arr = game.arr
        self.rectangles: pygame.sprite.Group = game.rectangles
        self.create_bars()
        print(self.arr)


    def create_bars(self):
        for i in range(len(self.arr)):
            bar = Bar(self.game, OFFSET, self.arr[i])
            bar.rect.left = OFFSET + (OFFSET * 2 * i)
            self.rectangles.add(bar)
    
    def update(self):
        # print(len(self.rectangles))
        self.rectangles.update()
        

    # def populate_rectangles(self):
    #     for hight in self.arr:
    #         if not self.rectangles:
    #             rect = pygame.Rect(OFFSET,0,OFFSET, hight)
    #             obj = self.screen.fill(rect, RED)
    #             self.rectangles.add(obj)
    #         else:
    #             last_obj = self.rectangles[-1]
    #             rect = pygame.Rect(last_obj.rect.right + OFFSET,0,OFFSET, hight)
    #             obj = self.screen.fill(rect, RED)
    #             self.rectangles.add(obj)
        


    
        
