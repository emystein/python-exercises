class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "ListNode: {}. Next: {}" % (self.val, self.next)


class LinkedListFactory(object):

    @staticmethod
    def create(original_list):
        if len(original_list) == 0:
            return

        node = ListNode(original_list[0])
        first_node = node

        for e in original_list[1:]:
            new_node = ListNode(e)
            node.next = new_node
            node = new_node

        return first_node


class SteppedSingleLinkedListIterator(object):

    def __init__(self, list_node, step):
        self.list_node = list_node
        self.step = step
        self.count = 0

    def __iter__(self):
        return self

    def has_next(self):
        node = self.list_node

        if self.count > 0:
            for i in range(1, self.step + 1):
                if node.next is not None:
                    node = node.next
                else:
                    return False

        return node is not None

    def next(self):
        return self.__next__()

    def __next__(self):
        if self.count > 0:
            for i in range(1, self.step + 1):
                if self.list_node.next is not None:
                    self.list_node = self.list_node.next
                else:
                    raise StopIteration

        self.count += 1

        return self.list_node

def longest_without_repeating(original_string):
    result = 0

    for i in range(0, len(original_string)):
        partial_count = 0

        for c in range(i, len(original_string)):
            substring = original_string[i:c+1]
            current_character = original_string[c]
            if substring.count(current_character) > 1:
                break
            partial_count += 1

        result = max(result, partial_count)

    return result

