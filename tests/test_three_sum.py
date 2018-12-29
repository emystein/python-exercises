import unittest
from ddt import ddt, data, unpack
from algorithms import three_sum

@ddt
class ThreeSumTestCase(unittest.TestCase):
    @unpack
    @data(([-1, 0, 1], [(-1, 0, 1)]),
          ([-1, 0, 1, 2], [(-1, 0, 1), (-1, 0, 2), (-1, 1, 2), (0, 1, 2)]))
    def test_get_combinations(self, input_list, expected):
        combinations = three_sum.get_combinations(input_list)

        self.assertEqual(expected, list(combinations))

    @unpack
    @data(([(-1, 0, 1), (-1, 0, 2), (-1, 1, 2), (0, 1, 2)], [(-1, 0, 1)]))
    def test_filter_combinations_sum_0(self, combinations, expected):
        filtered = three_sum.filter_combinations_sum_0(combinations)

        self.assertEqual(expected, list(filtered))

    @unpack
    @data(([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]))
    def test_three_sum(self, input_list, expected_result):
        result = three_sum.compute(input_list)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
