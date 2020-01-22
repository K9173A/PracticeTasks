"""
Для двух строк напишите метод, определяющий, является ли одна строка
перестановкой другой.
"""
import sys


class String(str):
    """
    Так как в задании указано слово "метод", то это означает, что реализовывать
    нужно в классе строки. Соответственно наследуемся от класса str, чтобы
    расширить его функционал этим методом.
    """
    def is_swappable_of(self, string):
        """
        Проверяет, является ли текущая строка результатом перестановки пере-
        данной строки.
        :param string: строка для сравнения.
        :return: булевой результат. True - если является, False - если нет.
        """
        # Если строка является результатом перестановки другой строки, то такие
        # строки будут совпадать в отсортированном виде.
        left = sorted(self)
        right = sorted(string)
        return left == right


if __name__ == '__main__':
    print(String(sys.argv[1]).is_swappable_of(sys.argv[2]))