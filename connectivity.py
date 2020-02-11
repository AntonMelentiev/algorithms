class Connectivity:
    def union(self, element, to_element):
        raise NotImplementedError

    def is_connected(self, element, to_element):
        raise NotImplementedError

    def drop(self):
        raise NotImplementedError

    def show_connection(self, element, to_element):
        raise NotImplementedError

    def show_data(self):
        raise NotImplementedError


class QuickFind(Connectivity):
    def __init__(self, length):
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

    def drop(self):
        self.data = [i for i in range(self.length)]
        print('=== Dropped ===')

    def show_connection(self, element, to_element):
        print(f'id {element} connected to id {to_element}: ', self.is_connected(element, to_element))

    def show_data(self):
        print([i for i in range(self.length)], '"ids"')
        print(self.data, end='\n\n')


class QuickUnion(Connectivity):
    def __init__(self, length):
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

    def drop(self):
        self.data = [i for i in range(self.length)]
        print('=== Dropped ===')

    def show_connection(self, element, to_element):
        print(f'id {element} connected to id {to_element}: ', self.is_connected(element, to_element))

    def show_data(self):
        print([i for i in range(self.length)], '"ids"')
        print(self.data, end='\n\n')
