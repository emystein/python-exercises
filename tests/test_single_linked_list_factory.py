import unittest
from algorithms.lists import LinkedListFactory
from algorithms.list_asserts import SingleLinkedListAssert


class LinkedListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.ass = SingleLinkedListAssert()

    def test_factory_1(self):
        original_list = [1]

        linked_list = LinkedListFactory.create(original_list)

        self.ass.equals(original_list, linked_list)

    def test_factory_2(self):
        original_list = [1, 2]

        linked_list = LinkedListFactory.create(original_list)

        self.ass.equals(original_list, linked_list)

    def test_factory_3(self):
        original_list = [1, 2, 3]

        linked_list = LinkedListFactory.create(original_list)

        self.ass.equals(original_list, linked_list)


if __name__ == '__main__':
    unittest.main()
