import unittest
from algorithms import lists


class LongestWithoutRepeatingTest(unittest.TestCase):

    def test_string_is_empty(self):
        result = lists.longest_without_repeating('')
        self.assertEqual(0, result)

    def test_string_has_only_one_character(self):
        result = lists.longest_without_repeating('a')
        self.assertEqual(1, result)

    def test_string_doesnt_contain_repeating_characters(self):
        result = lists.longest_without_repeating('abc')
        self.assertEqual(3, result)

    def test_string_contain_only_repeating_characters(self):
        result = lists.longest_without_repeating('aaa')
        self.assertEqual(1, result)

    def test_string_contain_repeating_character_at_the_end_only(self):
        result = lists.longest_without_repeating('abca')
        self.assertEqual(3, result)

    def test_string_contain_repeating_substring_at_the_end_only(self):
        result = lists.longest_without_repeating('abcabc')
        self.assertEqual(3, result)

    def test_repeating_characters_at_the_beginning(self):
        result = lists.longest_without_repeating('aabc')
        self.assertEqual(3, result)

    def test_repeating_characters_at_the_beginning_and_repeating_character_is_different_than_first_of_substring(self):
        result = lists.longest_without_repeating('babc')
        self.assertEqual(3, result)

    def test_repeating_characters_at_the_beginning_and_the_end(self):
        result = lists.longest_without_repeating('aabca')
        self.assertEqual(3, result)

    def test_longest_substring_is_first_one(self):
        result = lists.longest_without_repeating('abcdeabc')
        self.assertEqual(5, result)

    def test_longest_substring_is_first_one_and_repeating_character_at_the_end(self):
        result = lists.longest_without_repeating('abcdeabca')
        self.assertEqual(5, result)

    def test_longest_substring_is_the_second_one(self):
        result = lists.longest_without_repeating('abcabcde')
        self.assertEqual(5, result)

    def test_longest_substring_is_the_second_one_and_repeating_character_at_the_end(self):
        result = lists.longest_without_repeating('abcabcdea')
        self.assertEqual(5, result)

    def test_longest_substring_is_in_the_middle_of_the_string(self):
        result = lists.longest_without_repeating('abcabcdeabc')
        self.assertEqual(5, result)

    def test_longest_substring_is_in_the_middle_of_the_string_with_repeating_character_at_the_beginning(self):
        result = lists.longest_without_repeating('aabcabcdeabc')
        self.assertEqual(5, result)

    def test_longest_substring_is_in_the_middle_of_the_string_with_repeating_character_at_the_end(self):
        result = lists.longest_without_repeating('abcabcdeabcc')
        self.assertEqual(5, result)

    def test_longest_substring_is_in_the_middle_of_the_string_with_repeating_character_at_the_beginning_and_the_end(self):
        result = lists.longest_without_repeating('aabcabcdeabcc')
        self.assertEqual(5, result)

    def test_longest_substring_is_in_the_middle_of_the_string_with_repeating_character_at_the_beginning_and_the_end(self):
        result = lists.longest_without_repeating('aabcabcdeabcc')
        self.assertEqual(5, result)

if __name__ == '__main__':
    unittest.main()
