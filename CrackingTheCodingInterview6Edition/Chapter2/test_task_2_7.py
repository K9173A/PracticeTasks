"""
Модульные тесты для проверки задания из книги "Cracking The Coding
Interview 6 Edition". Глава 2. Упражнение 2.7.
"""
import unittest

from linked_list import Node, LinkedList
from task_2_7 import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """
    Набор тестов для проверки поведения функции is_palindrome().
    """
    def test_even_list(self):
        """
        Тестовый случай со связным списком из чётного количества нодов.
        """
        letters = LinkedList()
        letters.add_node(Node('A'))
        letters.add_node(Node('D'))
        letters.add_node(Node('D'))
        letters.add_node(Node('A'))
        result = is_palindrome(letters)
        self.assertEqual(result, True)

    def test_odd_list(self):
        """
        Тестовый случай со связным списком из нечётного количества нодов.
        """
        letters = LinkedList()
        letters.add_node(Node('A'))
        letters.add_node(Node('D'))
        letters.add_node(Node('D'))
        letters.add_node(Node('D'))
        letters.add_node(Node('A'))
        result = is_palindrome(letters)
        self.assertEqual(result, True)

    def test_empty_list(self):
        """
        Тестовый случай с пустым связным списком.
        """
        letters = LinkedList()
        result = is_palindrome(letters)
        self.assertEqual(result, False)

    def test_no_palindrome_list(self):
        """
        Тестовый случай со связным списоком, который не является палиндромом.
        """
        letters = LinkedList()
        letters.add_node(Node('A'))
        letters.add_node(Node('D'))
        letters.add_node(Node('D'))
        letters.add_node(Node('D'))
        result = is_palindrome(letters)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
