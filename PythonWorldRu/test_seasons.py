"""
Модульные тесты для проверки задания №4 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from seasons import season


class TestSeason(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции square().
    """
    def test_spring(self):
        """
        Тестовый случай с пятым месяцем.
        """
        self.assertEqual(season(5), 'Spring')

    def test_invalid_month_number(self):
        with self.assertRaises(ValueError):
            season(77)


if __name__ == '__main__':
    unittest.main()
