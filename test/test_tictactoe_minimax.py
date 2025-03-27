import pytest

from tictactoe import *

def test_minimax_returns_coord_for_x_win():
    board = [['X', 'X', EMPTY],
            ['O', 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = minimax(board)
    assert result == (0,2)

def test_minimax_returns_coord_for_o_win():
    board = [['X', 'X', EMPTY],
            ['O', 'O', EMPTY],
            ['X', EMPTY, EMPTY]]
    result = minimax(board)
    assert result == (1,2)

def test_minimax_returns_None_for_no_win():
    board = [['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X']]
    result = minimax(board)
    assert result == None
