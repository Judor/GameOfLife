# Guillaume Lochon et Anis Akeb
# Game Of Life
# MD4 @ HETIC

import pygame
import numpy as np
import sys


def create_frame():
    return np.array([[0, 0, 0, 0, 0, 0, 0],
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


def is_playable(paded_frame, index_line, index_column):  # Test if the given case is in the playable frame or not
    nb_rows, nb_columns = paded_frame.shape
    return (1 > index_line > nb_rows) & (1 > index_column > nb_columns)


def kill(paded_frame, i, j):
    paded_frame[i][j] = 0


def is_alive(paded_frame, i, j):
    return paded_frame[i][j] == 1


def born(paded_frame, i, j):
    paded_frame[i][j] = 1


def unPad_frame(paded_frame):
    return np.delete(np.delete(paded_frame, [0, 7], 0), [0, 7], 1)


def compute_next_frame(frame):
    paded_frame = np.pad(frame, 1, mode='constant')
    nb_rows, nb_columns = paded_frame.shape
    update = False
    for i in range(1, nb_rows - 1):
        for j in range(1, nb_columns - 1):
            if compute_number_neighbors(paded_frame, i, j) >= 3:
                if not is_alive(paded_frame, i, j):
                    born(paded_frame, i, j)
                    update = True
            else:
                kill(paded_frame, i, j)
                update = True

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


def graphic_render():
    frame = create_frame()
    argv_list = str(sys.argv)
    nb_rows = 8
    nb_cols = 8
    density = 30
    if len(argv_list) > 2:
        density = argv_list[3]

    weight = nb_rows * 10
    height = nb_cols * 10

    (running, pause) = init(weight, height)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_p:
                    pause = True

        if not pause:
            #  TODO update print frame each time
            compute_next_frame(frame)
            pygame.display.update()


def terminal_render():
    frame = create_frame()
    argv_list = str(sys.argv)
    # nb_rows = a
    # nb_cols = 8
    # density = 30
    if len(argv_list) > 2:
        density = argv_list[3]
    days = 0
    while days < 10:
        print(frame)
        print(days)
        frame = compute_next_frame(frame)
        days = days + 1


if __name__ == "__main__":
    # graphic_render()
    terminal_render()

# while True:

#   # Infinite loop that print all the frames . Ctrl + C to stop the computation
#  print(frame)
# frame = compute_next_frame
