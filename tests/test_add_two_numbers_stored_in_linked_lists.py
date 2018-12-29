import unittest
from ddt import ddt, data, unpack
from algorithms.lists import LinkedListFactory
from algorithms.list_asserts import SingleLinkedListAssert
import algorithms.add_two_numbers_stored_in_linked_lists as add_two_numbers


@ddt
class AddTwoNumbersStoredInLinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.ass = SingleLinkedListAssert()

    @data(([1, 2, 3], '123'))
    @unpack
    def test_list_values_to_string(self, l, expected):
        ll = LinkedListFactory.create(l)

        result = add_two_numbers.list_values_to_string(ll)

        self.assertEqual(expected, result)

    @data(([0], [0], [0]),
          ([0], [1], [1]),
          ([1], [0], [1]),
          ([1], [1], [2]),
          ([1, 0], [1, 0], [2]),
          ([2], [0, 1], [2, 1]),
          ([0, 1], [2], [2, 1]),
          ([2, 4, 3], [5, 6, 4], [7, 0, 8]))
    @unpack
    def test_add_numbers_as_linked_lists(self, number1, number2, expected):
        list_number1 = LinkedListFactory.create(number1)
        list_number2 = LinkedListFactory.create(number2)

        result = add_two_numbers.add(list_number1, list_number2)

        self.ass.equals(expected, result)


if __name__ == '__main__':
    unittest.main()
