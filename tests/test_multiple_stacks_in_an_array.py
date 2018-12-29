import unittest
from ddt import ddt, data, unpack
from algorithms.multiple_stacks_in_an_array import StackContext

@ddt
class MultipleStacksInAnArrayTestCase(unittest.TestCase):

    def test_create_stacks(self):
        stack_count = 3
        total_capacity = 6
        stack_context = StackContext(stack_count, total_capacity)

        for stack in stack_context.stacks:
            self.assertTrue(stack.is_empty())
            self.assertEqual(total_capacity / stack_count, stack.capacity)

    def test_get_stack(self):
        stack_context = StackContext(1, 4)
        stack = stack_context.get_stack(0)
        self.assertIsNotNone(stack)

    def test_stack_indices(self):
        stack_context = StackContext(2, 4)
        for i in range(len(stack_context.stacks)):
            stack = stack_context.get_stack(i)
            self.assertEqual(i, stack_context.stack_indices[stack])

    def test_next_stack_is_second_stack(self):
        stack_context = StackContext(2, 4)
        stack = stack_context.get_stack(0)
        next_stack = stack_context.next_stack(stack)
        self.assertEquals(1, stack_context.stack_indices[next_stack])

    def test_next_stack_is_first_stack(self):
        stack_context = StackContext(2, 4)
        stack = stack_context.get_stack(1)
        next_stack = stack_context.next_stack(stack)
        self.assertEquals(0, stack_context.stack_indices[next_stack])

    def test_reject_to_create_stacks_without_enough_context_capacity(self):
        with self.assertRaises(IndexError):
            stacks = 3
            context_capacity = 2
            StackContext(stacks, context_capacity)

    def test_push(self):
        stack_context = StackContext(2, 2)
        stack = stack_context.get_stack(0)

        stack.push('A')

        self.assertFalse(stack.is_empty())

    def test_push_exhaust_context_capacity(self):
        stack_context = StackContext(1, 1)
        stack = stack_context.get_stack(0)

        stack.push('A')

        with self.assertRaises(OverflowError):
            stack.push('B')

    def test_pop_last_remaining_element(self):
        stack_context = StackContext(2, 2)
        stack = stack_context.get_stack(0)
        stack.push('A')

        self.assertEqual('A', stack.pop())
        self.assertTrue(stack.is_empty())

    def test_shrink_with_available_space(self):
        stack_count = 2
        total_capacity = 4
        stack_context = StackContext(stack_count, total_capacity)
        stack = stack_context.get_stack(1)

        initial_capacity = stack.capacity

        stack.push('A')

        stack.shrink()

        self.assertEqual(initial_capacity - 1, stack.capacity)
        self.assertEqual('A', stack.pop())

    def test_reject_shrink_when_no_space_available(self):
        stack_count = 1
        total_capacity = 1
        stack_context = StackContext(stack_count, total_capacity)
        stack = stack_context.get_stack(0)

        stack.push('A')

        with self.assertRaises(OverflowError):
            stack.shrink()

    def test_grow_first_stack(self):
        stack_count = 2
        total_capacity = 2
        stack_context = StackContext(stack_count, total_capacity)
        stack = stack_context.get_stack(0)
        stack.push('A')
        stack.push('B')

        self.assertEqual('B', stack.pop())
        self.assertEqual('A', stack.pop())

        self.assertEqual(0, stack_context.next_stack(stack).capacity)

    def test_grow_last_stack(self):
        stack_count = 2
        total_capacity = 2
        stack_context = StackContext(stack_count, total_capacity)
        stack = stack_context.get_stack(1)
        stack.push('A')
        stack.push('B')

        self.assertEqual('B', stack.pop())
        self.assertEqual('A', stack.pop())

        self.assertEqual(0, stack_context.next_stack(stack).capacity)

    @data((1, 0, 0), (1, 1, 1), (2, 1, 2), (2, 2, 4))
    @unpack
    def test_total_size(self, stack_count, stack_size, expected_total_size):
        stack_context = StackContext(stack_count, 10)

        for stack in stack_context.stacks:
            for i in range(stack_size):
                stack.push('A')

        self.assertEqual(expected_total_size, stack_context.total_size())

if __name__ == '__main__':
    unittest.main()
