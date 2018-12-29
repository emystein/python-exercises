import unittest
from algorithms import zigzag_string
from ddt import ddt, data, unpack


@ddt
class ZigZagStringTestCase(unittest.TestCase):

    @data(('A', 1, 'A'),
          ('AB', 1, 'AB'),
          ('ABC', 1, 'ABC'),
          ('AB', 2, 'AB'),
          ('AB', 3, 'AB'),
          ('ABC', 1, 'ABC'),
          ('ABC', 2, 'ACB'),
          ('ABC', 3, 'ABC'),
          ('ABCD', 1, 'ABCD'),
          ('ABCD', 2, 'ACBD'),
          ('ABCD', 3, 'ABDC'),
          ('ABCD', 4, 'ABCD'),
          ('ABCDE', 1, 'ABCDE'),
          ('ABCDE', 2, 'ACEBD'),
          ('ABCDE', 3, 'AEBDC'),
          ('ABCDE', 4, 'ABCED'),
          ('ABCDE', 5, 'ABCDE'),
          ('ABCDEF', 1, 'ABCDEF'),
          ('ABCDEF', 2, 'ACEBDF'),
          ('ABCDEF', 3, 'AEBDFC'),
          ('ABCDEF', 4, 'ABFCED'),
          ('ABCDEF', 5, 'ABCDFE'),
          ('ABCDEF', 6, 'ABCDEF'),
          ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'))
    @unpack
    def test_zigzag(self, input_string, number_of_rows, expected):
        result = zigzag_string.compute(input_string, number_of_rows)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
