"""
Модульные тесты для проверки задания №6 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from prime import is_prime


class TestIsPrime(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции is_prime().
    """
    def test_prime(self):
        """
        Тестовый случай с числом, которое является простым.
        """
        self.assertEqual(is_prime(107), True)

    def test_not_prime(self):
        """
        Тестовый случай с числом, которое не является простым.
        """
        self.assertEqual(is_prime(32), False)


if __name__ == '__main__':
    unittest.main()
