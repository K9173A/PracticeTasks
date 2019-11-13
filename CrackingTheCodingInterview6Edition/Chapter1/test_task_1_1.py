"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.1.
"""
import unittest

from .task_1_1 import quick_sort, consists_of_unique_chars


class TestQuickSort(unittest.TestCase):
    """
    Set of tests checking quick_sort() function.
    """
    def test_empty_list(self):
        """
        Test that quick_sort can handle empty list.
        """
        result = quick_sort([])
        self.assertEqual(result, [])

    def test_regular_list(self):
        """
        Test case for the list with characters.
        """
        result = quick_sort(['b', 't', '2', 'f', 'a', 'E', 'e'])
        self.assertEqual(result, ['2', 'E', 'a', 'b', 'e', 'f', 't'])


class TestHasUniqueChars(unittest.TestCase):
    """
    Set of tests checking consists_of_unique_chars() function.
    """
    def test_unique_string(self):
        """
        Test case for the string with unique characters.
        Function should return True.
        """
        sorted_string = ''.join(
            quick_sort(['b', 't', '2', 'f', 'a', 'E', 'e'])
        )
        result = consists_of_unique_chars(sorted_string)
        self.assertEqual(result, True)

    def test_repeated_string(self):
        """
        Test case for the string with repeated characters.
        Function should return False.
        """
        sorted_string = ''.join(
            quick_sort(['b', 'c', 'g', 'e', 'e', 'e'])
        )
        result = consists_of_unique_chars(sorted_string)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
