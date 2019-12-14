"""
Пользователь делает вклад в размере a рублей сроком на years лет под 10%
годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги
прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму,
которая будет на счету пользователя.
"""


def bank(deposit_sum, deposit_years):
    """
    Вычисляет итоговую сумму депозита.
    :param deposit_sum: сумма депозита.
    :param deposit_years: годовой процент депозита.
    :return: итоговая сумма депозита.
    """
    percent = 0.1
    for _ in range(deposit_years):
        deposit_sum += deposit_sum * percent
    return int(deposit_sum)