"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.1.
"""
import unittest

from .task_1_1 import quick_sort, consists_of_unique_chars


class TestQuickSort(unittest.TestCase):
    """
    Набор тестов проверяющих поведение функции quick_sort().
    """
    def test_empty_list(self):
        """
        Тестовый случай с пустым списком.
        """
        result = quick_sort([])
        self.assertEqual(result, [])

    def test_regular_list(self):
        """
        Тестовый случай с обычным списоком из различных символов.
        """
        result = quick_sort(['b', 't', '2', 'f', 'a', 'E', 'e'])
        self.assertEqual(result, ['2', 'E', 'a', 'b', 'e', 'f', 't'])


class TestHasUniqueChars(unittest.TestCase):
    """
    Набор тестов проверяющих поведение функции consists_of_unique_chars().
    """
    def test_unique_string(self):
        """
        Тестовый случай для строки с уникальными символами.
        """
        sorted_string = ''.join(
            quick_sort(['b', 't', '2', 'f', 'a', 'E', 'e'])
        )
        result = consists_of_unique_chars(sorted_string)
        self.assertEqual(result, True)

    def test_repeated_string(self):
        """
        Тестовый случай для строки с повторяющимися символами.
        """
        sorted_string = ''.join(
            quick_sort(['b', 'c', 'g', 'e', 'e', 'e'])
        )
        result = consists_of_unique_chars(sorted_string)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
