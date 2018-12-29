from algorithms.lists import ListNode

"""
Given a linked list, swap every two adjacent nodes and return its head.

For example, given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.

You may not modify the values in the list, only nodes itself can be changed.
"""


def swap_pairs(linked_list):
    return swap_pairs_recursive(linked_list, True)


def swap_pairs_recursive(linked_list, is_odd_node):

    if linked_list is not None:
        if is_odd_node:
            linked_list = swap_current_and_next(linked_list, linked_list.next)
        linked_list.next = swap_pairs_recursive(linked_list.next, not is_odd_node)

    return linked_list


def swap_current_and_next(current_node, next_node):
    if next_node is not None:
        new_next = ListNode(current_node.val)
        new_next.next = next_node.next

        current_node = ListNode(next_node.val)
        current_node.next = new_next

        return current_node
    else:
        return current_node
