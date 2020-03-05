from dataclasses import dataclass


@dataclass
class BTElement:
    key: int
    value: object
    left_element = None
    right_element = None
    size = 1


class BinaryTree:
    def __init__(self):
        self.root = None

    def get(self, key: int, default=None):
        x = self.root

        while x is not None:
            if key < x.key:
                x = x.left_element
            elif key < x.key:
                x = x.right_element
            else:
                return x.value

        return default

    def put(self, key: int, value: object):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return BTElement(key=key, value=value)

        if key < node.key:
            node.left_element = self._put(node.left_element, key, value)
        elif key > node.key:
            node.right_element = self._put(node.right_element, key, value)
        else:
            node.value = value

        node.size = 1 + getattr(node.left_element, 'size', 0) + getattr(node.right_element, 'size', 0)
        return node

    def get_floor(self, key):
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
            return self._get_floor(node.left_element, key)

        right_floor = self._get_floor(node.right_element, key)

        if right_floor is not None:
            return right_floor
        else:
            return node

    def get_size(self):
        return getattr(self.root, 'size', 0)


    def get_rank(self, key)
        return self._get_rank(self.root, key)

    def _get_rank(self, node, key):
     if node is None:
         return 0

     if key < node.key:
         return self._get_rank(node.left_element, key)
     elif key > node.key:
         return 1 + getattr(node.left_element, 'size', 0) + self._get_rank(node.right_element, key)
     else:
         return getattr(node.left_element, 'size', 0)

    def del_min(self):
        self.root = self._del_min(self.root)

    def _del_min(self, node):
        if node.left_element is None:
            return node.right_element

        node.left_element = self._del_min(node.left_element)
        # node.size  # TODO
     
"""
 public void deleteMin()
 { root = deleteMin(root); }
 private Node deleteMin(Node x)
 {
 if (x.left == null) return x.right;
 x.left = deleteMin(x.left);
 x.count = 1 + size(x.left) + size(x.right);
 return x;
 }
"""