# Guillaume Lochon et Anis Akeb
# Game Of Life
# MD4 @ HETIC

import pygame
import numpy as np
import sys
import optparse
import os
import time


def create_frame():
    return np.array([[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])


# TODO create a function that takes in entry number of rows and cols and returns an array with a given density
def create_density_frame(nb_rows, nb_cols, density):
    return True


def create_frame_from_file(nb_rows, nb_cols, file):
    return np.loadtxt(file).reshape(nb_rows, nb_cols).astype(int)


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


def kill(frame, i, j):
    frame[i][j] = 0


def is_alive(frame, i, j):
    return frame[i][j] == 1


def born(frame, i, j):
    frame[i][j] = 1


def unPad_frame(paded_frame):
    (nb_rows, nb_cols) = np.shape(paded_frame)
    return np.delete(np.delete(paded_frame, [0, nb_rows - 2], 0), [0, nb_cols - 2], 1)


def compute_next_frame(frame):
    paded_frame = np.pad(frame, 1, mode='constant')
    new_frame = paded_frame.copy()
    nb_rows, nb_columns = paded_frame.shape
    update = False

    for i in range(1, nb_rows - 1):
        for j in range(1, nb_columns - 1):
            neighbors = compute_number_neighbors(paded_frame, i, j)
            if is_alive(paded_frame, i, j):
                if neighbors < 2:  # Rule 1
                    kill(new_frame, i, j)
                    update = True
                if neighbors > 3:  # Rule 2
                    kill(new_frame, i, j)
                    update = True
            if neighbors == 3:  # Rule 4
                born(new_frame, i, j)
                update = True

    return update, unPad_frame(new_frame)


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


def terminal_render(file):
    # TODO arrange the update boolean
    if file:
        # TODO find how to get nb_rows & cols from the array in the file. To play with bigger frames
        nb_rows = nb_cols = 7
        frame = np.loadtxt('save.txt').reshape(nb_rows, nb_cols).astype(int)
    else:
        frame = create_frame()
    # Init for the computation loop
    days = 0
    update = True  # Boolean that stops the computation if no change is detected
    print("The first day :")
    print(frame)
    while days < 10:
        time.sleep(0.8)  # Pause in the computation to get to the chance to see the change
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal each time for better visibility
        update, frame = compute_next_frame(frame)
        days = days + 1
        print("Day " + str(days) + " :")
        print(frame)
    print("Fin de la simulation")


if __name__ == "__main__":
    # create OptionParser object
    parser = optparse.OptionParser()

    # While launching the program, type -g to render with pygame, -t to render in the terminal,
    # and -f to import the array from a file

    parser.add_option('-g', dest='graphic', action='store_true',
                      help='Render the game in a graphic window using PyGame')
    parser.add_option('-t', dest='terminal',
                      action='store_true',
                      help='Render the game in a terminal window')
    parser.add_option("-f", dest="import_file",
                      action='store_true',
                      default=False,
                      help="a ")
    (options, args) = parser.parse_args()

    if options.terminal:
        terminal_render(options.import_file)

    elif options.graphic:
        graphic_render()
