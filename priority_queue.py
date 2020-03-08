from dataclasses import dataclass


@dataclass
class PriorityQueueItem:
    weight: int
    item: object


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.queue.append(PriorityQueueItem(0, None))  # item with index 0 not used in this model
        self.queue_size = 0

    # Display realisation adjasted from
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34014370

    def display(self):
        lines, _, _, _ = self._display_aux(1)
        for line in lines:
            print(line)

    def _display_aux(self, id):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if (id * 2 + 1 > self.queue_size) and (id * 2 > self.queue_size):
            line = '%s (%s)' % (self.queue[id].weight, self.queue[id].item)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if id * 2 + 1 > self.queue_size:
            lines, n, p, x = self._display_aux(id * 2)
            s = '%s (%s)' % (self.queue[id].weight, self.queue[id].item)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Two children.
        left, n, p, x = self._display_aux(id * 2)
        right, m, q, y = self._display_aux(id * 2 + 1)
        s = '%s (%s)' % (self.queue[id].weight, self.queue[id].item)
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










    def _exchange(self, i: int, j: int):
        temp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = temp

    def _swim(self, item_id: int):
        while (item_id > 1) and (self.queue[item_id // 2].weight < self.queue[item_id].weight):
            self._exchange(item_id, item_id // 2)
            item_id = item_id // 2

    def _sink(self, item_id: int, bottom: int = None):
        if bottom is None:
            bottom = self.queue_size

        while item_id * 2 <= bottom:
            bigger_child_id = item_id * 2

            if (
                    (bigger_child_id < bottom)
                    and
                    (self.queue[bigger_child_id].weight < self.queue[bigger_child_id + 1].weight)
            ):
                bigger_child_id += 1

            if self.queue[item_id].weight > self.queue[bigger_child_id].weight:
                break

            self._exchange(item_id, bigger_child_id)
            item_id = bigger_child_id

    def add_to_queue(self, item, priority):

        item_to_queue = PriorityQueueItem(weight=priority, item=item)

        self.queue.append(item_to_queue)
        self.queue_size += 1
        self._swim(self.queue_size)

    def pop_max(self):
        if self.queue_size == 0:
            return

        self._exchange(1, self.queue_size)
        item_to_return = self.queue.pop().item
        self.queue_size -= 1
        self._sink(1)
        return item_to_return

    def get_size(self):
        return self.queue_size

    def is_empty(self):
        return bool(self.queue_size)

    def make_queue_from_list(self, sequence):
        if self.queue_size > 0:
            print('Queue is not empty. Please start with empty queue.')
            return

        for i in sequence:
            self.queue.append(PriorityQueueItem(i, i))
            self.queue_size += 1

    def get_sorted(self, reverse=False):
        # Make queue heap-sorted.
        n = self.queue_size
        for item_id in range(n // 2, 0, -1):
            self._sink(item_id)

        while n > 1:
            self._exchange(1, n)
            n -= 1
            self._sink(1, n)

        result = [i.item for i in self.queue[1:]]

        if reverse:
            result.reverse()

        return result


if __name__ == '__main__':
    import time
    from random import randint

    from common import is_sorted

    pq_1 = PriorityQueue()

    for _ in range(15):
        pq_1.add_to_queue(item=randint(20, 25), priority=randint(1, 20))

    print(f'\nQueue size: {pq_1.queue_size}\n\n')
    pq_1.display()

    print()
    print('--- '*27)

    full_time = 0
    times = 10
    size = 3_000

    for _ in range(times):
        pq_2 = PriorityQueue()
        pq_2.make_queue_from_list(range(size))  # unique items
        # pq_2.make_queue_from_list([randint(1, 100) for _ in range(size)])  # items with duplicated keys

        start = time.time()
        sorted_result = pq_2.get_sorted()
        end = time.time()
        full_time += end - start

        if not is_sorted(sorted_result):
            print('Not sorted result!!!')

    print(f'Rounded average time out of 10 executions of "heap_sort" for {size} items:'.ljust(90), end='')
    print(f' {round(full_time / times, 5)} seconds')

    print('--- '*27, end='\n\n')
