import pytest

from tictactoe import *

def test_terminal_returns_true_for_win():
    board = [['X', 'X', 'X'],
            ['O', 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = terminal(board)
    assert result == True

def test_terminal_returns_False_for_still_turns():
    board = [['X', 'O', EMPTY],
            ['X', 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = terminal(board)
    assert result == False

def test_terminal_returns_True_for_tie():
    board = [['O', 'X', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']]
    result = terminal(board)
    assert result == True
