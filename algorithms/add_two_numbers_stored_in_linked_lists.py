"""
You are given two linked lists representing two non-negative numbers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
from algorithms.lists import ListNode


def add(l1, l2):
    n1 = reversed_list_to_number(l1)
    n2 = reversed_list_to_number(l2)
    ns = n1 + n2
    s = str(ns)
    return to_linked_list(list(s))


def reversed_list_to_number(l):
    rs = list_values_to_string(l)
    s = rs[::-1]  # reverse string
    return int(s)


def list_values_to_string(l):
    s = ''
    while l is not None:
        s += str(l.val)
        l = l.next
    return s


def to_linked_list(l):
    while len(l) > 0:
        node = ListNode(int(l.pop()))
        node.next = to_linked_list(l)
        return node
    else:
        return None
