# Guillaume Lochon et Anis Akeb
# Game Of Life
# MD4 @ HETIC


import pygame


def init(WINDOW_HEIGHT, WINDOW_WIDTH):
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 36)
    (width, height) = (WINDOW_HEIGHT, WINDOW_WIDTH)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Sudoku')
    screen.fill(WHITE)
    pygame.display.flip()
    running = True
