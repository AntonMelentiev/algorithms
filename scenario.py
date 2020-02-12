from connectivity import QuickFind, QuickUnion, QuickUnionWeighted


def scenario_1(find_object):
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


# scenario_1(find_object=QuickFind(length=10))
scenario_1(find_object=QuickUnion(length=10))
scenario_1(find_object=QuickUnionWeighted(length=10))
