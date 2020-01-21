"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето
или осень).
"""


def season(month_number):
    """
    Возвращает название сезона по номеру месяца.
    :param month_number: номер месяца.
    :return: строка с названием сезона.
    """
    if month_number in [1, 2, 12]:
        return 'Winter'
    elif 3 <= month_number <= 5:
        return 'Spring'
    elif 6 <= month_number <= 8:
        return 'Summer'
    elif 9 <= month_number <= 11:
        return 'Autumn'
    raise ValueError('Неверный номер месяца!')
