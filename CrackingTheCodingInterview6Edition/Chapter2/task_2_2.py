"""
Реализуйте алгоритмы для поиска в одновязном списке k-го элемента с конца.
"""
from linked_list import Node, LinkedList


def find_node(linked_list, n):
    """
    Находит нод, который располагается на n-ой позиции с конца.
    :param linked_list: связный список.
    :param n: число, которое отражает индекс нода с конца.
    :return: нод по заданной позиции.
    """
    index = sum(1 for _ in linked_list) - n
    # Если размер связного списка больше, чем переданный индекс,
    # то будет выкинуто исключение.
    if index < 0:
        raise IndexError

    for i, node in enumerate(linked_list):
        if i == index:
            return node
