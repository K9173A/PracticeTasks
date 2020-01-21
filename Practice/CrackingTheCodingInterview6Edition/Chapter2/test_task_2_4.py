"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 2. Упражнение 2.4.
"""
import unittest

from linked_list import Node, LinkedList
from task_2_4 import distribute_nodes


class TestDistributeNodes(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции distribute_nodes().
    """
    def test_numbers(self):
        """
        Тестовый случай со случайно распределёнными числами.
        """
        numbers = LinkedList()
        numbers.add_node(Node(21))
        numbers.add_node(Node(12))
        numbers.add_node(Node(55))
        numbers.add_node(Node(33))
        numbers.add_node(Node(52))
        numbers.add_node(Node(51))
        numbers.add_node(Node(31))
        numbers.add_node(Node(44))
        result_list = [item.data for item in distribute_nodes(numbers, 37)]
        self.assertEqual(result_list, [21, 12, 33, 31, 55, 52, 51, 44])

    def test_ascending_numbers(self):
        """
        Тестовый случай с числами, распределёнными по возрастанию.
        """
        numbers = LinkedList()
        numbers.add_node(Node(1))
        numbers.add_node(Node(2))
        numbers.add_node(Node(3))
        numbers.add_node(Node(4))
        numbers.add_node(Node(5))
        numbers.add_node(Node(6))
        numbers.add_node(Node(7))
        numbers.add_node(Node(8))
        result_list = [item.data for item in distribute_nodes(numbers, 4)]
        self.assertEqual(result_list, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_descending_numbers(self):
        """
        Тестовый случай с числами, распределёнными по убыванию.
        """
        numbers = LinkedList()
        numbers.add_node(Node(8))
        numbers.add_node(Node(7))
        numbers.add_node(Node(6))
        numbers.add_node(Node(5))
        numbers.add_node(Node(4))
        numbers.add_node(Node(3))
        numbers.add_node(Node(2))
        numbers.add_node(Node(1))
        result_list = [item.data for item in distribute_nodes(numbers, 4)]
        self.assertEqual(result_list, [3, 2, 1, 8, 7, 6, 5, 4])


if __name__ == '__main__':
    unittest.main()
