"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 2. Упражнение 2.5.
"""
import unittest

from linked_list import Node, LinkedList
from task_2_5 import sum_linked_lists, sum_reversed_linked_lists


class TestSumLinkedLists(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции sum_linked_lists().
    """
    def test_linked_lists(self):
        """
        Тестовый случай со стандартыми связными списками с нодами из чисел.
        """
        linked_list_1 = LinkedList()
        linked_list_1.add_node(Node(1))
        linked_list_1.add_node(Node(2))
        linked_list_1.add_node(Node(3))

        linked_list_2 = LinkedList()
        linked_list_2.add_node(Node(4))
        linked_list_2.add_node(Node(5))
        linked_list_2.add_node(Node(6))

        result = [
            node.data
            for node in sum_linked_lists(linked_list_1, linked_list_2)
        ]
        self.assertEqual(result, [5, 7, 9])


class TestSumReversedLinkedLists(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции sum_reversed_linked_lists().
    """
    def test_linked_lists(self):
        """
        Тестовый случай со стандартыми связными списками с нодами из чисел.
        """
        linked_list_1 = LinkedList()
        linked_list_1.add_node(Node(1))
        linked_list_1.add_node(Node(2))
        linked_list_1.add_node(Node(3))

        linked_list_2 = LinkedList()
        linked_list_2.add_node(Node(4))
        linked_list_2.add_node(Node(5))
        linked_list_2.add_node(Node(6))

        result = [
            node.data
            for node in sum_reversed_linked_lists(linked_list_1, linked_list_2)
        ]
        self.assertEqual(result, [9, 7, 5])


if __name__ == '__main__':
    unittest.main()
