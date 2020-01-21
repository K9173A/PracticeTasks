"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 1. Упражнение 1.6.
"""
import unittest

from .task_1_6 import turn_image


class TestTurnImage(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции turn_matrix().
    """
    def test_matrix(self):
        """
        Тестовый случай, в котором передана матрица.
        """
        # Исходная матрица (изображение)
        numbers_matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        # Повёрнутая матрица (для проверки)
        turned_matrix = [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]
        output_matrix = turn_image(numbers_matrix)
        self.assertEqual(output_matrix, turned_matrix)


if __name__ == '__main__':
    unittest.main()
