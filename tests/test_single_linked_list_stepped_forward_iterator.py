import unittest
from algorithms.lists import LinkedListFactory
from algorithms.lists import SteppedSingleLinkedListIterator
from ddt import ddt, data, unpack


@ddt
class SteppedSingleLinkedListIteratorTest(unittest.TestCase):

    @data(([1], 2), ([1, 2], 2), ([1, 2, 3, 4], 2))
    @unpack
    def test_stepped_iterator(self, original_list, step):
        linked_list = LinkedListFactory.create(original_list)

        iterator = SteppedSingleLinkedListIterator(linked_list, step)

        self.verify_iterator(iterator, original_list, step)

    def verify_iterator(self, iterator, original_list, step):
        for i in range(0, len(original_list), step):
            self.assertTrue(iterator.has_next())
            self.assertEqual(original_list[i], iterator.next().val)

        self.assertFalse(iterator.has_next())


if __name__ == '__main__':
    unittest.main()