import unittest
from algorithms import sort_string_with_numbers
from ddt import ddt, data, unpack


@ddt
class SortStringWithNumbersTestCase(unittest.TestCase):
    @data(('is2 Thi1s T4est 3a', 'Thi1s is2 3a T4est'))
    @unpack
    def test_sort(self, sentence, expected):
        self.assertEqual(expected, sort_string_with_numbers.order(sentence))

if __name__ == '__main__':
    unittest.main()
