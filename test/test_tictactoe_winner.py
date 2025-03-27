import pytest

from tictactoe import *

def test_winner_returns_x_for_x_row_win():
    board = [['X', 'X', 'X'],
            ['O', 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = winner(board)
    assert result == 'X'

def test_winner_returns_x_for_x_col_win():
    board = [['X', 'O', EMPTY],
            ['X', 'O', EMPTY],
            ['X', EMPTY, EMPTY]]
    result = winner(board)
    assert result == 'X'

def test_winner_returns_o_for_o_diag_win():
    board = [['O', 'X', 'X'],
            [EMPTY, 'O', EMPTY],
            [EMPTY, 'X', 'O']]
    result = winner(board)
    assert result == 'O'

def test_winner_returns_None_for_tie():
    board = [['O', 'X', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']]
    result = winner(board)
    assert result == None
