"""
Допустим, что существует метод is_substring, проверяющий, является ли одно
слово подстрокой другого. Для двух строк, s1 и s2, напишите код проверки,
получена ли строка s2 циклическим сдвигом s1, используя только один вызов
метода is_substring (пример: слово waterbottle получено циклическим сдвигом
erbottlewat).
"""
import collections


def shift_left(string, n):
    """
    Циклически сдвигает строку на n позиций влево.
    :param string: строка, которую нужно сдвинуть.
    :param n: количество позиций для сдвига.
    :return: строка с циклическим сдвигом влево на n позиций.
    """
    deque_string = collections.deque(string)
    for _ in range(n):
        # При передаче негативного значения - сдвиг влево.
        # При передаче негативного значения - сдвиг вправо.
        deque_string.rotate(-n)
    return ''.join(deque_string)


def is_substring(string1, string2):
    """
    Проверяет, является ли строка результатом циклического сдвига другой
    строки.
    :param string1: первая строка.
    :param string2: вторая строка.
    :return: если строка является результатом циклического сдвига другой
    строки, то возвращает True, в ином случае возвращает False.
    """
    for _ in range(len(string1)):
        if string1 == string2:
            return True
        string1 = shift_left(string1, 1)
    return False


if __name__ == '__main__':
    print(is_substring('waterbottle', 'erbottlewat'))
