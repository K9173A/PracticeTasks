"""
Написать функцию arithmetic, принимающую 3 аргумента: первые два - числа,
третий - операция, которая должна быть произведена над ним. Если третий
аргумент +, сложить их, если -, то вычесть; * - умножить / — разделить
(первое на второе). В остальных случаях вернуть строку "Неизвестная
операция".
"""


def arithmetic(left_operand, right_operand, operation):
    """
    Применяет заданную в параметре operation математичечскую операцию к
    left_operand и right_operand. Операция должна быть бинарной.
    :param left_operand: левый операнд.
    :param right_operand: правый операнд.
    :param operation: символ операции в виде строки.
    :return: числовой результат применения операции.
    """
    if type(left_operand) != int or type(right_operand) != int:
        raise TypeError('Неверный тип данных!')
    if operation == '+':
        return left_operand + right_operand
    elif operation == '-':
        return left_operand - right_operand
    elif operation == '*':
        return left_operand * right_operand
    elif operation == '/':
        return left_operand / right_operand
    else:
        raise ValueError('Неизвестная операция!')
