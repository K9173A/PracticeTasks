"""
Написать функцию date, принимающую 3 аргумента — день, месяц и год.
Вернуть True, если такая дата есть в нашем календаре, и False иначе.
"""
import datetime


def date(day, month, year):
    """
    Проверяет, существует ли дата.
    :param day: номер дня в месяце.
    :param month: номер месяца в году.
    :param year: год.
    :return: если дата существует, то возвращает True, в ином случае возвращает
    False.
    """
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True
