"""
Напишите код, удаляющий дубликаты из несортированного связного списка.
"""
from linked_list import Node, LinkedList


def remove_duplicates(linked_list):
    """
    Удаляет из переданного связного списка дубликаты. То есть ноды,
    которые имеют одинаковые значения в атрибуте data.
    :param linked_list: связный список.
    :return: связный список без дубликатов.
    """
    # Начинаем итерацию с корневого нода.
    current_node = linked_list.head_node
    # Если нод не равен None, то он существует.
    while current_node:
        # Предыдущий нод нужет, чтобы в ситуации если текущий нод является
        # дубликатом, связать предыдущий нод и следующий, тем самым отвязав
        # текущий нод из цепочки ссылок в связном списке.
        previous_node = None
        for node in linked_list:
            # 1) Если previous_node равен None, то у нас нет предудущего нода,
            # 2) Данное условие нужно, чтобы не сравнивать нод с самим собой,
            # так как он удалится в таком случае.
            # 3) Если значения совпадают, то это дубликаты.
            if previous_node \
                    and current_node is not node \
                    and current_node.data == node.data:
                # Перезаписываем ссылку на следующий нод в предыдущий элемент, если
                # таковой имеется. Таким образом на дубликат никаких ссылок больше
                # не будет и мусоросборщик удалит его из памяти.
                previous_node.next_node = node.next_node
            # Если значения отличны друг от друга, то просто переписываем в
            # previous_node ссылку на текущий нод.
            else:
                previous_node = node
        current_node = current_node.next_node
    return linked_list


if __name__ == '__main__':
    letters = LinkedList()
    letters.add_node(Node('A'))
    letters.add_node(Node('B'))
    letters.add_node(Node('A'))
    letters.add_node(Node('A'))
    letters.add_node(Node('A'))
    letters.add_node(Node('A'))
    letters.add_node(Node('A'))
    letters.add_node(Node('A'))
    letters.add_node(Node('C'))
    letters.add_node(Node('D'))
    letters.add_node(Node('D'))
    letters.add_node(Node('A'))

    for n in remove_duplicates(letters):
        print(n.data)
