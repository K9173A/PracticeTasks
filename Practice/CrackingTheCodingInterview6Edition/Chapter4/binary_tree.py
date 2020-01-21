"""
Binary tree implementation.
"""
import enum


class Side(enum.Enum):
    """
    Enum для переходов от одного нода к другому.
    """
    LEFT = 0
    RIGHT = 1


class Node:
    """
    Реализация нода для бинарного дерева.
    """
    def __init__(self, data):
        """
        Создаёт нод с ссылками на левый и правый ноды.
        :param data: данные для записи в нод.
        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Реализация бинарного дерева.
    """
    def __init__(self, node):
        """
        Создаёт бинарное дерево с корневым нодом.
        :param node: узловой нод.
        """
        self.root_node = node

    def add_node(self, node, path):
        """
        Добавляет нод в дерево в место, определённое в path.
        path представляет из себя список переходов от корневого нода к
        следующему: [left, right, right, ...]
        :param node: нод, который нужно добавить.
        :param path: путь добавления нода.
        :return: None.
        """
        current_node = self.root_node
        if len(path) == 0:
            self.root_node = node
        for index, side in enumerate(path):
            if side not in [Side.LEFT, Side.RIGHT]:
                raise ValueError('Incorrect Side value!')
            # Если мы не дошли до последнего элемента side, то его значение
            # None может означать неправильно прописанный путь до нода:
            # дерево просто не будет иметь последующих ветвей и неожиданно
            # закончится.
            attribute_name = 'left' if side == Side.LEFT else 'right'
            if index < len(path) - 1:
                current_node = getattr(current_node, attribute_name, None)
                if current_node is None:
                    raise ValueError('Incorrect path!')
            # У последнего нода значение правого или левого нода могут быть
            # равны None.
            else:
                setattr(current_node, attribute_name, node)


if __name__ == '__main__':
    bt = BinaryTree(Node(1))
    bt.add_node(Node(2), [Side.LEFT])
    bt.add_node(Node(3), [Side.RIGHT])
    bt.add_node(Node(4), [Side.RIGHT, Side.RIGHT])
