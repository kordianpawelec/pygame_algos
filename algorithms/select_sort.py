import pygame
import time
from utils.constants import *

class SelectSort:
    def __init__(self, game):
        self.game = game
        
        
    

    def sorting(self):
        self.arr: pygame.sprite.Group = self.game.rectangles
        self.arr = list(self.arr.sprites())
        self.arr_size = self.game.range
        for i in range(self.arr_size):
            minimum = i
            for j in range(i + 1, self.arr_size):
                self.arr[j].colour = WHITE
                self.game.render()
                # time.sleep(0.1)
                if self.arr[minimum].ht > self.arr[j].ht:
                    minimum = j
                
                self.arr[j].colour = RED
                self.game.render()
            
            self.arr[i].rect.x, self.arr[minimum].rect.x = self.arr[minimum].rect.x,  self.arr[i].rect.x
            self.arr[i], self.arr[minimum] = self.arr[minimum], self.arr[i]
            for k in range(i+1):
                self.arr[k].colour = GREEN
                self.game.render()
            time.sleep(0.1)
        self.game.render()
