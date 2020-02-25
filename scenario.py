import copy
import time
from random import randint

from connectivity import QuickFind, QuickUnion, QuickUnionWeighted
from sort_and_shuffle import SortAndShuffle


def is_sorted(a: list):
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


def time_it(func, data: list):
    full_time = 0

    for _ in range(10):
        new_data = copy.deepcopy(data)
        start = time.time()
        func(new_data)
        end = time.time()
        full_time += (end - start)

    full_time /= 10
    rounded_time = round(full_time, 5)
    print(f'Rounded average time out of 10 executions of "{func.__name__}":'.ljust(70), end='')
    print(f' {rounded_time} seconds')


def connectivity_scenario_1(find_object):
    find_object.show_connection(0, 3)

    find_object.union(0, 3)
    find_object.show_connection(0, 3)

    find_object.drop(find_object)
    find_object.show_connection(0, 3)

    find_object.union(0, 3)
    print(find_object)
    find_object.union(0, 4)
    print(find_object)
    find_object.union(3, 5)
    print(find_object)
    find_object.union(9, 1)
    print(find_object)
    find_object.show_connection(5, 4)


# connectivity_scenario_1(find_object=QuickFind(length=10))
# connectivity_scenario_1(find_object=QuickUnion(length=10))
# connectivity_scenario_1(find_object=QuickUnionWeighted(length=10))

def sort_scenario_1(a: int):
    """
    Make list of dimension 'a' shuffle it and then sort it using insertion sort algorithm.
    Print shuffled list and then sorted list.
    :param a: list dimension
    :return: None
    """
    worker = SortAndShuffle()
    b = worker.knuth_shuffle(list(range(a)))

    print(b)
    worker.insertion_sort(b)
    print(b)


def sort_scenario_2(a: int):
    """
    Make list of dimension 'a' shuffle it and then sort it using shell sort algorithm.
    Print shuffled list and then sorted list.
    :param a: list dimension
    :return: None
    """
    worker = SortAndShuffle()
    b = worker.knuth_shuffle(list(range(a)))

    print(b)
    worker.shell_sort(b)
    print(b)


def sort_scenario_3(a: int):
    """
    Make list of dimension 'a' shuffle it and then sort it using merge sort algorithm.
    Print shuffled list and then sorted list.
    :param a: list dimension
    :return: None
    """
    worker = SortAndShuffle()
    b = worker.knuth_shuffle(list(range(a)))

    print(b)
    worker.merge_sort(b)
    print(b)


def sort_scenario_4(a: int):
    """
    Make list of dimension 'a' shuffle it and then sort it using merge sort algorithm.
    Print shuffled list and then sorted list.
    :param a: list dimension
    :return: None
    """
    worker = SortAndShuffle()
    b = worker.knuth_shuffle(list(range(a)))

    print(b)
    worker.merge_sort_bottom_up(b)
    print(b)


def sort_scenario_5(a: int):
    """
    Make list of dimension 'a' shuffle it and then sort it using quick sort algorithm.
    Print shuffled list and then sorted list.
    :param a: list dimension
    :return: None
    """
    worker = SortAndShuffle()
    b = worker.knuth_shuffle(list(range(a)))

    print(b)
    worker.quick_sort(b)
    print(b)


def sort_scenario_6(a: int):
    """
    Make list of dimension 'a' shuffle it and then sort it using 3-way quick sort algorithm.
    Print shuffled list and then sorted list.
    :param a: list dimension
    :return: None
    """
    worker = SortAndShuffle()
    b = worker.knuth_shuffle(list(range(a)))

    print(b)
    worker.three_way_quick_sort(b)
    print(b)


# sort_scenario_1(17)
# sort_scenario_2(17)
# sort_scenario_3(17)
# sort_scenario_4(17)
# sort_scenario_5(17)
# sort_scenario_6(17)


b = SortAndShuffle().knuth_shuffle(list(range(3_000)))
# b = [randint(1, 100) for _ in range(3_000)]
funcs = [
    SortAndShuffle().insertion_sort,
    SortAndShuffle().shell_sort,
    SortAndShuffle().merge_sort,
    SortAndShuffle().merge_sort_bottom_up,
    SortAndShuffle().quick_sort,
    SortAndShuffle().three_way_quick_sort,
]

for func in funcs:
    data = copy.deepcopy(b)
    time_it(func, data)


'''
Results for unique 3000 items:

Rounded average time out of 10 executions of "insertion_sort":         1.04087 seconds
Rounded average time out of 10 executions of "shell_sort":             0.01485 seconds
Rounded average time out of 10 executions of "merge_sort":             0.00961 seconds
Rounded average time out of 10 executions of "merge_sort_bottom_up":   0.01321 seconds
Rounded average time out of 10 executions of "quick_sort":             0.00742 seconds  # without shuffle
Rounded average time out of 10 executions of "quick_sort":             0.01311 seconds
Rounded average time out of 10 executions of "three_way_quick_sort":   0.01293 seconds


Results for 3000 items with a lot of duplicates:

Rounded average time out of 10 executions of "insertion_sort":         1.04107 seconds
Rounded average time out of 10 executions of "shell_sort":             0.01143 seconds
Rounded average time out of 10 executions of "merge_sort":             0.01179 seconds
Rounded average time out of 10 executions of "merge_sort_bottom_up":   0.01416 seconds
Rounded average time out of 10 executions of "quick_sort":             0.01245 seconds  # without shuffle
Rounded average time out of 10 executions of "quick_sort":             0.0149 seconds
Rounded average time out of 10 executions of "three_way_quick_sort":   0.0078 seconds
'''