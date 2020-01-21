"""
Модульные тесты для проверки задания №2 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from leap_year import is_leap_year


class MyTestCase(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции is_leap_year().
    """
    def test_leap_year(self):
        """
        Тестовый случай с високосным годом.
        """
        self.assertEqual(is_leap_year(2000), True)

    def test_not_leap_year(self):
        """
        Тестовый случай с невисокосным годом.
        """
        self.assertEqual(is_leap_year(2007), False)


if __name__ == '__main__':
    unittest.main()
