import unittest
from algorithms import sorted_lists
from ddt import ddt, data, unpack


@ddt
class RemoveDuplicatesFromSortedListTestCase(unittest.TestCase):

    @data(([1], [1]),
          ([1, 2, 3, 4], [1, 2, 3, 4]),
          ([1, 1, 2, 3, 4], [1, 2, 3, 4]),
          ([1, 2, 2, 3, 4], [1, 2, 3, 4]),
          ([1, 2, 3, 3, 4], [1, 2, 3, 4]),
          ([1, 2, 3, 4, 4], [1, 2, 3, 4]),
          ([1, 1, 2, 2, 3, 4], [1, 2, 3, 4]),
          ([1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4]),
          ([1, 1, 2, 2, 3, 3, 4, 4], [1, 2, 3, 4]))
    @unpack
    def test_remove_duplicates(self, numbers, expected):
        result = sorted_lists.remove_duplicates(numbers)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
