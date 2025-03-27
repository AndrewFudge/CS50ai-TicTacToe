import pytest

from tictactoe import *

def test_player_returns_x_for_first_go():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = player(board)
    assert result == 'X'

def test_player_returns_o_for_second_go():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, 'X', EMPTY]]
    result = player(board)
    assert result == 'O'

def test_player_returns_x_for_third_go():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = player(board)
    assert result == 'X'

def test_player_returns_x_for_fith_go():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, 'O', EMPTY],
            ['O', EMPTY, 'X']]
    result = player(board)
    assert result == 'X'