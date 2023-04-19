import pygame

pygame.init()

screen = pygame.display.set_mode((1000,1000))

while True:
    screen.fill("purple")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
