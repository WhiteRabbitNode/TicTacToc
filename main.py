from sys import exit

from play.board import *
from show.music import *

initPygame()
drawScreen()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            row = event.pos[0] // 200
            col = event.pos[1] // 200
            if isSquareAvailable(row, col):
                assignSquare(row, col, player)
                drawFigure(player, row, col)
                music('tool/click.wav')
                if isGameOver(player):
                    game_over = True
                    changeTitle(player)
                elif isBoardFull():
                    game_over = True
                    changeTitle(0)
                player = -player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
                changeTitle(2)
    pygame.display.update()