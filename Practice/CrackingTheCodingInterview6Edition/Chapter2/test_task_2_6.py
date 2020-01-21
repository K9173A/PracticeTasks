"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 2. Упражнение 2.6.
"""
import unittest

from linked_list import LinkedList, Node
from task_2_6 import get_list_circle_root


class MyTestCase(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции get_list_circle_root().
    """
    def test_circled_linked_list(self):
        """
        Тестовый случай, где передан связный список с петлёй на
        ноде со значением 2.
        """
        numbers = LinkedList()
        numbers.add_node(Node(1))
        numbers.add_node(Node(2))
        numbers.add_node(Node(3))
        numbers.add_node(Node(4))
        numbers.add_node(Node(5))
        numbers.peak().next_node = numbers.head_node.next_node
        result = get_list_circle_root(numbers)
        self.assertEqual(result.data, 2)

    def test_standard_linked_list(self):
        """
        Тестовый случай, где передан связный список без петель.
        Функция должна вернуть None.
        """
        numbers = LinkedList()
        numbers.add_node(Node(1))
        numbers.add_node(Node(2))
        numbers.add_node(Node(3))
        numbers.add_node(Node(4))
        numbers.add_node(Node(5))
        result = get_list_circle_root(numbers)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
