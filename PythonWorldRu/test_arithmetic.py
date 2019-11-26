"""
Модульные тесты для проверки задания №1 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from arithmetic import arithmetic


class TestArithmetic(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции arithmetic().
    """
    def setUp(self):
        """
        Устанавливает заранее заготовленные значения для операндов.
        Делается для удобства.
        """
        self.left_operand = 81
        self.right_operand = 9

    def test_sum(self):
        """
        Тестовый случай с операцией сложения.
        """
        result = arithmetic(self.left_operand, self.right_operand, '+')
        self.assertEqual(result, 90)

    def test_subtraction(self):
        """
        Тестовый случай с операцией вычитания.
        """
        result = arithmetic(self.left_operand, self.right_operand, '-')
        self.assertEqual(result, 72)

    def test_division(self):
        """
        Тестовый случай с операцией деления.
        """
        result = arithmetic(self.left_operand, self.right_operand, '/')
        self.assertEqual(result, 9)

    def test_multiplication(self):
        """
        Тестовый случай с операцией умножения.
        """
        result = arithmetic(self.left_operand, self.right_operand, '*')
        self.assertEqual(result, 729)

    def test_undefined_operation(self):
        """
        Тестовый случай с неопределённой операцией.
        """
        with self.assertRaises(ValueError):
            arithmetic(self.left_operand, self.right_operand, '?')

    def test_invalid_operand_type(self):
        """
        Тестовый случай с неверными типами операндов.
        """
        with self.assertRaises(TypeError):
            arithmetic('7', False, '*')


if __name__ == '__main__':
    unittest.main()
