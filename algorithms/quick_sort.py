
import time
from utils.constants import *

class QuickSort:
    def __init__(self, game):
        self.game = game
 
        
        

    def sorting(self, arr):
        self.quicksort_inplace(arr, 0, len(arr) - 1)
        self.colour_green(arr)
        return arr

    def quicksort_inplace(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            
            self.quicksort_inplace(arr, low, pi - 1)
            self.quicksort_inplace(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        pivot.colour = WHITE
        
        i = low - 1 
        
        for j in range(low, high):
            time.sleep(0.03)
            
            if arr[j].ht <= pivot.ht:
                i += 1

                self.swap_bars(arr, i, j)

        self.swap_bars(arr, i + 1, high)
        pivot.colour = RED
        self.game.render()
        time.sleep(0.1)
        
        return i + 1

    def swap_bars(self, arr, i, j):
        if i != j:

            arr[i], arr[j] = arr[j], arr[i]
 
            temp_x = arr[i].rect.x
            arr[i].rect.x = arr[j].rect.x
            arr[j].rect.x = temp_x
            
            self.game.render()
            time.sleep(0.02)

    def colour_green(self, arr):
        for bar in arr:
            bar.colour = GREEN
            self.game.render()
            time.sleep(0.001)
            