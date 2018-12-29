import unittest
from ddt import ddt, data, unpack
from algorithms import two_strings_to_one


@ddt
class TwoStringsToOneTestCase(unittest.TestCase):
    @data(('xyaabbbccccdefww', 'xxxxyyyyabklmopq', 'abcdefklmopqwxy'))
    @unpack
    def test_two_strings_to_one(self, a, b, expected):
        result = two_strings_to_one.longest(a, b)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
