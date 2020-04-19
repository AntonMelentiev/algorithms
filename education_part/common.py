import time
from copy import deepcopy


def is_sorted(a: list):
    """
    Check if elements in the given list are in sorted order.
    Implies that all items in the given list are compatible to each other.
    :param a: list
    :return: bool
    """
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


def is_alphabetic_first(a: list):
    """
    Check if elements in the given list are in alphabetic order by first letter.
    Implies all items in the given list are strings.
    :param a: list
    :return: bool
    """
    for i in range(1, len(a)):
        if a[i][0] < a[i - 1][0]:
            return False
    return True


def time_it(func, data: list, check_sort: bool = True, check_alphabetic_first: bool = False):
    full_time = 0

    for _ in range(10):
        new_data = deepcopy(data)
        start = time.time()
        func(new_data)
        end = time.time()
        full_time += (end - start)

        if check_sort:
            if not is_sorted(new_data):
                print(f'"{func.__name__}" doesn\'t sorts list properly')

        if check_alphabetic_first:
            if not is_alphabetic_first(new_data):
                print(f'"{func.__name__}" doesn\'t in alphabetic order')

    full_time /= 10
    rounded_time = round(full_time, 5)
    print(f'Rounded average time out of 10 executions of "{func.__name__}":'.ljust(70), end='')
    print(f' {rounded_time} seconds')
