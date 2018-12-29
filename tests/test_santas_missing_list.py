import unittest

from algorithms.santas_missing_list import gifts, previous_power_of_2

class SantasMissingListTest(unittest.TestCase):
    def test(self):
        self.assertEqual(['Toy Soldier'], gifts(1))
        self.assertEqual(['Wooden Train'], gifts(2))
        self.assertEqual(['Toy Soldier', 'Wooden Train'], gifts(3))
        self.assertEqual(['Hoop'], gifts(4))
        self.assertEqual(['Hoop', 'Toy Soldier'], gifts(5))
        self.assertEqual(['Hoop', 'Horse', 'Wooden Train'], gifts(22))
        self.assertEqual(['Football', 'Teddy'], gifts(160))

    def test_closest_lower_power_of_2(self):
        self.assertEqual(1, previous_power_of_2(1))
        self.assertEqual(2, previous_power_of_2(2))
        self.assertEqual(2, previous_power_of_2(3))
        self.assertEqual(4, previous_power_of_2(4))
