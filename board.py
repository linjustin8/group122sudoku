import pygame
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.difficulty = difficulty
    def draw(self):
        # draw horizontal lines
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

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def if_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

