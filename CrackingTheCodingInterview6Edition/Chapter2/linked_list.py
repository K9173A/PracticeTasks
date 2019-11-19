"""
Простейший вариант реализации связного списка.
"""


class Node:
    """
    Класс, который реализует нод для связного списка. Нод может хранить
    данные. Также каждый нод хранит ссылку на следующий нод. В чём как раз
    и заключается смысл связного списка.
    """
    def __init__(self, data=None, next_node=None):
        """
        Инициализирует нод данными и следующим нодом.
        :param data: данные.
        :param next_node: следующий нод.
        """
        self.data = data
        self.next_node = next_node

    def set_next_node(self, next_node):
        """
        Устанавливает новый следующий нод для данного нода.
        :param next_node: новый нод.
        :return: None.
        """
        self.next_node = next_node

    def set_data(self, data):
        """
        Устанаилвает новые данные, которые будут храиться в данном ноде.
        :param data: новые данные.
        :return: None.
        """
        self.data = data


class LinkedList:
    """
    Простая реализация связного списка.
    """
    def __init__(self):
        """
        Инициализирует пустой связный список.
        """
        self.head_node = None

    def __iter__(self):
        """
        Итерируется через связный список, возвращая следующий нод за один
        цикл. Если больше нодов нет, то выкидывает StopIteration, который
        сигнализирует, чтоб итерация прекратилась.
        :return: объект нода.
        """
        # В начале устанавливаем текущим нодом корневой нод, с которого будет
        # начинаться итерация по связному списку
        current_node = self.head_node
        # В цикле проверяем текущий нод: если он равен None, то значит мы
        # добрилсь до последнего нода. Если связный список пустой, то
        # корневой нод тоже будет пустым.
        while current_node:
            # Возвращаем через yield текущий нод. Так как в цикле проверяется
            # наличие текущего нода, то значит на текущем этапе однозначно
            # он существует и не равен None.
            yield current_node
            # После этого перезаписываем в текущий нод следующий нод.
            current_node = current_node.next_node

    def __len__(self):
        """
        Вычисляет длину связного списка.
        :return: длина связного списка.
        """
        return sum(1 for _ in self)

    def clear(self):
        """
        Очищает связный список от нодов.
        :return: None.
        """
        current_node = None
        for node in self:
            if current_node:
                current_node.set_next_node(None)
            current_node = node

    def peak(self):
        """
        Возвращает последний нод из связного списка.
        Если список пуст, то возвращает None.
        :return: последний нод.
        """
        last_node = None
        for node in self:
            last_node = node
        return last_node

    def add_node(self, node):
        """
        Добавляет нод в конец связного списка.
        :param node: новый нод, который нужно добавить.
        :return: None.
        """
        last_node = self.peak()
        # Если корневой нод не равен None, значит связный список не пуст.
        if last_node:
            # Тогда устанавливаем ссылку в последний нод на добавляемый нод.
            last_node.set_next_node(node)
        # Если корневой нод равен None, то устанавливаем текущий нод корневым.
        else:
            self.head_node = node


def main():
    linked_list = LinkedList()
    linked_list.add_node(Node('Monday'))
    linked_list.add_node(Node('Tuesday'))
    linked_list.add_node(Node('Wednesday'))
    linked_list.add_node(Node('Thursday'))
    linked_list.add_node(Node('Friday'))
    linked_list.add_node(Node('Saturday'))
    linked_list.add_node(Node('Sunday'))

    for node in linked_list:
        print(node.data)

    linked_list.clear()


if __name__ == '__main__':
    main()
