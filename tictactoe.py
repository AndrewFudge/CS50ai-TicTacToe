"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if board empty, return x
    # count X and O
    # return least
    counter = 0
    for row in board:
        for each in row:
            if each == 'X':
                counter += 1
            elif each == 'O':
                counter -= 1
    if counter == 0:
        return 'X'
    elif counter == 1:
        return 'O'
    else:
        raise Exception('Too many of one player on the board!')
            


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos_actions = set()
    for row_index, row in enumerate(board):
        for square_index, square in enumerate(row):
            if not square:
                pos_actions.add((row_index, square_index))
    return pos_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
