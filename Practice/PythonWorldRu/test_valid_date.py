"""
Модульные тесты для проверки задания №7 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from valid_date import date


class TestDate(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции date().
    """
    def test_valid_date(self):
        """
        Тестовый случай с существующей датой.
        """
        self.assertEqual(date(29, 2, 2020), True)

    def test_invalid_date(self):
        """
        Тестовый случай с несуществующей датой.
        """
        self.assertEqual(date(30, 2, 2020), False)


if __name__ == '__main__':
    unittest.main()
