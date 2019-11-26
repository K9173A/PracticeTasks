"""
Модульные тесты для проверки задания №5 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from bank import bank


class TestBank(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции bank().
    """
    def test_bank(self):
        """
        Тестовый случай с обычным банковским вкладом.
        """
        self.assertEqual(bank(10000, 7), 19487)


if __name__ == '__main__':
    unittest.main()
