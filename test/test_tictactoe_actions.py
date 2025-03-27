import pytest

from tictactoe import *

def test_actions_returns_9_tuples_for_first_go():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = actions(board)
    assert len(result) == 9
    for item in result:
        assert isinstance(item, tuple)

def test_actions_returns_7_tuples_for_third_go():
    board = [['X', 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    result = actions(board)
    assert len(result) == 7
    for item in result:
        assert len(item) == 2
        assert isinstance(item, tuple)
