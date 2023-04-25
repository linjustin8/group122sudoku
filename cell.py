import pygame

class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        pass

    def draw(self):

        number_font = pygame.font.Font(None, 20)
        num_surface = number_font.render(str(self.value), 0, "black")
        num_rect = num_surface.get_rect(center =((self.row * 80) + 40,
                                                (self.col * 80) + 40))
        self.screen.blit(num_surface, num_rect)


