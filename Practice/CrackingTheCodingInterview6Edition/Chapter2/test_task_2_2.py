"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 2. Упражнение 2.2.
"""
import unittest

from linked_list import Node, LinkedList
from task_2_2 import find_node


class TestFindNode(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции find_node().
    """
    def test_linked_list(self):
        """
        Тестовый случай со связным списком из букв.
        """
        letters = LinkedList()
        letters.add_node(Node('A'))
        letters.add_node(Node('B'))
        letters.add_node(Node('C'))
        letters.add_node(Node('D'))
        letters.add_node(Node('E'))
        result = find_node(letters, 2).data
        self.assertEqual(result, 'D')


if __name__ == '__main__':
    unittest.main()
