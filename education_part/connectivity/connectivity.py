class Connectivity:
    def __init__(self):
        self.data = None
        self.length = None

    def union(self, element, to_element):
        raise NotImplementedError

    def is_connected(self, element, to_element):
        raise NotImplementedError

    @staticmethod
    def drop(obj):
        obj.data = [i for i in range(obj.length)]
        print('=== Dropped ===')

    def show_connection(self, element, to_element):
        print(f'id {element} connected to id {to_element}: ', self.is_connected(element, to_element))

    def __repr__(self):
        a = [i for i in range(self.length)]
        b = self.data
        return f'{a} "ids"\n{b}\n'

    def __str__(self):
        return self.__repr__()


class QuickFind(Connectivity):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.data = [i for i in range(length)]

    def union(self, element, to_element):
        if self.is_connected(element, to_element):
            return

        element_value = self.data[element]
        to_element_value = self.data[to_element]

        for i in range(self.length):
            if self.data[i] == element_value:
                self.data[i] = to_element_value

    def is_connected(self, element, to_element):
        return self.data[element] == self.data[to_element]


class QuickUnion(Connectivity):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.data = [i for i in range(length)]

    def _get_root(self, i):

        while i != self.data[i]:
            i = self.data[i]

        return i

    def union(self, element, to_element):
        element_root = self._get_root(element)
        to_element_root = self._get_root(to_element)
        self.data[element_root] = to_element_root

    def is_connected(self, element, to_element):
        return self._get_root(element) == self._get_root(to_element)


class QuickUnionWeighted(QuickUnion):
    def __init__(self, length):
        super().__init__(length)
        self.size_array = [1 for _ in range(length)]

    def union(self, element, to_element):
        element_root = self._get_root(element)
        to_element_root = self._get_root(to_element)

        if element_root == to_element_root:
            return

        if self.size_array[element_root] < self.size_array[to_element_root]:
            self.data[element_root] = to_element_root
            self.size_array[to_element_root] += self.size_array[element_root]
        else:
            self.data[to_element_root] = element_root
            self.size_array[element_root] += self.size_array[to_element_root]


if __name__ == "__main__":
    def connectivity_scenario(find_object):
        print('--- ' * 20)
        print(f'Scenario for {find_object.__class__.__name__}')
        print('--- ' * 20)
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
        print('--- ' * 20)

    connectivity_scenario(find_object=QuickFind(length=10))
    connectivity_scenario(find_object=QuickUnion(length=10))
    connectivity_scenario(find_object=QuickUnionWeighted(length=10))
