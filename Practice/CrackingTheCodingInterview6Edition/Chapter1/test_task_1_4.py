"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.4.
"""
import unittest

from .task_1_4 import replace_whitespaces


class TestReplaceWhitespaces(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции replace_whitespaces().
    """
    def test_normal_input(self):
        """
        Тестовый случай, в котором передана строка пробелами до, в середине
        и в конце строки. Пробелы в начале и конце строки должны быть убраны.
        А проблеы в середине строки заменены на символ '%20'.
        """
        result = replace_whitespaces(' Mr John    Smith ', '%20')
        self.assertEqual(result, 'Mr%20John%20%20%20%20Smith')

    def test_no_whitespaces_input(self):
        """
        Тестовый случай, в котором передана строка без пробелов.
        Функция должна вернуть исходную строку.
        """
        result = replace_whitespaces('MrJohnSmith', '%20')
        self.assertEqual(result, 'MrJohnSmith')


if __name__ == '__main__':
    unittest.main()
