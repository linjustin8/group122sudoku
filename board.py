import pygame
from cell import Cell
from sudoku_generator import generate_sudoku
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.boardy = SudokuGenerator(9,0)
        self.board = generate_sudoku(9, difficulty)
        self.boardy.board = self.board
        self.original = [[self.board[i][j] for j in range(9)]for i in range(9)]
        self.cells = [[Cell(self.board[i][j], i, j, screen) for j in range(9)]for i in range(9)]
        self.selected_x = -1
        self.selected_y = -1

    def draw(self):
        # draw horizontal lines
        self.screen.fill((191, 222, 217))
        for i in range(1, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen,
                                 (0, 0, 0),
                                 (0, i * 80),
                                 (720, i * 80), 5)

            else:
                pygame.draw.line(self.screen,
                                 (0, 0, 0),
                                 (0, i * 80),
                                 (720, i * 80))
        # draw vertical lines
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(self.screen,
                                 (0, 0, 0),
                                 (i * 80, 0),
                                 (i * 80, 720), 5)
            else:
                pygame.draw.line(self.screen,
                                (0,0,0),
                                (i * 80, 0),
                                (i * 80, 720))
        for row in range(9):
            for col in range(9):
                value = str(self.board[row][col])
                self.cells[row][col].draw()

        pygame.draw.rect(self.screen, (255, 0, 0), (self.selected_y * 80, self.selected_x * 80, 80, 80), 5)
        return 1

    def select(self, row, col):
        self.selected_x = row
        self.selected_y = col



    def click(self, x, y):
        row = y // 80
        col = x // 80
        if(row>=9):
            return None
        return (row, col)

    def clear(self):
        self.cells[self.selected_x][self.selected_y].set_cell_value('0')
        self.cells[self.selected_x][self.selected_y].set_sketched_value('0')


    def sketch(self, value):
        self.cells[self.selected_x][self.selected_y].set_sketched_value(str(value))

    def place_number(self, value):
        self.cells[self.selected_x][self.selected_y].set_cell_value(value)

    def reset_to_original(self):
        self.cells = [[Cell(self.original[i][j], i, j, self.screen) for j in range(9)]for i in range(9)]

    def if_full(self):
        for i in range(9):
            for j in range(9):
                if(self.cells[i][j].value == 0):
                    return False
        return True

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cells[i][j].value

    def find_empty(self):
        empty = (-1, -1)
        for i in range(9):
            for j in range(9):
                if (self.cells[i][j].value == 0):
                    empty = (i, j)
                    return empty
        return None

    def check_board(self):
        check = SudokuGenerator(9,0)
        check.board = self.board
        for i in range(9):
            for j in range(9):
                if not check.is_valid(i, j, check.board[i][j]):
                    return False
        return True

