import time

from connectivity import QuickFind, QuickUnion, QuickUnionWeighted
from sort_and_shuffle import SortAndShuffle


def is_sorted(a: list):
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True


def time_it(func, *args, **kwargs):
    full_time = 0

    for _ in range(10):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        full_time += (end - start)

    full_time /= 10
    rounded_time = round(full_time, 5)
    print(f'Average time out of 10 executions: {rounded_time} seconds')


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


# sort_scenario_1(17)
# sort_scenario_2(17)
# sort_scenario_3(17)
# sort_scenario_4(17)


b = SortAndShuffle().knuth_shuffle(list(range(100_000)))
func = SortAndShuffle().merge_sort
time_it(func, b)
print(is_sorted(b))

