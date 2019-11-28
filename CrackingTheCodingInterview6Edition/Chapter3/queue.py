"""
Простейший вариант реализации очереди поверх обычного списка.
Реализовывать Queue нет целесообразности, потому что имеется отдельный
модуль с потокобезопасной версией Queue. Реализация исключительно для
практики.
"""


class Queue:
    """
    Класс, который реализует очередь. Выступаает в роли фасада над
    списком, методы которого используются для доступа к содержимому.
    """
    def __init__(self):
        """
        Создаёт пустой список, где будут содержаться данные очереди.
        """
        self.content = []

    def __len__(self):
        """
        Использует длину внутреннего списка как своою собственную.
        :return: длина внутреннего списка.
        """
        return len(self.content)

    def push(self, data):
        """
        Добавляет данные в конец очереди.
        :param data: данные.
        :return: None.
        """
        self.content.append(data)

    def pop(self):
        """
        Берёт данные из начала очереди.
        :return: данные из начала очереди.
        """
        self.content.pop(0)


class Deque:
    """
    Класс, который реализует двусвязеую очередь. Выступаает в роли фасада над
    списком, методы которого используются для доступа к содержимому.
    """
    def __init__(self):
        """
        Создаёт пустой список, где будут содержаться данные двусвязной очереди.
        """
        self.content = []

    def __len__(self):
        """
        Использует длину внутреннего списка как своою собственную.
        :return: длина внутреннего списка.
        """
        return len(self.content)

    def push_front(self, data):
        """
        Добавляет данные в начало двусвязной очереди.
        :param data: данные.
        :return: None.
        """
        self.content.insert(0, data)

    def push_back(self, data):
        """
        Добавляет данные в конец двусвязной очереди.
        :param data: данные.
        :return: None.
        """
        self.content.append(data)

    def pop_front(self):
        """
        Берёт данные из начала очереди.
        :return: данные из начала очереди.
        """
        self.content.pop(0)

    def pop_back(self):
        """
        Берёт данные из конца очереди.
        :return: данные из конца очереди.
        """
        self.content.pop(len(self.content) - 1)
