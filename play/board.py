import numpy

from show.draw import *

__row = 3
__col = 3

__board = numpy.zeros([__row, __col])


# whether board is assigned
def isSquareAvailable(row, col):
    if row >= __row or col >= __col:
        return False
    return __board[row][col] == 0


# assign board
def assignSquare(row, col, player):
    __board[row][col] = player


# whether the board is full
def isBoardFull():
    return len([x for row in __board for x in row if x == 0]) == 0


# whether any player win
def isGameOver(player):
    for col in range(__col):
        if __board[0][col] == player and __board[1][col] == player and __board[2][col] == player:
            drawHorizontalWinLine(col, player)
            return True
    for row in range(__row):
        if __board[row][0] == player and __board[row][1] == player and __board[row][2] == player:
            drawVerticalWinLine(row, player)
            return True
    if __board[2][0] == player and __board[1][1] == player and __board[0][2] == player:
        drawAscDiagonal(player)
        return True
    if __board[0][0] == player and __board[1][1] == player and __board[2][2] == player:
        drawDescDiagonal(player)
        return True

    return False


# restart game
def restart():
    drawScreen()
    global __board
    __board = numpy.zeros([__row, __col])
