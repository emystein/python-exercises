import pytest
from algorithms import rice_chess


@pytest.mark.parametrize('grains, expected_squares',
    [
    (0, 0),
    (1, 1),
    (2, 2), (3, 2),
    (4, 3), (5, 3), (6, 3), (7, 3),
    (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4),
    (16, 5),
    (32, 6),
    (64, 7)
    ]
)
def test_squares_needed(grains, expected_squares):
    assert expected_squares == rice_chess.squares_needed(grains)
