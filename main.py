# Guillaume Lochon et Anis Akeb
# Game Of Life
# MD4 @ HETIC

import pygame
import numpy as np
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


def compute_number_neighbors(paded_frame, index_line, index_column):
    number_neighbors = 0

    for i in range(index_line - 1, index_line + 2):
        for j in range(index_column - 1, index_column + 2):
            number_neighbors = number_neighbors + paded_frame[i][j]

    number_neighbors = number_neighbors - paded_frame[
        index_line, index_column]  # Suppression of cell in entry to not count it twice

    return number_neighbors


def kill(frame, i, j):
    frame[i][j] = 0


# returns a True or False boolean to tell if the frame contains a living cell at this very point
def is_alive(frame, i, j):
    return frame[i][j] == 1


def new_cell(frame, i, j):
    frame[i][j] = 1


def unPad_frame(paded_frame):
    (nb_rows, nb_columns) = np.shape(paded_frame)
    return np.delete(np.delete(paded_frame, [0, nb_rows - 2], 0), [0, nb_columns - 2], 1)  # Suppression of the borders
    # : first and last row and column witch are the axis 0 & 1


def compute_next_frame(frame):
    paded_frame = np.pad(frame, 1, mode='constant')
    new_frame = paded_frame.copy()  # We will work on the copy of the frame to not alter it while we're running
    # through it
    nb_rows, nb_columns = paded_frame.shape
    update = False  # Set the update boolean to false to stop the computation if no change is detected

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
                new_cell(new_frame, i, j)
                update = True
    return update, unPad_frame(new_frame)


def init(WINDOW_HEIGHT, WINDOW_WIDTH):
    pygame.init()
    WHITE = (255, 255, 255)
    (width, height) = (WINDOW_HEIGHT, WINDOW_WIDTH)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game Of Life')
    pygame.display.set_icon(pygame.image.load('resources/icon.png'))

    screen.fill(WHITE)
    pygame.display.flip()
    return True, False


def graphic_render(file):
    if file == 'default':
        frame = create_frame()
    else:
        frame = np.loadtxt(file).astype(int)

    nb_rows, nb_columns = frame.shape
    weight = nb_rows * 10
    height = nb_columns * 10

    (running, pause) = init(weight, height)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_p:
                    pause = True

        if not pause:
            compute_next_frame(frame)
            pygame.display.update()


def terminal_render(file, max_days):
    if file == 'default':
        frame = create_frame()
    else:
        frame = np.loadtxt(file).astype(int)
    # Init for the computation loop
    days = 0
    update = True  # Boolean that stops the computation if no change is detected
    print("The first day :")
    print(frame)
    while (days < max_days) & update:
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
    parser.add_option("-f", "--filename", dest='test', type='str', metavar='STR',
                      help="Use the array in the file to create the frame")
    (options, args) = parser.parse_args()

    days_max = 50
    if options.terminal:
        if options.test:
            terminal_render(options.test, days_max)
        else:
            terminal_render('default', days_max)

    elif options.graphic:
        graphic_render('file')
