import pytest

from algorithms.distribute_server_workload import distribute


def test_remove_an_specific_element_from_an_array():
    assert distribute(2, 4) == [[0, 1], [2, 3]]
    assert distribute(3, 3) == [[0], [1], [2]]
    assert distribute(3, 9) == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert distribute(2, 5) == [[0, 1, 2], [3, 4]]
    assert distribute(4, 10) == [[0, 1, 2], [3, 4, 5], [6, 7], [8, 9]]
    assert distribute(4, 5) == [[0, 1], [2], [3], [4]]
    assert distribute(1, 1) == [[0]]
    assert distribute(2, 1) == [[0], []]
    assert distribute(5, 4) == [[0], [1], [2], [3], []]
    assert distribute(5, 1) == [[0], [], [], [], []]
