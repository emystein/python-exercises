import unittest

from algorithms.lists import ListNode


class SingleLinkedListAssert(unittest.TestCase):

    def equals(self, original_list, linked_list):
        node = ListNode(linked_list.val)
        node.next = linked_list.next

        for i in range(0, len(original_list)):
            self.assertEqual(original_list[i], node.val)
            node = node.next
            if i == len(original_list) - 1:
                self.assertIsNone(node)
