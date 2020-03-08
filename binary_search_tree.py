from dataclasses import dataclass


@dataclass
class BTElement:
    key: int
    value: object
    left_node = None
    right_node = None
    size = 1


class BinaryTree:
    def __init__(self):
        self.root = None

    # Display realisation taken from
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34014370
    def display(self):
        lines, _, _, _ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right_node is None and node.left_node is None:
            line = '%s' % node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right_node is None:
            lines, n, p, x = self._display_aux(node.left_node)
            s = '%s' % node.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left_node is None:
            lines, n, p, x = self._display_aux(node.right_node)
            s = '%s' % node.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left_node)
        right, m, q, y = self._display_aux(node.right_node)
        s = '%s' % node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def _get_size(self, node):
        return getattr(node, 'size', 0)

    def get(self, key: int, default=None):
        """
        Get value by given key.
        :param key: key from BT
        :param default: what return if BT is empty
        :return: value of given key
        """
        x = self.root

        while x is not None:
            if key < x.key:
                x = x.left_node
            elif key < x.key:
                x = x.right_node
            else:
                return x.value

        return default

    def put(self, key: int, value: object):
        """
        Add key: value pair to BT
        :param key: key
        :param value: value
        :return: None
        """
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return BTElement(key=key, value=value)

        if key < node.key:
            node.left_node = self._put(node.left_node, key, value)
        elif key > node.key:
            node.right_node = self._put(node.right_node, key, value)
        else:
            node.value = value

        node.size = 1 + self._get_size(node.left_node) + self._get_size(node.right_node)
        return node

    def get_floor(self, key):
        """
        Get nearest lower key for given key
        :param key: key for searching
        :return: nearest lower key
        """
        node = self._get_floor(self.root, key)

        if node is None:
            return None

        return node.key

    def _get_floor(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self._get_floor(node.left_node, key)

        right_floor = self._get_floor(node.right_node, key)

        if right_floor is not None:
            return right_floor
        else:
            return node

    def get_size(self):
        """
        Get full size of BT
        :return: size of BT
        """
        return getattr(self.root, 'size', 0)

    def get_rank(self, key):
        """
        How many keys in BT less than given
        :param key: key for search
        :return: numbers of keys less than given
        """
        return self._get_rank(self.root, key)

    def _get_rank(self, node, key):
        if node is None:
            return 0

        if key < node.key:
            return self._get_rank(node.left_node, key)
        elif key > node.key:
            return 1 + self._get_size(node.left_node) + self._get_rank(node.right_node, key)
        else:
            return getattr(node.left_node, 'size', 0)

    def del_min(self):
        """
        Remove minimum value from BT
        :return: None
        """
        self.root = self._del_min(self.root)

    def _del_min(self, node):
        if node.left_node is None:
            return node.right_node

        node.left_node = self._del_min(node.left_node)
        node.size = 1 + self._get_size(node.left_node) + self._get_size(node.right_node)
        return node


if __name__ == '__main__':
    from random import randint

    bt = BinaryTree()

    for _ in range(15):
        i = randint(1, 1000)
        bt.put(i, i)

    print(f'\nBinary tree size: {bt.get_size()}\n')
    bt.display()
    print('--- ' * 27)

    print('Minimum removed')
    bt.del_min()
    bt.display()
    print('--- ' * 27)

    print(bt.get_floor(150))
    print(bt.get_size())
    print(bt.get_rank(150))
    bt.put(150, 150)
    bt.display()
    print('--- '*27)
