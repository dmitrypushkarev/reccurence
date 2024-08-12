"""Несколько функций с использованием рекурсии."""


def summa(ls: list) -> int:
    """Получение суммы"""
    if not ls:
        return 0
    else:
        return ls[0] + summa(ls[1:])


def len_elements(ls: list) -> int:
    """Получение длины списка"""
    if not ls:
        return 0
    else:
        return len_elements(ls[1:]) + 1


def max_element(ls: list) -> int:
    """Получение максимального элемента в списке"""
    if len(ls) == 2:
        return ls[0] if ls[0] > ls[1] else ls[1]
    sub_max = max_element(ls[1:])
    return ls[0] if ls[0] > sub_max else sub_max


def in_out():
    """Функция input - output"""
    import random
    ls_input = [random.randint(1, 30) for _ in range(int(input("Введите количество элементов в списке: ")))]
    print(f'Сгенерировался список: {ls_input}')
    print(f'Сумма элементов списка: {summa(ls_input)}')
    print(f'Длина списка: {len_elements(ls_input)}')
    print(f'Максимальный элемент в списке: {max_element(ls_input)}')


if __name__ == '__main__':
    in_out()
