"""
Модульные тесты для проверки задания №8 с сайта:
https://pythonworld.ru/osnovy/tasks.html
"""
import unittest

from xor import xor_cipher, xor_uncipher


class TestXOR(unittest.TestCase):
    """
    Набор тестов для проверки поведения функций xor_cipher() и xor_uncipher().
    """
    def test_string_decryption(self):
        """
        Тестовый случай с шифрованием/дещифрованием строки hello.
        """
        encrypted = xor_cipher('hello', 'apple')
        self.assertEqual(xor_uncipher(encrypted, 'apple'), 'hello')


if __name__ == '__main__':
    unittest.main()
