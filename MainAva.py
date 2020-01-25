import pygame
import time
import copy
from Block_Cayden import Block
from GameBoard_Cayden import gameboard
from Shape_Cayden import shape

pygame.init()
tick = 0
tickm = 0
delay = 1
delaym = 4
tickplus = 0.03
scorefont = pygame.font.SysFont('freesans.ttf', 30)
titlefont = pygame.font.SysFont('Times New Roman', 60)
sshape = False

# RGB colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)


def keypress(done):
    global sshape
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                s.rotate_cc()
            elif event.key == pygame.K_x:
                s.rotate_cw()
            elif event.key == pygame.K_r:
                g.resetgb()
                g.score = 0
                s.active = False
                draw_all(screen)
            elif event.key == pygame.K_SPACE:
                s.harddrop()
            elif event.key == pygame.K_ESCAPE:
                g.pause()
            elif event.key == pygame.K_BACKSPACE:
                g.remove(19)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        time.sleep(0.1)
        s.move_down()
    if keys[pygame.K_RIGHT]:
        s.move_right()
    if keys[pygame.K_LEFT]:
        s.move_left()
    if keys[pygame.K_n]:
        sshape = True
    return False
def draw_all(screen):
    screen.fill(BLACK)
    g.draw_gb(screen)
    s.draw_shape(screen)
    shapepreview.draw_copy_shape(screen)
    arrowtext = scorefont.render('Arrow Keys = Move falling block', 1, WHITE)
    Ztext = scorefont.render('\'Z\' = Rotate counter-clockwise', 1, WHITE)
    Xtext = scorefont.render('\'X\' = Rotate clockwise', 1, WHITE)
    spacetext = scorefont.render('\'Space\' = Hard drop', 1, WHITE)
    restarttext = scorefont.render('\'R\' = Reset game', 1, WHITE)
    escapetext = scorefont.render('\'Escape\' = Pause', 1, WHITE)
    scoretext = scorefont.render('Score: '+str(g.score), 1, WHITE)
    titletext = titlefont.render('Tetris Avalanche', 1, WHITE)
    screen.blit(scoretext, (110, 515))
    screen.blit(titletext, (360, 20))
    screen.blit(arrowtext, (400, 110))
    screen.blit(Ztext, (410, 150))
    screen.blit(Xtext, (445, 190))
    screen.blit(restarttext, (475, 230))
    screen.blit(spacetext, (465, 270))
    screen.blit(escapetext, (475, 310))
    pygame.draw.line(screen, RED, (360, 70), (500, 35), 4)
    pygame.draw.line(screen, RED, (360, 35), (500, 70), 4)
if __name__ == "__main__":
    size = (800, 600)
    xpos = 0
    ypos = 0
    bsize = 50

    b = Block(RED, xpos, ypos)
    g = gameboard(BLUE)
    s = shape()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Avalanche")


done = False
while not done:

    shapepreview = copy.deepcopy(s)

    shapepreview.copydrop()

    draw_all(screen)

    time.sleep(0.025)
    tick += tickplus
    tickm += 1

    if sshape == True:
        s = shape()
        sshape = False
    if tick >= delay:
        s.move_down()
        tick = 0
    if tickm >= delaym:
        done = keypress(done)
        tickm = 0
    if s.active == False:
        g.CB()
        if g.lineremoved:
            tickplus += 0.005
            print(tickplus)
            g.lineremoved = False
        if g.loss():
            g.resetgb()
            g.score = 0
        s = shape()
    pygame.display.flip()