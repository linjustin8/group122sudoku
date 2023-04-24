import pygame
from board import Board
pygame.init()


screen = pygame.display.set_mode((720, 720))
screen.fill((191, 222, 217))
sudoku_board = Board(720, 720, screen, 0)
sudoku_board.draw()

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

