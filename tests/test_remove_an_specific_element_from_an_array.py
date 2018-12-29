import pytest

from algorithms.remove_an_specific_element_from_an_array import select_subarray

def test_remove_an_specific_element_from_an_array():
    assert select_subarray([1, 23, 2, -8, 5]) == [3, -8]
    assert select_subarray([1, 3, 23, 4, 2, -8, 5, 18]) == [2, 23]
    assert select_subarray([10, 20, -30, 100, 200]) == [[3, 100], [4, 200]]