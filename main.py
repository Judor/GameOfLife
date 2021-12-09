# Guillaume Lochon et Anis Akeb
# Game Of Life
# MD4 @ HETIC


import numpy as np

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):
    number_neighbors = 0  # Creation of the

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

# while True:
#   # Infinite loop that print all the frames . Ctrl + C to stop the computation
#  print(frame)
# frame = compute_next_frame
