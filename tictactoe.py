"""
Tic Tac Toe Player
"""

import math
import copy
from collections import Counter

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
    working_board = copy.deepcopy(board)
    row_index, square_index = action
    if action not in (actions(board)):
        raise Exception('impossible')
    else:
        working_board[row_index][square_index] = player(working_board)
        return working_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # can check rows first
    # then row [index]
    # then diagnals
    for row in board:
        counts = Counter(row)
        if counts['X'] == 3:
            return 'X'
        if counts['O'] == 3:
            return 'O'
    for square_index in range(3):
        counter = 0
        for row in board:
            if row[square_index] == 'X':
                counter += 1
            elif row[square_index] == 'O':
                counter -= 1
            if counter == 3:
                return 'X'
            elif counter == -3:
                return 'O'
    count_down_diag = Counter([board[0][0], board[1][1], board[2][2]])
    count_up_diag = Counter([board[2][0], board[1][1], board[0][2]])
    if count_down_diag['X'] == 3 or count_up_diag['X'] == 3:
        return 'X'
    elif count_down_diag['O'] == 3 or count_up_diag['O'] == 3:
        return 'O'
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not actions(board) or winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winna = winner(board)
    if winna == 'X':
        return 1
    elif winna == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == X:
        current_score = -math.inf
        for action in actions(board):
            updated_score = min_value(result(board, action))    
            if updated_score > current_score:
                current_score = updated_score
                best_move = action
    else:
        current_score = math.inf
        for action in actions(board):
            updated_score = max_value(result(board, action))    
            if updated_score < current_score:
                current_score = updated_score
                best_move = action
    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    current_score = -math.inf
    for action in actions(board):
        current_score = max(current_score, min_value(result(board, action)))
    return current_score    


def min_value(board):
    if terminal(board):
        return utility(board)
    current_score = math.inf
    for action in actions(board):
        current_score = min(current_score, max_value(result(board, action)))
    return current_score    