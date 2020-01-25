import pygame
pygame.init()
GBW = 12
GBH = 20
bsize = 25
abs = [[False for y in range(GBH)]for x in range(GBW)]
abscolour = [[(0, 0, 0) for y in range(GBH)]for x in range(GBW)]
linesound = pygame.mixer.Sound("bruh.wav")
losssound = pygame.mixer.Sound("clearline.wav")

class gameboard:
    def __init__(self, colour):
        self.colour = colour
        self.size = bsize
        self.score = 0
        self.lineremoved = False
    def draw_gb(self, screen):
        pygame.draw.rect(screen, self.colour, [0, 0, self.size*GBW, self.size*GBH], 1)
        for x in range(GBW):
            for y in range(GBH):
                if abs[x][y] == True:
                    pygame.draw.rect(screen, abscolour[x][y], [x*bsize, y*bsize, bsize-1, bsize-1], 0)
        for x in range(GBW):
            pygame.draw.line(screen, (100, 100, 100), [x * bsize - 1, 0], [x * bsize - 1, GBH * bsize - 1], 1)
        for y in range(GBH):
            pygame.draw.line(screen, (100, 100, 100), [0, y * bsize - 1], [GBW * bsize - 1, y * bsize - 1], 1)
    def LC(self, y):
        FF = True
        x = 0
        while x < GBW and FF == True:
            FF = abs[x][y]
            x += 1
        return FF
    def CB(self):
        for i in range(GBH):
            if self.LC(i):
                self.remove(i)
    def remove(self, row):
        for y in range(row, 1, -1):
            for x in range(GBW):
                abs[x][y] = abs[x][y-1]
                abscolour[x][y] = abscolour[x][y-1]
        for x in range(GBW):
            abs[x][0] = False
        self.score += 100
        self.lineremoved = True
        linesound.play()
    def loss(self):
        for x in range(GBW):
            if abs[x][0] == True:
                losssound.play()
                return True
        return False
    def pause(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
        return
    def resetgb(self):
        for x in range(GBW):
            for y in range(GBH):
                abs[x][y] = False
                abscolour[x][y] = (0, 0, 0)