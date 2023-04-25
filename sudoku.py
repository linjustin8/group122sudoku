import pygame, sys
from board import Board
pygame.init()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

screen = pygame.display.set_mode((720, 720))
screen.fill(("light blue"))
font = pygame.font.SysFont("arialblack", 30)
draw_text("Welcome to Sudoku!", font, (0,0,0), 190, 200)
draw_text("Select game mode:", font, (0,0,0), 200, 300)




'''screen.fill((191, 222, 217))
sudoku_board = Board(720, 720, screen, 0) # change 0 for difficulty
sudoku_board.draw()
'''
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
