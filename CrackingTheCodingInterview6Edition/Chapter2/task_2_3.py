"""
Реализуйте алгоритм, удаляющий узел из середины односвязного списка (доступ дан
только к этому узлу).
"""
import math


def remove_central_node(linked_list):
    """
    Удаляет центральный нод из связного списка.
    :param linked_list: связный список.
    :return: свящный список с удалённым центральным нодом.
    """
    # В конце вычитаем единицу, потому что индексация начинается с нуля.
    central_node_index = math.ceil(sum(1 for _ in linked_list) / 2) - 1
    previous_node = None
    for i, node in enumerate(linked_list):
        # Аналогично заданию 2.1, делаем связку предыдущего и следуюшего нода.
        if i == central_node_index:
            previous_node.next_node = node.next_node
        else:
            previous_node = node
    return linked_list
