# Guillaume Lochon et Anis Akeb
# Game Of Life
# MD4 @ HETIC

import pygame
import numpy as np
import sys

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):
    number_neighbors = 0

    for i in range(index_line - 1, index_line + 2):
        for j in range(index_column - 1, index_column + 2):
            number_neighbors = number_neighbors + paded_frame[i][j]

    number_neighbors = number_neighbors - paded_frame[index_line, index_column]  # Suppression of cell in entry

    # TODO --> Optimize the function to skip the cell in entry
    return number_neighbors


def compute_next_frame(frame):
    # TODO --> create a function that takes in entry a frame and compute the next one according to the rules of the game
    # TODO --> 1rst Step : create the frame with the border :
    paded_frame = np.pad(frame, 1, mode='constant')
    # TODO --> 2nd Step : Create 2 nested loops to compute the paded frame element by element. Be careful about the
    #  start and end index
    #  TODO --> 3rd Step : Inside the previous interation, we call the function to compute the
    #   number of neighbors
    #   TODO --> 4th Step : For each element, test if their is something updated since the last
    #    frame. If it's the case, update the element in the matrix
    return frame


def init(WINDOW_HEIGHT, WINDOW_WIDTH):
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 36)
    (width, height) = (WINDOW_HEIGHT, WINDOW_WIDTH)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game Of Life')
    pygame.display.set_icon(pygame.image.load('resources/icon.png'))

    screen.fill(WHITE)
    pygame.display.flip()
    return True, False


def main():
    argv_list = str(sys.argv)
    nb_rows = 10
    nb_cols = 10
    density = 30
    if len(argv_list) > 2:
        density = argv_list[3]

    weight = (nb_rows + 2) * 10
    height = (nb_cols + 2) * 10

    (running, pause) = init(weight, height)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True

        if not pause:
            pygame.display.update()


if __name__ == "__main__":
    main()
# while True:

#   # Infinite loop that print all the frames . Ctrl + C to stop the computation
#  print(frame)
# frame = compute_next_frame
