import pytest

from tictactoe import *

def test_utility_returns_1_for_x_win():
    board = [['X', 'X', 'X'],
            ['O', 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = utility(board)
    assert result == 1

def test_utility_returns_minus_1_for_o_win():
    board = [['O', 'X', 'X'],
            [EMPTY, 'O', EMPTY],
            [EMPTY, 'X', 'O']]
    result = utility(board)
    assert result == -1

def test_utility_returns_0_for_tie():
    board = [['O', 'X', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']]
    result = utility(board)
    assert result == 0
