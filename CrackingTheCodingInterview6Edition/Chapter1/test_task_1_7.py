"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.7.
"""
import unittest

from .task_1_7 import nullify_matrix


class TestNullify(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции nullify_matrix().
    """
    def test_matrix(self):
        """
        Тестовый случай, в котором передана матрица с одним нулём.
        """
        input_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]
        valid_output = [
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1],
        ]
        nullified_matrix = nullify_matrix(input_matrix)
        self.assertEqual(nullified_matrix, valid_output)


if __name__ == '__main__':
    unittest.main()
