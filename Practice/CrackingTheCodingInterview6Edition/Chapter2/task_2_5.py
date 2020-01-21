"""
Два числа хранятся в виде связных списков, в которых каждый узел содержит один
разряд. Все цифры хранятся в обратном порядке, при этом первая цифра числа
находится в начале списка. Напишите функцию, которая суммирует два числа и
возвращает результат в виде связного списка. Решите задачу, предполагая, что
цифры записаны в прямом порядке.
"""
from linked_list import Node, LinkedList


def sum_linked_lists(left_list, right_list):
    """
    Суммирует каждый из нодов двух связных списков, возвращая итоговый
    связный список.
    :param left_list: первый связный список.
    :param right_list: второй связный список.
    :return: связный список из просуммированных нодов в прямом порядке.
    """
    result_list = LinkedList()
    left_list_iter = iter(left_list)
    right_list_iter = iter(right_list)
    while True:
        try:
            left_node = next(left_list_iter)
            right_node = next(right_list_iter)
        except StopIteration:
            break
        else:
            result_list.add_node(Node(left_node.data + right_node.data))
    return result_list


def sum_reversed_linked_lists(left_list, right_list):
    """
    Суммирует каждый из нодов двух связных в обратном порядке, возвращая
    итоговый связный список.
    :param left_list: первый связный список.
    :param right_list: второй связный список.
    :return: связный список из просуммированных нодов в обратном порядке.
    """
    result_list = LinkedList()
    nodes_list = []
    left_list_iter = iter(left_list)
    right_list_iter = iter(right_list)
    while True:
        try:
            left_node = next(left_list_iter)
            right_node = next(right_list_iter)
        except StopIteration:
            break
        else:
            nodes_list.append(Node(left_node.data + right_node.data))
    for node in nodes_list[::-1]:
        result_list.add_node(node)
    return result_list
