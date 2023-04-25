import pygame, sys, os, subprocess
from board import Board
from sudoku_generator import SudokuGenerator
from cell import Cell
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

def draw_progress_menu():
    #initialize buttons and button font
    button_font = pygame.font.SysFont("arialblack", 25)
    reset_button = button_font.render("RESET", 0, (0, 0, 0))
    restart_button = button_font.render("RESTART", 0, (0, 0, 0))
    exit_button = button_font.render("EXIT", 0, (0, 0, 0))

    reset_surface = pygame.Surface((reset_button.get_size()[0] + 20,
                                   reset_button.get_size()[1] + 20))
    reset_surface.fill((204, 216, 217))
    reset_surface.blit(reset_button, (10, 10))

    restart_surface = pygame.Surface((restart_button.get_size()[0] + 20,
                                     restart_button.get_size()[1] + 20))
    restart_surface.fill((204, 216, 217))
    restart_surface.blit(restart_button, (10, 10))

    exit_surface = pygame.Surface((exit_button.get_size()[0] + 20,
                                   exit_button.get_size()[1] + 20))
    exit_surface.fill((204, 216, 217))
    exit_surface.blit(exit_button, (10, 10))

    #create button backgrounds
    reset_rectangle = reset_surface.get_rect(
        center=(220, 760))
    restart_rectangle = restart_surface.get_rect(
        center=(360, 760))
    exit_rectangle = exit_surface.get_rect(
        center=(500, 760))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    # button operations
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_rectangle.collidepoint(event.pos):
                    pass
                elif restart_rectangle.collidepoint(event.pos):
                    # Source: stack overflow - https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input
                    subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
                    pygame.quit()
                elif exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def game_end(sudoku):
    title_font = pygame.font.SysFont("arialblack", 50)
    button_font = pygame.font.SysFont("arialblack", 25)
    if(sudoku.is_full()):
        if(sudoku.check_board()):#if won sudoku game
            draw_text("Game Won!", title_font, (0, 0, 0), 150, 100)
            exit_button = button_font.render("EXIT", 0, (0, 0, 0))
            exit_surface = pygame.Surface((exit_button.get_size()[0] + 20,
                                           exit_button.get_size()[1] + 20))
            exit_surface.fill((204, 216, 217))
            exit_surface.blit(exit_button, (10, 10))
            exit_rectangle = exit_surface.get_rect(
                center=(360, 500))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if exit_rectangle.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                pygame.display.update()
        else:#if lost sudoku game
            draw_text("Game Over!", title_font, (0, 0, 0), 150, 100)
            restart_button = button_font.render("RESTART", 0, (0, 0, 0))
            restart_surface = pygame.Surface((restart_button.get_size()[0] + 20,
                                              restart_button.get_size()[1] + 20))
            restart_surface.fill((204, 216, 217))
            restart_surface.blit(restart_button, (10, 10))
            restart_rectangle = restart_surface.get_rect(
                center=(360, 760))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_rectangle.collidepoint(event.pos):
                            pass
                pygame.display.update()


def main():
    game_over = False
    game_loop = True



    while(game_loop):
        # starting menu screen
        difficulty = start_menu(screen)


        #main playing screen
        screen.fill((191, 222, 217))
        sudoku = Board(720, 720, screen, difficulty)  # change 0 for difficulty
        sudoku.draw()
        for row in range(9):
            for col in range(9):
                value = str(sudoku.board[row][col])
                if value != '0':
                    cell = Cell(value, row, col, screen)
                    cell.draw()


        while True:
            #draw_progress_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = sudoku.click(x,y)
                    print(row, col)
                    sudoku.draw_square(row, col)




            pygame.display.update()



if __name__ == "__main__":
    main()
