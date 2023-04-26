import pygame

class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = '0'

    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value

        number_font = pygame.font.Font(None, 30)
        num_surface = number_font.render(str(self.sketched_value), 1, "dark gray")
        num_rect = num_surface.get_rect(center=((self.col * 80) + 40,
                                                (self.row * 80) + 40))
        self.screen.blit(num_surface, num_rect)

    def draw(self):
        if self.value != '0' and self.value != 0:
            number_font = pygame.font.Font(None, 50)
            num_surface = number_font.render(str(self.value), 1, "black")
            num_rect = num_surface.get_rect(center =((self.col * 80) + 40,
                                                    (self.row * 80) + 40))
            self.screen.blit(num_surface, num_rect)
            self.sketched_value = '0'

        elif self.sketched_value != '0':
            number_font = pygame.font.Font(None, 30)
            num_surface = number_font.render(str(self.sketched_value), 1, "dark gray")
            num_rect = num_surface.get_rect(center=((self.col * 80) + 40,
                                                    (self.row * 80) + 40))
            self.screen.blit(num_surface, num_rect)


