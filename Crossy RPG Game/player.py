import pygame
from gameObject import GameObject

class Player(GameObject):
    def __init__(self,x,y,width,height,image_path, speed):
        super().__init__(x,y,width,height,image_path)
        
        self.speed = speed
    
    def move(self,direction,max_height):
        if (self.y >= max_height - self.height and direction >0) or (self.y <= 0 and direction <0): # 0 (top) max_height (buttom)
          return
        self.y += (direction * self.speed)