import unittest
from algorithms import google_minion_labor_shift_1
from ddt import ddt, data, unpack

@ddt
class GoogleTest(unittest.TestCase):

    @data(([1, 2, 3], 0, []),
          ([1, 2, 2, 3, 3, 3, 4, 5, 5], 1, [1, 4]),
          ([1, 2, 3], 6, [1, 2, 3]),
          ([2, 1, 2, 3], 1, [1, 3]))
    @unpack
    def test_answer(self, data, n, expected_output):
        self.assertEqual(expected_output, google_minion_labor_shift_1.answer(data, n))
