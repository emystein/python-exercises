import unittest
from algorithms.stop_gninnips_my_sdrow import spin_words

class SpinWordsTest(unittest.TestCase):
    def test(self):
        self.assertEqual('Hey wollef sroirraw', spin_words('Hey fellow warriors'))
        self.assertEqual('This is a test', spin_words('This is a test'))
        self.assertEqual('This is rehtona test', spin_words('This is another test'))