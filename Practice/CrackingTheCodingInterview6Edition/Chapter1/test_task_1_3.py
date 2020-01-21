"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.3.
"""
import unittest

from .task_1_3 import String


class TestIsSwappableOf(unittest.TestCase):
    """
    Набор тестов для проверки поведения метода is_swappable_of() класса String.
    """
    def setUp(self):
        """
        Заранее устанавливаем исходную строку, которую будем использовать
        в тестовых случаях.
        :return: None.
        """
        self.left = String('Hello World')

    def test_is_swappable(self):
        """
        Тестовый случай, в котором передана строка, являющаяся
        результатом перестановки.
        """
        result = self.left.is_swappable_of('World olleH')
        self.assertEqual(result, True)

    def test_is_not_swappable(self):
        """
        Тестовый случай, в котором передана строка, не являющаяся
        результатом перестановки.
        """
        result = self.left.is_swappable_of('World Hell')
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
