import pygame

__LINE_COLOR = (23, 145, 130)
__BG_COLOR = (40, 150, 150)
__SIZE = (600, 600)

__LINE_WIDTH = 15

__CIRCLE_RADIUS = 60
__CIRCLE_WIDTH = 15
__CIRCLE_COLOR = (235, 235, 245)

__CROSS_COLOR = (66, 66, 66)
__CROSS_WIDTH = 25
__SPACE = 55

screen = pygame.display.set_mode(__SIZE)


def initPygame():
    pygame.init()
    pygame.display.set_caption('TicTacToc')


def __drawLine(begin, end):
    pygame.draw.line(screen, __LINE_COLOR, begin, end, __LINE_WIDTH)


def drawScreen():
    screen.fill(__BG_COLOR)
    __drawLine((10, 0), (10, 600))
    __drawLine((200, 10), (200, 600))
    __drawLine((400, 10), (400, 600))
    __drawLine((590, 10), (590, 600))

    __drawLine((0, 10), (600, 10))
    __drawLine((10, 200), (600, 200))
    __drawLine((10, 400), (600, 400))
    __drawLine((10, 590), (600, 590))


def drawFigure(x, row, col):
    if x == 1:
        pygame.draw.circle(screen, __CIRCLE_COLOR, (int(row * 200 + 100), int(col * 200 + 100)), __CIRCLE_RADIUS,
                           __CIRCLE_WIDTH)
    elif x == -1:
        p1 = x1, y1 = row * 200 + __SPACE, col * 200 + 200 - __SPACE
        p2 = x2, y2 = row * 200 + 200 - __SPACE, col * 200 + __SPACE
        p3 = x2, y1
        p4 = x1, y2
        pygame.draw.line(screen, __CROSS_COLOR, p1, p2, __LINE_WIDTH)
        pygame.draw.line(screen, __CROSS_COLOR, p3, p4, __LINE_WIDTH)


def drawVerticalWinLine(col, player):
    posX = col * 200 + 100
    color = __CIRCLE_COLOR if player == 1 else __CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, __SIZE[1] - 15), __LINE_WIDTH)


def drawHorizontalWinLine(row, player):
    posY = row * 200 + 100
    color = __CIRCLE_COLOR if player == 1 else __CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (__SIZE[0] - 15, posY), __LINE_WIDTH)


def drawAscDiagonal(player):
    color = __CIRCLE_COLOR if player == 1 else __CROSS_COLOR
    pygame.draw.line(screen, color, (15, __SIZE[1] - 15), (__SIZE[0] - 15, 15), __LINE_WIDTH)


def drawDescDiagonal(player):
    color = __CIRCLE_COLOR if player == 1 else __CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (__SIZE[0] - 15, __SIZE[1] - 15), __LINE_WIDTH)


def changeTitle(option):
    if option == 1:
        pygame.display.set_caption('Circle Win!Enter R to restart')
    elif option == -1:
        pygame.display.set_caption('Cross Win!Enter R to restart')
    elif option == 0:
        pygame.display.set_caption('Tie.Enter R to restart')
    elif option == 2:
        pygame.display.set_caption('Tic Tac Toc')
