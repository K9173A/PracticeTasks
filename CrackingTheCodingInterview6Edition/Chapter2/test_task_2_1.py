"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 2. Упражнение 2.1.
"""
import unittest

from linked_list import Node, LinkedList
from task_2_1 import remove_duplicates


class TestDeleteDuplicates(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции delete_duplicates().
    """
    def test_linked_list(self):
        """
        Тестовый случай, в создаётся связный список со множественными дуб-
        ликатами.
        """
        letters = LinkedList()
        letters.add_node(Node('A'))
        letters.add_node(Node('B'))
        letters.add_node(Node('B'))
        letters.add_node(Node('A'))
        letters.add_node(Node('A'))
        letters.add_node(Node('A'))
        letters.add_node(Node('C'))
        letters.add_node(Node('C'))
        letters.add_node(Node('C'))
        letters.add_node(Node('D'))
        letters.add_node(Node('D'))
        letters.add_node(Node('A'))
        result_list = [item.data for item in remove_duplicates(letters)]
        self.assertEqual(result_list, ['A', 'B', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
