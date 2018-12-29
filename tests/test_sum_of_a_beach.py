import unittest
from ddt import ddt, data, unpack
import algorithms.sum_of_a_beach as sum_of_a_beach


@ddt
class SumOfABeachTestCase(unittest.TestCase):
    @data(('WAtErSlIde', 1),
          ('GolDeNSanDyWateRyBeaChSuNN', 3),
          ('gOfIshsunesunFiSh', 4),
          ('cItYTowNcARShoW', 0))
    @unpack
    def test_sum_of_a_beach(self, input, expected):
        result = sum_of_a_beach.apply(input)
        self.assertEqual(expected, result)
