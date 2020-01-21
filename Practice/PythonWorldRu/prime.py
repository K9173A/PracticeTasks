"""
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и
возвращающую True, если оно простое, и False - иначе.
"""


def is_prime(number):
    """
    Определяет, является ли переданное число простым.
    :param number: число.
    :return: булевое значение, отвечающее на вопрос, является ли переданное
    число простым.
    """
    if number in [1, 2]:
        return True
    else:
        return 0 not in [number % i for i in range(2, number)]
