from Block_Cayden import Block
from GameBoard_Cayden import GBW, GBH, abs, abscolour
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)
GOLD = (255, 215, 0)

# Z SHAPE
ZSHAPE = [[(GBW/2)-1, 0], [(GBW/2)-2, 0], [(GBW/2)-1, 1], [GBW/2, 1]]
# S SHAPE
SSHAPE = [[(GBW/2)-1, 0], [GBW/2, 0], [(GBW/2)-2, 1], [(GBW/2)-1, 1]]
# LINE
LINESHAPE = [[(GBW/2)-1, 0], [(GBW/2)-2, 0], [(GBW/2), 0], [(GBW/2)+1, 0]]
# SQUARE
SQUARESHAPE = [[(GBW/2)-1, 0], [GBW/2, 0], [GBW/2, 1], [(GBW/2)-1, 1]]
# L
LSHAPE = [[(GBW/2)-1, 1], [(GBW/2)-1, 0], [(GBW/2)-1, 2], [GBW/2, 2]]
# Mirror L
MLSHAPE = [[(GBW/2), 1], [(GBW/2), 0], [(GBW/2), 2], [(GBW/2)-1, 2]]
#T Shape
TSHAPE = [[(GBW/2)-1, 1], [(GBW/2)-1, 0], [(GBW/2), 1], [(GBW/2)-2, 1]]

ALLSHAPES = [ZSHAPE, SSHAPE, SQUARESHAPE, LINESHAPE, LSHAPE, MLSHAPE, TSHAPE]
ALLCOLOURS = [WHITE, GREEN, RED, BLUE, YELLOW, MAGENTA, TURQUOISE]


class shape:
    def __init__(self):
        self.randomshape = random.randrange(7)
        self.colour = ALLCOLOURS[self.randomshape]
        self.numblocks = 4
        self.blocklist = []
        self.active = True
        self.copyactive = True
        self.hitbottom = False
        self.shape = ALLSHAPES[self.randomshape]
        for i in ALLSHAPES[self.randomshape]:
            self.blocklist.append(Block(self.colour, i[0], i[1]))

    def draw_shape(self, screen):
        for i in self.blocklist:
            i.draw_b(screen)
    def draw_copy_shape(self, screen):
        for i in self.blocklist:
            i.draw_copy_b(screen)
    def move_down(self):
        blocked = False
        for i in self.blocklist:
            if i.ypos == GBH - 1 or abs[int(i.xpos)][int(i.ypos)+1] == True:
                blocked = True
                for b in self.blocklist:
                    abs[int(b.xpos)][int(b.ypos)] = True
                    abscolour[int(b.xpos)][int(b.ypos)] = self.colour
                    self.active = False
        if blocked != True:
            for i in self.blocklist:
                i.ypos += 1

    def copy_move_down(self):
        copyblocked = False
        for i in self.blocklist:
            if i.ypos == GBH - 1 or abs[int(i.xpos)][int(i.ypos) + 1] == True:
                copyblocked = True
                self.copyactive = False
                self.hitbottom = True
        if copyblocked != True:
            for i in self.blocklist:
                i.ypos += 1
    def move_left(self):
        blocked = False
        for i in self.blocklist:
            if i.xpos == 0 or abs[int(i.xpos)-1][int(i.ypos)] == True:
                blocked = True
        if blocked != True:
            for i in self.blocklist:
                i.xpos -= 1
    def move_right(self):
        blocked = False
        for i in self.blocklist:
            if i.xpos == GBW - 1 or abs[int(i.xpos)+1][int(i.ypos)] == True:
                blocked = True
        if blocked != True:
            for i in self.blocklist:
                i.xpos += 1
    def rotate_cw(self):
        blocked = False
        if self.shape != ALLSHAPES[2]:
            newX = [0, 0, 0, 0]
            newY = [0, 0, 0, 0]
            theta = self.blocklist[0]
            for i in range(self.numblocks):
                y = self.blocklist[i].ypos
                x = self.blocklist[i].xpos
                newX[i] = -(y - theta.ypos) + theta.xpos
                newY[i] = (x - theta.xpos) + theta.ypos
                if newX[i] > GBW - 1 or newY[i] > GBH - 1 or newX[i] < 0 or abs[int(newX[i])][int(newY[i])] == True:
                        blocked = True
            if blocked != True:
                for i in range(self.numblocks):
                    x = newX[i]
                    y = newY[i]
                    self.blocklist[i].xpos = x
                    self.blocklist[i].ypos = y
    def rotate_cc(self):
        blocked = False
        if self.shape != ALLSHAPES[2]:
            newX = [0, 0, 0, 0]
            newY = [0, 0, 0, 0]
            theta = self.blocklist[0]
            for i in range(self.numblocks):
                y = self.blocklist[i].ypos
                x = self.blocklist[i].xpos
                newX[i] = (y - theta.ypos) + theta.xpos
                newY[i] = -(x - theta.xpos) + theta.ypos
                if newX[i] > GBW - 1 or newY[i] > GBH - 1 or newX[i] < 0 or abs[int(newX[i])][int(newY[i])] == True:
                    blocked = True
            if blocked != True:
                for i in range(self.numblocks):
                    x = newX[i]
                    y = newY[i]
                    self.blocklist[i].xpos = x
                    self.blocklist[i].ypos = y
    def harddrop(self):
        while (self.active):
            self.move_down()
    def copydrop(self):
        while self.hitbottom == False:
            self.copy_move_down()