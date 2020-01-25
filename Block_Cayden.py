import pygame
from GameBoard_Cayden import bsize


class Block:

    def __init__(self, colour, x, y):
        self.bsize = bsize
        self.xpos = x
        self.ypos = y
        self.colour = colour

    def draw_b(self, screen):
        pygame.draw.rect(screen, self.colour, [self.xpos*bsize, self.ypos*bsize, self.bsize-1, self.bsize-1], 0)
    def draw_copy_b(self, screen):
        pygame.draw.rect(screen, self.colour, [self.xpos*bsize, self.ypos*bsize, self.bsize-1, self.bsize-1], 3)
