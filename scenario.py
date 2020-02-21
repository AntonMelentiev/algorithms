from connectivity import QuickFind, QuickUnion, QuickUnionWeighted
from sort_and_shuffle import SortAndShuffle


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

def sort_scenario_1(a):
    shell_sort = SortAndShuffle()
    b = shell_sort.knuth_shuffle(list(range(a)))

    print(b)
    print(shell_sort.shell_sort(b))


def sort_scenario_2(a):
    shell_sort = SortAndShuffle()
    b = shell_sort.knuth_shuffle(list(range(a)))

    print(b)
    print(shell_sort.merge_sort(b))


# sort_scenario_1(17)
# sort_scenario_2(17)
