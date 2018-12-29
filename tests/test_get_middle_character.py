import unittest
from ddt import ddt, data, unpack
from algorithms import get_middle_character


@ddt
class GetMiddleCharacterTestCase(unittest.TestCase):
    @data(('test', 'es'),
          ('testing', 't'),
          ('middle', 'dd'),
          ('A', 'A'))
    @unpack
    def test_get_middle_character(self, word, expected):
        self.assertEqual(expected, get_middle_character.get_middle(word))
