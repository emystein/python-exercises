import unittest
from ddt import ddt, data, unpack
from algorithms import two_sum


@ddt
class TwoSumTestCase(unittest.TestCase):
    @data(([], 3, []),
          ([3], 3, []),
          ([3, 0], 3, [0, 1]),
          ([0, 3], 3, [0, 1]),
          ([1, 2, 3], 3, [0, 1]),
          ([2, 1, 3], 3, [0, 1]),
          ([1, 3, 2], 3, [0, 2]),
          ([2, 3, 1], 3, [0, 2]),
          ([3, 1, 2], 3, [1, 2]),
          ([3, 2, 1], 3, [1, 2]),
          ([1, 2, 3, 4], 3, [0, 1]),
          ([1, 2, 3, 4], 4, [0, 2]),
          ([1, 2, 3, 4], 5, [0, 3]),
          ([1, 2, 3, 5], 5, [1, 2]),
          ([1, 2, 3, 5], 7, [1, 3]),
          ([1, 2, 3, 5], 8, [2, 3]),
          ([2, 7, 11, 15], 9, [0, 1]),
          ([3, 2, 4], 6, [1, 2]),
          ([-1, 2, 3], 1, [0, 1]),
          ([1, 2, 3, 4, 5], 6, [0, 4]),
          ([1, 2, 3, 4, 5, 6], 8, [1, 5]))
    @unpack
    def test_two_sum(self, original_list, target, expected_result):
        result = two_sum.compute(original_list, target)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
