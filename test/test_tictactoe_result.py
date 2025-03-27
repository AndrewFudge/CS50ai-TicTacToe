import pytest

from tictactoe import *

def test_result_returns_x_for_first_go():
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    action = (0,0)
    expected = [['X', EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    response = result(board, action)
    assert response == expected
    assert response is not board

def test_result_returns_o_for_second_valid_go():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    action = (1,1)
    expected = [['X', EMPTY, EMPTY],
            [EMPTY, 'O', EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    response = result(board, action)
    assert response == expected
    assert response is not board

def test_result_returns_error_for_invalid_action():
    board = [['X', EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    action = (0,0)
    expected = [['X', EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    with pytest.raises(Exception):
        result(board, action)


# def test_result_returns_x_for_fith_go():
#     board = [['X', EMPTY, EMPTY],
#             [EMPTY, 'O', EMPTY],
#             ['O', EMPTY, 'X']]
#     result = result(board)
#     assert result == 'X'