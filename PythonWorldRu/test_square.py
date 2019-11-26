"""
Модульные тесты для проверки задания №3 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from square import square


class TestSquare(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции square().
    """
    def test_square(self):
        """
        Тестовый случай с квадратом со стороной 5.
        """
        self.assertEqual(square(5), (20, 25, 7.0710678118654755))


if __name__ == '__main__':
    unittest.main()
