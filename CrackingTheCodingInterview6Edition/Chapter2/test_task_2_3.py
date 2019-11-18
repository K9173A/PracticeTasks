"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 2. Упражнение 2.3.
"""
import unittest

from linked_list import Node, LinkedList
from task_2_3 import remove_central_node


class TestRemoveCentralNode(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции remove_central_node().
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
        result_list = [item.data for item in remove_central_node(letters)]
        self.assertEqual(result_list, ['A', 'B', 'D', 'E'])


if __name__ == '__main__':
    unittest.main()
