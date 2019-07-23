import unittest
from ddt import ddt, data, unpack
from algorithms.lists import LinkedListFactory
from algorithms.lists import SteppedSingleLinkedListIterator
from algorithms import swap_pairs_in_single_linked_list


@ddt
class SwapLinkedListElementsTest(unittest.TestCase):

    @data(([1], [1]), ([1, 2], [2, 1]), ([1, 2, 3], [2, 1, 3]), ([1, 2, 3, 4], [2, 1, 4, 3]), ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]))
    @unpack
    def test_swap_linked_list_elements(self, original_list, expected_list):
        linked_list = LinkedListFactory.create(original_list)

        result = swap_pairs_in_single_linked_list.swap_pairs(linked_list)

        self.assertEqual(expected_list[0], result.val)
        iterator = SteppedSingleLinkedListIterator(result, 1)
        self.verify_list(iterator, expected_list)

    def verify_list(self, iterator, original_list):
        for i in range(0, len(original_list)):
            self.assertTrue(iterator.has_next())
            self.assertEqual(original_list[i], iterator.next().val)

        self.assertFalse(iterator.has_next())

if __name__ == '__main__':
    unittest.main()
