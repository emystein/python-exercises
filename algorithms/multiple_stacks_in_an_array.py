from functools import reduce

"""
Implement multiple stacks backed by a single array.

The StackContext class is responsible for wrapping the array and providing Stack instances to the client.

The backend array is considered circular.

[|    ___________     |    ___________     |    ___________     |]
 top1            size1=top2           size2=top3           size3=top1

"""


class Stack(object):
    def __init__(self, context, first_index, capacity, array_indices):
        self.context = context
        self.size = 0
        self.first_index = first_index
        self.last_index = first_index + capacity - 1
        self.capacity = capacity
        self.array_indices = array_indices

    def capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def push(self, element):
        self.context.check_not_full()
        if self.is_full():
            self.grow()
        self.context.set_element_at(element, self.next_index())
        self.size += 1

    def is_full(self):
        return self.size == self.capacity

    def grow(self):
        self.context.next_stack(self).shrink()
        self.capacity += 1
        self.last_index = self.array_indices.increment_index(self.last_index)

    def next_index(self):
        return self.indices()[self.size]

    def indices(self):
        return self.array_indices.index_range(self.first_index, self.last_index)

    def shrink(self):
        if self.size >= self.capacity:
            raise OverflowError

        # move elements forward in the array
        for i in reversed(self.indices()):
            previous = self.array_indices.decrement_index(i)
            self.context.wrapped_array[i] = self.context.wrapped_array[previous]

        self.capacity -= 1
        self.first_index = self.array_indices.increment_index(self.first_index)

    def pop(self):
        element = self.context.pop_element_at(self.last_index)
        self.size -= 1
        self.last_index = self.array_indices.decrement_index(self.last_index)
        return element


class StackContext(object):
    def __init__(self, stack_count, total_capacity):
        if stack_count > total_capacity:
            raise IndexError
        self.total_capacity = total_capacity
        self.wrapped_array = [None for _ in range(total_capacity)]
        self.array_indices = CircularArrayIndices(total_capacity)
        self.stacks = self.create_stacks(stack_count, total_capacity)
        self.stack_indices = self.set_up_stack_indices(self.stacks)

    def create_stacks(self, stack_count, total_capacity):
        capacity = total_capacity // stack_count

        stack_info = []
        first_index = 0
        for i in range(stack_count - 1):
            stack_info.append((first_index, capacity))
            first_index = first_index + capacity

        stack_info.append((first_index, total_capacity - first_index))

        # TODO: use map function to create stacks dictionary
        stacks = []

        for (first_index, capacity) in stack_info:
            stacks.append(Stack(self, first_index, capacity, self.array_indices))

        return stacks

    def set_up_stack_indices(self, stacks):
        stack_indices = {}
        for i in range(len(stacks)):
            stack_indices[self.get_stack(i)] = i
        return stack_indices

    def get_stack(self, index):
        return self.stacks[index]

    def next_stack(self, stack):
        stack_index = self.stack_indices[stack]
        return self.get_stack((stack_index + 1) % len(self.stacks))

    def total_size(self):
        return sum(map(lambda s: s.size, self.stacks))

    def check_not_full(self):
        if self.total_size == self.total_capacity:
            raise OverflowError

    def set_element_at(self, element, index):
        self.wrapped_array[index] = element

    def pop_element_at(self, index):
        element = self.wrapped_array[index]
        self.wrapped_array[index] = None
        return element


class CircularArrayIndices(object):
    def __init__(self, total_capacity):
        self.total_capacity = total_capacity

    def index_range(self, first_index, last_index):
        result = [first_index]

        index = first_index
        while index != last_index:
            index = self.increment_index(index)
            result.append(index)

        return result

    def increment_index(self, index):
        return self.normalize_index(index + 1)

    def decrement_index(self, index):
        return self.normalize_index(index - 1)

    def normalize_index(self, index):
        return index % self.total_capacity
