"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.5.
"""
import unittest

from .task_1_5 import compress_string


class TestCompressString(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции compress_string().
    """
    def test_standard_string(self):
        """
        Тестовый случай, в котором передана стандартная строка.
        Фукнкция должна её сжать и вернуть результат.
        """
        result = compress_string('aabcccccaaaf')
        self.assertEqual(result, 'a2b1c5a3f1')

    def test_standard_string2(self):
        """
        Тестовый случай, в котором проверяется случай, когда
        последние символы одинаковые.
        """
        result = compress_string('aaaaaaaa')
        self.assertEqual(result, 'a8')

    def test_unique_string(self):
        """
        Тестовый случай, в котором передана строка без повторяющихся символов,
        поэтому сжатая строка оказывается длиннее, чем исходная. Функция в
        этом случае должна вернуть исходную строку.
        """
        result = compress_string('abcdefg')
        self.assertEqual(result, 'abcdefg')


if __name__ == '__main__':
    unittest.main()
