import unittest
from ddt import ddt, data, unpack
from algorithms.multiple_stacks_in_an_array import CircularArrayIndices


@ddt
class CircularArrayIndicesTestCase(unittest.TestCase):
    @data((4, 0, 0, [0]),
          (4, 0, 1, [0, 1]),
          (4, 2, 3, [2, 3]),
          (4, 3, 0, [3, 0]),
          (4, 3, 1, [3, 0, 1]))
    @unpack
    def test_index_range(self, total_capacity, first_index, last_index, expected):
        indices = CircularArrayIndices(total_capacity)
        self.assertEqual(expected, indices.index_range(first_index, last_index))

    @data((3, 0, 1),
          (3, 1, 2),
          (3, 2, 0))
    @unpack
    def test_increment_index(self, array_size, index, expected):
        indices = CircularArrayIndices(array_size)
        self.assertEqual(expected, indices.increment_index(index))

    @data((3, 1, 0),
          (3, 2, 1),
          (3, 0, 2))
    @unpack
    def test_decrement_index(self, array_size, index, expected):
        indices = CircularArrayIndices(array_size)
        self.assertEqual(expected, indices.decrement_index(index))
