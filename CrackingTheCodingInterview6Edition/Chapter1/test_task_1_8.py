"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.8.
"""
import unittest

from .task_1_8 import is_substring


class TestIsSubstring(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции is_substring().
    """
    def test_is_shift_result(self):
        """
        Тестовый случай, где одна строка является результатом циклического
        сдвига другой строки.
        """
        result = is_substring('waterbottle', 'erbottlewat')
        self.assertEqual(result, True)

    def test_is_not_shift_result(self):
        """
        Тестовый случай, где строки не связаны между собой циклическим сдвигом.
        """
        result = is_substring('waterbottle', 'watermelon')
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
