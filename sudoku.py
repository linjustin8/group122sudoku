import pygame, sys
from board import Board
pygame.init()
screen = pygame.display.set_mode((720, 800))

# Print Title
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    return img
def start_menu(screen):
    # Initialize title font
    title_font = pygame.font.SysFont("arialblack", 40)
    button_font = pygame.font.SysFont("arialblack", 25)
    screen.fill(("light blue"))

    # Print Title
    draw_text("Welcome to Sudoku!", title_font, (0, 0, 0), 150, 100)
    draw_text("Select game mode:", title_font, (0, 0, 0), 160, 300)

    # Make Buttons
    easy_button = button_font.render("Easy", 0, (0,0,0))
    medium_button = button_font.render("Medium", 0, (0, 0, 0))
    hard_button = button_font.render("Hard", 0, (0, 0, 0))

    # Initialize button Background color and text
    easy_surface = pygame.Surface((easy_button.get_size()[0] + 20,
                                   easy_button.get_size()[1] + 20))
    easy_surface.fill((204, 216, 217))
    easy_surface.blit(easy_button, (10,10))

    medium_surface = pygame.Surface((medium_button.get_size()[0] + 20,
                                   medium_button.get_size()[1] + 20))
    medium_surface.fill((204, 216, 217))
    medium_surface.blit(medium_button, (10, 10))

    hard_surface = pygame.Surface((hard_button.get_size()[0] + 20,
                                   hard_button.get_size()[1] + 20))
    hard_surface.fill((204, 216, 217))
    hard_surface.blit(hard_button, (10, 10))


    # Make rectangle around button
    easy_rectangle = easy_surface.get_rect(
        center = (220, 500))
    medium_rectangle = medium_surface.get_rect(
        center=(360, 500))
    hard_rectangle = hard_surface.get_rect(
        center=(500, 500))
    # Print Button
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30 # Returns 30 for Easy
                elif medium_rectangle.collidepoint(event.pos):
                    return 40 # Returns 40 For Medium
                elif hard_rectangle.collidepoint(event.pos):
                    return 50 # Returns 50 for Hard
        pygame.display.update()




difficulty = start_menu(screen)



screen.fill((191, 222, 217))
sudoku_board = Board(720, 720, screen, difficulty) # change 0 for difficulty
sudoku_board.draw()

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
