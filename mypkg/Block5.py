import pygame
import time
import random
from Block import Block;
class block5(Block):
    def __init__(self,a,b,bs):
         self.x1=a
         self.x2=a+bs
         self.x3=a+2*bs
         self.x4=a+2*bs
         self.leftx=a
         self.y1=b
         self.y2=b
         self.y3=b
         self.y4=b+bs
         self.lefty=b
         self.array=[[1,1,1],[0,0,1]]
         blue=(0,0,255)
         self.color=blue
